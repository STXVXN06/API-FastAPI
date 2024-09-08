from fastapi import APIRouter, Body
from models.vechicle import Vehicle
from database import VehicleModel

vehicle_router = APIRouter()

@vehicle_router.get("/vehicles")
def get_vehicles():

    try:
        vehicles = VehicleModel.select().where(VehicleModel.id > 0).dicts()
        if vehicles:
            return list(vehicles)
    except VehicleModel.DoesNotExist:
        return "No vehicles found"
    
@vehicle_router.get("/vehicles/{vehicle_id}")
def get_vehicle(vehicle_id: int):
    try:
        vehicle = VehicleModel.get(VehicleModel.id == vehicle_id)
        return vehicle
    except VehicleModel.DoesNotExist:
        return "Vehicle not found"
    
@vehicle_router.post("/vehicles")
def create_vehicle(vehicle: Vehicle = Body(...)):
    vehicle = VehicleModel.create(make=vehicle.make, model=vehicle.model, year=vehicle.year, color=vehicle.color)
    return vehicle

@vehicle_router.put("/vehicles/{vehicle_id}")
def update_vehicle(vehicle_id: int, vehicle_data: dict):
    VehicleModel.update(**vehicle_data).where(VehicleModel.id == vehicle_id).execute()
    vehicle = VehicleModel.get(VehicleModel.id == vehicle_id)
    return vehicle

@vehicle_router.delete("/vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id: int):
    try:
        vehicle = VehicleModel.get(VehicleModel.id == vehicle_id)
        if vehicle:
            vehicle.delete_instance()
            return {"message": "Vehicle deleted successfully"}
        else:
            raise VehicleModel.DoesNotExist(status_code=404, detail="Vehicle not found")
    except VehicleModel.DoesNotExist:
        return "Vehicle not found"

