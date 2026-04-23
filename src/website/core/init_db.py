from sqlalchemy.orm import Session
from website.core.database import engine, Base
from website.core.models import DBProduct
from website.shops import group_1

def init_db():
    # Create tables
    Base.metadata.create_all(bind=engine)
    
def seed_data(db: Session):
    # Mapping of shop_id to their inventory module
    shops_data = {
        "1": group_1.inventory,
    }
    
    # We DO NOT clear existing data anymore to preserve purchases and users.
    
    for shop_id, inventory in shops_data.items():
        for item in inventory:
            # Check if product already exists by name
            db_product = db.query(DBProduct).filter(DBProduct.name == item.name).first()
            if db_product:
                # Update existing (in case they changed price/desc in git)
                db_product.price = item.price
                db_product.category = item.category
                db_product.description = item.description
                db_product.image_filename = item.image_filename
                # Note: We don't update stock to preserve the competition state!
            else:
                # Insert new
                db_product = DBProduct(
                    shop_id=shop_id,
                    name=item.name,
                    price=item.price,
                    category=item.category,
                    description=item.description,
                    image_filename=item.image_filename,
                    stock=item.stock
                )
                db.add(db_product)
    
    db.commit()
