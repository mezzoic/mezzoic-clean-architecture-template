from typing import Optional
from pydantic import BaseModel, field_validator, model_validator
from app.domain.entity import Entity

class User( Entity, BaseModel):
    id: Optional[int] = None
    name: Optional[str]
    email: str
        
    @field_validator("name", mode='before')
    @classmethod
    def none_to_empty_string(cls, value):
        return value or ''    
    
    @model_validator(mode="after")
    def validate_email(self) -> "User":
        if "@" not in self.email:
            raise ValueError("Invalid email address")
        return self