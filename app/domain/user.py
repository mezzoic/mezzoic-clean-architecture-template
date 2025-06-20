from typing import Optional
from pydantic import BaseModel, validator
from app.domain.entity import Entity


class User(Entity, BaseModel):
    id: Optional[int] = None
    name: Optional[str]
    email: str

    @validator("name", pre=True, always=True)
    def none_to_empty_string(cls, value):
        return value or ""

    @validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        return value
