from pydantic import BaseModel
from datetime import datetime

class Order(BaseModel):
    customer_name: str
    product_id: int
    quantity: int
    order_date: datetime

    