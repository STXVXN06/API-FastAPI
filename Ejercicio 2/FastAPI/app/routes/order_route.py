from fastapi import APIRouter, Body
from ..models.order import Order


order_router = APIRouter()

@order_router.get("/orders")
def get_orders():

    return "Orders"
    
@order_router.get("/orders/{order_id}")
def get_order(order_id: int):
    
    return "Order"
    
@order_router.post("/orders")
def create_order(order: Order = Body(...)):
    return order

@order_router.put("/orders/{order_id}")
def update_order(order_id: int, order_data: dict):
    return "Order updated"

@order_router.delete("/orders/{order_id}")
def delete_order(order_id: int):
    
    return "Order deleted"

