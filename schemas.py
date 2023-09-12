from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(..., example="John Doe")


class User(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., example="John Doe")

    class Config:
        orm_mode = True