from sqlalchemy import text
from sqlalchemy.engine import Engine
from app.domain.user import User
from app.interfaces.repositories.user_repository import IUserRepository

class UserRepository(IUserRepository):
    def __init__(self, engine: Engine):
        self.engine = engine

    def add(self, user: User) -> User:
        with self.engine.connect() as connection:
            result = connection.execute(
                text("""
                     INSERT INTO Person (FullName, Email) VALUES ( :name, :email)
                     SELECT SCOPE_IDENTITY() AS Id
                     """),
                { "name": user.name, "email": user.email}
            )
            user.set_identity(result.scalar())
            return user

    def get_by_id(self, user_id: int) -> User:
        with self.engine.connect() as connection:
            result = connection.execute(
                text("SELECT Id, Fullname, Email FROM Person WHERE id = :id"),
                {"id": user_id}
            ).fetchone()
            if result:
                return User(id=result[0], name=result[1], email=result[2])
            else:
                raise ValueError(f"User with id {user_id} not found")
            
    def get_by_email(self, email: str) -> User:
        with self.engine.connect() as connection:
            result = connection.execute(
                text("SELECT Id, FullName, Email FROM Person WHERE email = :email"),
                {"email": email}
            ).fetchone()
            if result:
                return User(id=result[0], name=result[1], email=result[2])
            else:
                raise ValueError(f"User with email {email} not found")

