from pydantic import BaseModel
from typing import List
class User(BaseModel):
    name: str
    villageName:str
    role:str
    villageId:int
    phone:int
    galli_name: List[str]