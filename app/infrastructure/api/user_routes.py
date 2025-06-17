import logging
from fastapi import APIRouter, HTTPException
from app.interfaces.controllers.iuser_controller import IUserController
from app.use_cases.get_user import GetUserById
from app.use_cases.create_user import CreateUser
from app.interfaces.repositories.user_repository import IUserRepository
from app.domain.user import User


logger = logging.getLogger(__name__)
STD_ERROR = "Internal Server Error"

class UserRouter(IUserController):
    _app = APIRouter()
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def add(self,user: User) -> User:
        """
        Create a new user.
        """
        try:
            use_case = CreateUser(user_repository=self.user_repository)
            return use_case.execute(name=user.name, email=user.email)
        except Exception:
            logger.error(f"Error creating user {user.email}:", exc_info=True)
            raise HTTPException(status_code=500, detail=STD_ERROR)
            
    def get_by_id(self, user_id: int) -> User:
        """
        Get a user by ID.
        """
        if not user_id:
            raise HTTPException(status_code=400, detail="User ID is required")
        if user_id <= 0:
            raise HTTPException(status_code=400, detail="User ID must be a positive integer")
        try:
            user_id = int(user_id)
            use_case = GetUserById(user_repository= self.user_repository)
            return use_case.execute(user_id)
        except Exception:
            logger.error(f"Error retrieving user with ID {user_id}", exc_info=True)
            raise HTTPException(status_code=500, detail=STD_ERROR)
    
    def _register_routes(self):
        @self._app.get("/users/{user_id}", response_model=User)
        def route_get_user(user_id: int):
            return self.get_by_id(user_id)
        @self._app.post("/users", response_model=User)
        def route_create_user(user: User):
            return self.add(user)