from fastapi import APIRouter, Body
from ..models.product import Product

product_router = APIRouter()

@product_router.get("/products")
def get_products():


    return "No products found"
        

@product_router.get("/products/{product_id}")
def get_product(product_id: int):
    
    return "Product"

@product_router.post("/products")
def create_product(product: Product = Body(...)):

    return product

@product_router.put("/products/{product_id}")
def update_product(product_id: int, product_data: dict):
   
    return "Product updated"

@product_router.delete("/products/{product_id}")
def delete_product(product_id: int):
   
    return "Product deleted"
