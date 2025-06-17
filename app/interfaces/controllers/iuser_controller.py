from abc import ABC, abstractmethod
from app.domain.user import User

class IUserController(ABC):
    @abstractmethod
    def add(self, user: User) -> User:
        ...
    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        ...
