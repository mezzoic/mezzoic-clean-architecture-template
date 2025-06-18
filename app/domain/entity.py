from abc import ABC
from typing import Any, Optional

class Entity(ABC):
    id: Optional[int] = None

    def set_identity(self, value: Any) -> None:
        if value is None:
            raise ValueError("Identity value cannot be None")
        self.id = int(value)