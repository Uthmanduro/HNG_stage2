from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str = Field(..., example="John Doe")


class User(BaseModel):
    name: str = Field(..., example="John Doe")

    class Config:
        orm_mode = True