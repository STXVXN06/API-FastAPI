from fastapi import APIRouter, Body
from ..models.vechicle import Vehicle

vehicle_router = APIRouter()

@vehicle_router.get("/vehicles")
def get_vehicles():
    return "No vehicles found"
    
@vehicle_router.get("/vehicles/{vehicle_id}")
def get_vehicle(vehicle_id: int):
    
    return "Vehicle"
    
@vehicle_router.post("/vehicles")
def create_vehicle(vehicle: Vehicle = Body(...)):

    return vehicle

@vehicle_router.put("/vehicles/{vehicle_id}")
def update_vehicle(vehicle_id: int, vehicle_data: dict):
   
    return "Vehicle updated"

@vehicle_router.delete("/vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id: int):
    
    return "Vehicle deleted"

