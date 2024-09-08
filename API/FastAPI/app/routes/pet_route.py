from fastapi import APIRouter, Body
from models.pet import Pet
from database import PetModel

pet_router = APIRouter()

@pet_router.get("/pets")
def get_pets():

    try:
        pets = PetModel.select().where(PetModel.id > 0).dicts()
        if pets:
            return list(pets)
    except PetModel.DoesNotExist:
        return "No pets found"
    
@pet_router.get("/pets/{pet_id}")
def get_pet(pet_id: int):
    try:
        pet = PetModel.get(PetModel.id == pet_id)
        return pet
    except PetModel.DoesNotExist:
        return "Pet not found"
    
@pet_router.post("/pets")
def create_pet(pet: Pet = Body(...)):
    pet = PetModel.create(name=pet.name, species=pet.species, age=pet.age, owner_name=pet.owner_name)
    return pet

@pet_router.put("/pets/{pet_id}")
def update_pet(pet_id: int, pet_data: dict):
    PetModel.update(**pet_data).where(PetModel.id == pet_id).execute()
    pet = PetModel.get(PetModel.id == pet_id)
    return pet

@pet_router.delete("/pets/{pet_id}")
def delete_pet(pet_id: int):
    try:
        pet = PetModel.get(PetModel.id == pet_id)
        if pet:
            pet.delete_instance()
            return {"message": "Pet deleted successfully"}
        else:
            raise PetModel.DoesNotExist(status_code=404, detail="Pet not found")
    except PetModel.DoesNotExist:
        return "Pet not found"

