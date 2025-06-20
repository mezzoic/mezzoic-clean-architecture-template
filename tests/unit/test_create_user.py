import pathlib
import sys
import pytest

# Allow tests to import the application package without installing it
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from app.domain.user import User
from app.use_cases.create_user import CreateUser
from app.interfaces.repositories.user_repository import IUserRepository


class FakeRepo(IUserRepository):
    def __init__(self):
        self.users = {}
        self._next_id = 1

    def add(self, user: User) -> User:
        user_id = self._next_id
        self._next_id += 1
        user.id = user_id
        self.users[user_id] = user
        return user

    def get_by_id(self, user_id: int) -> User:
        return self.users[user_id]

    def get_by_email(self, email: str) -> User:
        for u in self.users.values():
            if u.email == email:
                return u
        raise KeyError(email)


def test_create_user_accepts_none_id():
    repo = FakeRepo()
    use_case = CreateUser(repo)
    user = User(name="Test", email="test@example.com")
    created = use_case.execute(user)
    assert created.id == 1
    assert repo.users[1].email == "test@example.com"


def test_create_user_rejects_existing_id():
    repo = FakeRepo()
    use_case = CreateUser(repo)
    user = User(id=42, name="Test", email="test@example.com")
    with pytest.raises(ValueError):
        use_case.execute(user)
