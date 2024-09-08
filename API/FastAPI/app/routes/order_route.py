from fastapi import APIRouter, Body
from models.order import Order
from database import OrderModel
from datetime import datetime

order_router = APIRouter()

@order_router.get("/orders")
def get_orders():

    try:
        orders = OrderModel.select().where(OrderModel.id > 0).dicts()
        if orders:
            return list(orders)
    except OrderModel.DoesNotExist:
        return "No orders found"
    
@order_router.get("/orders/{order_id}")
def get_order(order_id: int):
    try:
        order = OrderModel.get(OrderModel.id == order_id)
        return order
    except OrderModel.DoesNotExist:
        return "Order not found"
    
@order_router.post("/orders")
def create_order(order: Order = Body(...)):
    order = OrderModel.create(customer_name=order.customer_name, product_id=order.product_id, quantity=order.quantity, order_date=datetime.now())
    return order

@order_router.put("/orders/{order_id}")
def update_order(order_id: int, order_data: dict):
    OrderModel.update(**order_data).where(OrderModel.id == order_id).execute()
    order = OrderModel.get(OrderModel.id == order_id)
    return order

@order_router.delete("/orders/{order_id}")
def delete_order(order_id: int):
    try:
        order = OrderModel.get(OrderModel.id == order_id)
        if order:
            order.delete_instance()
            return {"message": "Order deleted successfully"}
        else:
            raise OrderModel.DoesNotExist(status_code=404, detail="Order not found")
    except OrderModel.DoesNotExist:
        return "Order not found"

