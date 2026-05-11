from fastapi import APIRouter
from pydantic import BaseModel
from website.core.models import Product

router = APIRouter()
shop_name = "testt shop"

# les membres : ajoutez vos  produits ici
inventory: list[Product] = [
    Product(name="Chreb o skot", price=55.00, category="Mug", stock=20, image_filename="sample3.jpg"),
]
@router.get("/products")
def get_products():
    return inventory