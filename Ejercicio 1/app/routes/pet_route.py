from fastapi import APIRouter, Body
from ..models.pet import Pet

pet_router = APIRouter()

@pet_router.get("/pets")
def get_pets():

    return "No pets found"
    
@pet_router.get("/pets/{pet_id}")
def get_pet(pet_id: int):
   
    return "Pet"
    
@pet_router.post("/pets")
def create_pet(pet: Pet = Body(...)):
    return pet

@pet_router.put("/pets/{pet_id}")
def update_pet(pet_id: int, pet_data: dict):
    return "Pet updated"

@pet_router.delete("/pets/{pet_id}")
def delete_pet(pet_id: int):
   
    return "Pet deleted"

