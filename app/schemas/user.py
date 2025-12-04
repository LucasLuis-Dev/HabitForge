from pydantic import BaseModel, EmailStr, constr
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: constr(min_length=6, max_length=72)

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # antes chamava orm_mode
