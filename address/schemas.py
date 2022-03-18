from pydantic import BaseModel
from typing import List, Optional
    


class AddressBase(BaseModel):
    title : str
    latitude : float
    longitude : float
    city : str
    state : str
    country : str

class Address(AddressBase):
    class Config():
        orm_mode = True
    
class User(BaseModel):
    name:str
    email:str
    password:str
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    name:str
    email:str
    addresses : List[Address] =[]
    class Config():
        orm_mode = True


class ShowAddress(AddressBase):
    owner: User

    class Config():
        orm_mode = True