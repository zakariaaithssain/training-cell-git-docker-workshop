"""Group 1 Shop - EDIT THIS FILE ONLY.

Each member adds their own products to the inventory list.
You may also add individual GET endpoints if you want.
"""

from fastapi import APIRouter
from typing import List
from website.core.models import Product

router = APIRouter()
shop_name = "InstructorStore"

# ═══════════════════════════════════════════════════════════
# GROUP 1: ADD YOUR PRODUCTS BELOW THIS LINE
# ═══════════════════════════════════════════════════════════
inventory: List[Product] = [
    Product(name="T-shirt nadi", price=170.00, category="Clothing", stock=20, image_filename="sample1.jfif"),
    Product(name="9ra 3la rassek", price=85.00, category="Agenda", stock=20, image_filename="sample2.jfif"),
    Product(name="Chreb o skot", price=55.00, category="Mug", stock=20, image_filename="sample3.jpg"),
]

# ═══════════════════════════════════════════════════════════
# END OF GROUP 1 EDIT ZONE
# ═══════════════════════════════════════════════════════════


@router.get("/products", response_model=List[Product])
def get_products():
    """Return all products in this Shop."""
    return inventory

