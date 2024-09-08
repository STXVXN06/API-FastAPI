from fastapi import APIRouter, Body
from models.user import User
from database import UserModel

user_router = APIRouter()

@user_router.get("/users")
def get_users():
    user = UserModel.select().where(UserModel.id > 0).dicts()
    return list(user)

@user_router.get("/users/{user_id}")
def get_user(user_id: int):
    try:
        user = UserModel.get(UserModel.id == user_id)
        return user
    except UserModel.DoesNotExist:
        return "User not Found"
    

@user_router.post("/users")
def create_user(user: User = Body(...)):
    UserModel.create(username=user.username, email=user.email, password=user.password)
    return user

    
@user_router.put("/users/{user_id}")
def update_user(user_id: int, user_data: dict):
    UserModel.update(**user_data).where(UserModel.id == user_id).execute()
    user = UserModel.get(UserModel.id == user_id)
    return user

@user_router.delete("/users/{user_id}")
def delete_user(user_id: int):
    try:
        user = UserModel.get(UserModel.id == user_id)
        if user:
            user.delete_instance() 
            return {"message": "User deleted successfully"}
        else:
            raise UserModel.DoesNotExist(status_code=404, detail="User not found")
    except UserModel.DoesNotExist:
        return "User not Found"
