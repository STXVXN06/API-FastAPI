from pydantic import BaseModel

class Pet(BaseModel):
    name: str
    species: str
    age: int
    owner_name: str