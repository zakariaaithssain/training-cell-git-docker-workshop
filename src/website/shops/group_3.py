"""Group 3 Shop - EDIT THIS FILE ONLY.

Each member adds their own products to the inventory list.
You may also add individual GET endpoints if you want.
"""

from fastapi import APIRouter
from typing import List
from website.core.models import Product

router = APIRouter()

# ═══════════════════════════════════════════════════════════
# GROUP 3: ADD YOUR PRODUCTS BELOW THIS LINE
# ═══════════════════════════════════════════════════════════
inventory: List[Product] = [
    # Example (feel free to delete after adding your own):
    Product(name="3 Sample", price=7.00, category="demo"),
]

# ═══════════════════════════════════════════════════════════
# END OF GROUP 3 EDIT ZONE
# ═══════════════════════════════════════════════════════════


@router.get("/products", response_model=List[Product])
def get_products():
    """Return all products in 3 Shop."""
    return inventory
