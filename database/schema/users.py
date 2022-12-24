from pydantic import BaseModel

class User(BaseModel):
    name: str
    description: str=None
    age: int
    pay: float
    tax: float=0