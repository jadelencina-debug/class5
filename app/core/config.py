from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Tienda API"
    DATABASE_URL: str
    CORS_ORIGINS: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def origins(self) -> list[str]:
        """Divide CORS_ORIGINS por comas y devuelve una lista limpia."""
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]


settings = Settings()
