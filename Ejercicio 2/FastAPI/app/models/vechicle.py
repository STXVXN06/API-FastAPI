from pydantic import BaseModel

class Vehicle(BaseModel):
    make: str
    model: str
    year: int
    color: str