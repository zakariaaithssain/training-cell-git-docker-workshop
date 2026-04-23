#### DO NOTT EDIT THIS FILE HHH ### 
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from website.core.database import Base


# SQLAlchemy Models
class DBUser(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)  # Simple plain text for workshop
    purchases = relationship("DBPurchase", back_populates="user")

class DBPurchase(Base):
    __tablename__ = "purchases"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    
    user = relationship("DBUser", back_populates="purchases")
    product = relationship("DBProduct", back_populates="purchases")

class DBProduct(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    shop_id = Column(String, index=True)  # To know which shop it belongs to (e.g. '1', '2')
    name = Column(String, index=True, unique=True) # Ensure unique name for upserting
    price = Column(Float)
    category = Column(String)
    description = Column(String, default="Ce produit a été ajouté par un de tes collègues.")
    image_filename = Column(String, default="default.jpg")
    stock = Column(Integer, default=20)
    
    purchases = relationship("DBPurchase", back_populates="product")


# Pydantic Schema (for API typing and Git files)
class Product(BaseModel):
    name: str
    price: float
    category: str
    description: str = "Ce produit a été ajouté par un de tes collègues."
    image_filename: str = "default.jpg"
    stock: int = 20
