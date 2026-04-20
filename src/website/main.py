#### DO NOT TOUUCH THIS CODE HHHHH #### 

from fastapi import FastAPI
from website.shops import group_1, group_2, group_3

app = FastAPI(
    title="Workshop Marketplace",
    description="A collaborative FastAPI project for learning Git & Docker.",
    version="1.0.0",
)

# Include shop routers
app.include_router(group_1.router, prefix="/1", tags=["1 Shop"])
app.include_router(group_2.router, prefix="/2", tags=["2 Shop"])
app.include_router(group_3.router, prefix="/3", tags=["3 Shop"])


@app.get("/")
def root():
    return {
        "message": "Welcome to the Workshop Marketplace!",
        "shops": ["/1/products", "/2/products", "/3/products"],
    }
