from fastapi import APIRouter, Body
from ..models.user import User

user_router = APIRouter()

@user_router.get("/users")
def get_users():
  
    return "users"

@user_router.get("/users/{user_id}")
def get_user(user_id: int):
   
    return "User"
    

@user_router.post("/users")
def create_user(user: User = Body(...)):
    return user

    
@user_router.put("/users/{user_id}")
def update_user(user_id: int, user_data: dict):
    return "User updated"

@user_router.delete("/users/{user_id}")
def delete_user(user_id: int):

   return "User deleted"
