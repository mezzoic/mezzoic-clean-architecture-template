# src/app/interfaces/repositories/user_repository.py
from abc import ABC, abstractmethod
from app.domain.user import User

class IUserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> User:
        ...
    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        ...
    @abstractmethod
    def get_by_email(self, email: str) -> User:
        ...
