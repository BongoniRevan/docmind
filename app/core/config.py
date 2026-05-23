from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "DocMind"
    gemini_api_key: str = ""
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    embedding_model: str = "all-MiniLM-L6-v2"
    gemini_model: str = "gemini-1.5-flash"
    top_k: int = 5
    chunk_size: int = 512
    chunk_overlap: int = 50

    class Config:
        env_file = ".env"

settings = Settings()
