from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Depends, HTTPException, Form, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy import func
import os

from website.shops import group_1
from website.core.database import get_db, engine
from website.core.init_db import init_db, seed_data
from website.core.models import DBProduct, DBUser, DBPurchase
from website.core.config import settings

# Lifespan context to initialize DB on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    with Session(engine) as session:
        seed_data(session)
    yield

app = FastAPI(
    title="Workshop Marketplace",
    description="A collaborative FastAPI project for learning Git & Docker.",
    version="1.0.0",
    lifespan=lifespan
)

# Setup Templates and Static files
app.mount("/static", StaticFiles(directory="website/static"), name="static")
templates = Jinja2Templates(directory="website/templates")

# Include shop routers (API)
app.include_router(group_1.router, prefix="/api/1", tags=["1 Shop"])


# --- DEPENDENCIES ---
def get_current_user(request: Request, db: Session = Depends(get_db)):
    username = request.cookies.get("session_user")
    if not username:
        return None
    user = db.query(DBUser).filter(DBUser.username == username).first()
    return user


# --- AUTH ROUTES ---
@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse(request=request, name="login.html", context={})

@app.post("/login")
async def login(response: Response, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(DBUser).filter(DBUser.username == username).first()
    if not user:
        # Auto-register for the workshop to keep it simple
        user = DBUser(username=username, password=password)
        db.add(user)
        db.commit()
    elif user.password != password:
        # Minimalist error handling
        return RedirectResponse(url="/login?error=Mauvais mot de passe", status_code=303)
        
    response = RedirectResponse(url="/", status_code=303)
    response.set_cookie(key="session_user", value=username, httponly=True)
    return response

@app.get("/logout")
async def logout(response: Response):
    response = RedirectResponse(url="/", status_code=303)
    response.delete_cookie("session_user")
    return response


# --- WEB ROUTES ---
@app.get("/")
async def index_web(request: Request, user: DBUser = Depends(get_current_user)):
    if not user:
        return RedirectResponse(url="/login", status_code=303)
        
    shops = [
        {"id": "1", "name": group_1.shop_name}
    ]
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"shops": shops, "user": user}
    )

@app.get("/shop/{shop_id}")
async def shop_web(request: Request, shop_id: str, db: Session = Depends(get_db), user: DBUser = Depends(get_current_user)):
    if not user:
        return RedirectResponse(url="/login", status_code=303)
        
    # Get products for this shop and pre-load their purchases
    products = db.query(DBProduct).filter(DBProduct.shop_id == shop_id).all()
    
    # Has the current user already bought anything overall?
    has_voted = False
    voted_product_id = None
    if user:
        purchase = db.query(DBPurchase).filter(DBPurchase.user_id == user.id).first()
        if purchase:
            has_voted = True
            voted_product_id = purchase.product_id
        
    shop_module = {"1": group_1}.get(shop_id)
    shop_name = shop_module.shop_name if shop_module else f"Magasin {shop_id}"
        
    return templates.TemplateResponse(
        request=request,
        name="shop.html",
        context={"shop_id": shop_id, "shop_name": shop_name, "products": products, "user": user, "has_voted": has_voted, "voted_product_id": voted_product_id}
    )


# --- GLOBAL API ACTIONS ---
@app.post("/api/buy/{product_id}")
def buy_product(product_id: int, db: Session = Depends(get_db), user: DBUser = Depends(get_current_user)):
    if not user:
        raise HTTPException(status_code=401, detail="Vous devez être connecté pour acheter")
        
    # Check if user already bought something
    existing_purchase = db.query(DBPurchase).filter(DBPurchase.user_id == user.id).first()
    if existing_purchase:
        raise HTTPException(status_code=403, detail="Vous avez déjà utilisé votre crédit d'achat ! (1 achat max)")
        
    product = db.query(DBProduct).filter(DBProduct.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
        
    if product.stock <= 0:
        raise HTTPException(status_code=400, detail="Rupture de stock")
        
    # Process purchase
    product.stock -= 1
    new_purchase = DBPurchase(user_id=user.id, product_id=product.id)
    db.add(new_purchase)
    db.commit()
    
    return {"message": "Achat validé pour la compétition !", "new_stock": product.stock, "buyer": user.username}

@app.post("/api/cancel_buy/{product_id}")
def cancel_buy_product(product_id: int, db: Session = Depends(get_db), user: DBUser = Depends(get_current_user)):
    if not user:
        raise HTTPException(status_code=401, detail="Vous devez être connecté pour annuler un achat")
        
    # Find the purchase for this user and product
    purchase = db.query(DBPurchase).filter(DBPurchase.user_id == user.id, DBPurchase.product_id == product_id).first()
    if not purchase:
        raise HTTPException(status_code=404, detail="Vous n'avez pas acheté ce produit")
        
    product = db.query(DBProduct).filter(DBProduct.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
        
    # Reverse purchase
    product.stock += 1
    db.delete(purchase)
    db.commit()
    
    return {"message": "Achat annulé", "new_stock": product.stock, "buyer": user.username}


# --- RESULTS ROUTE ---
@app.get("/results")
async def results_page(request: Request, db: Session = Depends(get_db)):
    if not settings.show_results:
        # Si la fonctionnalité n'est pas activée, on redirige vers l'accueil
        return RedirectResponse(url="/", status_code=303)
        
    # Requête SQL pour obtenir le classement
    leaderboard = db.query(
        DBProduct, 
        func.count(DBPurchase.id).label('purchase_count')
    ).outerjoin(
        DBPurchase
    ).group_by(
        DBProduct.id
    ).order_by(
        func.count(DBPurchase.id).desc()
    ).all()
    
    # Mapper les shop_id aux noms créatifs
    shop_modules = {"1": group_1}
    
    formatted_results = []
    for product, count in leaderboard:
        mod = shop_modules.get(product.shop_id)
        shop_name = mod.shop_name if mod else f"Magasin {product.shop_id}"
        formatted_results.append({
            "product_name": product.name,
            "shop_name": shop_name,
            "purchases": count
        })
        
    winner = formatted_results[0] if formatted_results else None
    
    return templates.TemplateResponse(
        request=request,
        name="results.html",
        context={"winner": winner, "leaderboard": formatted_results}
    )
