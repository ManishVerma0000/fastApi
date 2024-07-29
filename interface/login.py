from pydantic import BaseModel
class Login(BaseModel):
    villageId:int
    phone:str