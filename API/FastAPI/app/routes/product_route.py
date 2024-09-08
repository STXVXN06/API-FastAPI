from fastapi import APIRouter, Body
from models.product import Product
from database import ProductModel

product_router = APIRouter()

@product_router.get("/products")
def get_products():

    try:
        products = ProductModel.select().where(ProductModel.id > 0).dicts()
        if products:
            return list(products)
    except ProductModel.DoesNotExist:
        return "No products found"
        

@product_router.get("/products/{product_id}")
def get_product(product_id: int):
    try:
        product = ProductModel.get(ProductModel.id == product_id)
        return product
    except ProductModel.DoesNotExist:
        return "Product not found"

@product_router.post("/products")
def create_product(product: Product = Body(...)):
    product = ProductModel.create(name=product.name, description=product.description, price=product.price, stock=product.stock)
    return product

@product_router.put("/products/{product_id}")
def update_product(product_id: int, product_data: dict):
    ProductModel.update(**product_data).where(ProductModel.id == product_id).execute()
    product = ProductModel.get(ProductModel.id == product_id)
    return product

@product_router.delete("/products/{product_id}")
def delete_product(product_id: int):
    try:
        product = ProductModel.get(ProductModel.id == product_id)
        if product:
            product.delete_instance()
            return {"message": "Product deleted successfully"}
        else:
            raise ProductModel.DoesNotExist(status_code=404, detail="Product not found")
    except ProductModel.DoesNotExist:
        return "Product not found"
