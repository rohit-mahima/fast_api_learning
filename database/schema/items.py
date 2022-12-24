from pydantic import BaseModel
from pydantic import Field, HttpUrl
from typing import List, Union

class Image(BaseModel):
    url:HttpUrl
    name:str

class Items(BaseModel):
    name: str = Field(title="name of the item",default="name of the item", min_length=5)
    description: str = None
    price:float
    gst:float=None
    tags:List[str]=[]
    image:Image
