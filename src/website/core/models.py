#### DO NOTT EDIT THIS FILE HHH ### 
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    category: str
