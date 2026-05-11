from fastapi import APIRouter
from pydantic import BaseModel
from website.core.models import Product

router = APIRouter()
shop_name = "testt shop"
class ProductItem(BaseModel):
    name: str
    price: float
    category: str
    description: str
    image_filename: str
    stock: int = 10
# les membres : ajoutez vos  produits ici
inventory = [
        Product(name="Chreb o skotx2", price=57.00, category="Mug", stock=20, image_filename="sample3.jpg")
]
@router.get("/products")
def get_products():
    return inventory