#from uuid import uuid4, UUID
from app.domain.user import User
from app.interfaces.repositories.user_repository import IUserRepository

class CreateUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, newUser: User) -> User:
        """Persist a new ``User`` instance in the repository."""

        # Validate input
        # ``User`` instances created by the API typically have ``id`` set to
        # ``None``.  An explicit ``0`` is also allowed for backwards
        # compatibility.  Any other value means the object already exists.
        if newUser.id not in (None, 0):
            raise ValueError("Id must be unset for a new user")

        # Save the user to the repository which will assign the identity
        self.user_repository.add(newUser)
        return newUser

