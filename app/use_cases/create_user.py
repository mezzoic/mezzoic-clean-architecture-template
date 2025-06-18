#from uuid import uuid4, UUID
from app.domain.user import User
from app.interfaces.repositories.user_repository import IUserRepository

class CreateUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, newUser: User) -> User:
        # Validate input        
        if not newUser.id == 0:
            raise ValueError("Id must be 0 for a new user")
        # Save the user to the repository
        self.user_repository.add(newUser)
        return newUser

