import os
from pydantic import BaseModel


class Settings(BaseModel):
    OPEN_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
    TOGETHER_API_KEY: str | None = os.getenv("TOGETHER_API_KEY")
    HUGGINGFACE_API_KEY: str | None = os.getenv("HUGGINGFACE_API_KEY")

Settings = Settings()