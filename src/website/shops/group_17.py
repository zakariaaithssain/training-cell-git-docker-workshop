from fastapi import APIRouter
from pydantic import BaseModel
from website.core.models import Product

router = APIRouter()
shop_name = "group_17"
class ProductItem(BaseModel):
    name: str
    price: float
    category: str
    description: str
    image_filename: str
    stock: int = 10
# les membres : ajoutez vos  produits ici
inventory = [
]
@router.get("/products")
def get_products():
    return inventory
