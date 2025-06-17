#from uuid import uuid4, UUID
from app.domain.user import User
from app.interfaces.repositories.user_repository import IUserRepository

class GetUserById:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, id: int) -> User:
        # Validate input
        if not id :
            raise ValueError("Id is required")

        # Create a new user instance
        user = self.user_repository.get_by_id(id)

        if not user:
            raise ValueError(f"User with id {id} not found")

        return user

