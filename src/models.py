from sqlmodel import SQLModel, Field
from typing import List, Optional, Dict
from pydantic import EmailStr, HttpUrl, validator
from datetime import datetime

class Profile(SQLModel, table=True):
    id:str = Field(...,primary_key=True)
    username:str = Field(...)
    email:str = Field(..., index=True)
    colors:Optional[Dict[str,str]] = Field()
    image:str = Field()
    description:str = Field()
    updated_at:datetime = datetime.utcnow()