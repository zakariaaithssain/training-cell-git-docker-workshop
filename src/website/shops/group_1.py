"""Group 1 Shop - EDIT THIS FILE ONLY.

Each member adds their own products to the inventory list.
You may also add individual GET endpoints if you want.
"""

from fastapi import APIRouter
from typing import List
from website.core.models import Product

router = APIRouter()

# ═══════════════════════════════════════════════════════════
# GROUP 1: ADD YOUR PRODUCTS BELOW THIS LINE
# ═══════════════════════════════════════════════════════════
inventory: List[Product] = [
    # Example (feel free to delete after adding your own):
    Product(name="1 Sample", price=9.99, category="demo"),
]

# ═══════════════════════════════════════════════════════════
# END OF GROUP 1 EDIT ZONE
# ═══════════════════════════════════════════════════════════


@router.get("/products", response_model=List[Product])
def get_products():
    """Return all products in 1 Shop."""
    return inventory
