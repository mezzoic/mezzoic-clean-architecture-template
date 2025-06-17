#from uuid import uuid4, UUID
from app.domain.user import User
from app.interfaces.repositories.user_repository import IUserRepository

class CreateUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, name: str, email: str) -> User:
        # Validate input
        if not name or not email:
            raise ValueError("Name and email are required")

        # Create a new user instance
        user = User(id=int(), name=name, email=email)

        # Save the user to the repository
        self.user_repository.add(user)

        return user

