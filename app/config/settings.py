# settings.py
from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str = "dev"
    DEBUG: bool = True
    IS_PROD: bool = False

    DB_SERVER: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"mssql+pyodbc://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_SERVER}/{self.DB_NAME}"
            "?driver=ODBC+Driver+18+for+SQL+Server"
        )

    class Config:
        # Point explicitly to the .env next to this settings.py
        env_file = str(Path(__file__).resolve().parent / ".env")
        env_file_encoding = "utf-8"

# instantiate once
settings = Settings() # type: ignore

def get_settings() -> Settings:
    """
    Returns the singleton instance of Settings.
    This is useful for dependency injection in FastAPI.
    """
    return settings

if __name__ == "__main__":
    # a quick debug dump
    print("Working dir:", Path().resolve())
    print(".env loaded from:", Settings.Config.env_file)
    print("Exists?", Path(Settings.Config.env_file).exists())
    print("Loaded values:", settings.model_dump())
