"""Group 2 Shop - EDIT THIS FILE ONLY.

Each member adds their own products to the inventory list.
You may also add individual GET endpoints if you want.
"""

from fastapi import APIRouter
from typing import List
from website.core.models import Product

router = APIRouter()

# ═══════════════════════════════════════════════════════════
# GROUP 2: ADD YOUR PRODUCTS BELOW THIS LINE
# ═══════════════════════════════════════════════════════════
inventory: List[Product] = [
    # Example (feel free to delete after adding your own):
    Product(name="2 Sample", price=12.50, category="demo"),
]

# ═══════════════════════════════════════════════════════════
# END OF GROUP 2 EDIT ZONE
# ═══════════════════════════════════════════════════════════


@router.get("/products", response_model=List[Product])
def get_products():
    """Return all products in 2 Shop."""
    return inventory
