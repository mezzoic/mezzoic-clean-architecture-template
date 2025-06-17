from dataclasses import dataclass, field
from uuid import uuid4, UUID

@dataclass(frozen=True)
class User:
    id: int
    name: str
    email: str

    def __post_init__(self):
        if "@" not in self.email:
            raise ValueError(f"Invalid email address: {self.email}")
        