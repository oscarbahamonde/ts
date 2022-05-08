from pydantic import BaseModel, EmailStr, HttpUrl, validator
from typing import List, Dict, Optional
from enum import Enum

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str

class User(BaseModel):
    id: str
    username: str
    email: EmailStr
    colors: List[str]
    image: Optional[HttpUrl]
    description: Optional[str]
    
