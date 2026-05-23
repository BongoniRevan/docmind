from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="RAG engine for document question answering (Gemini powered)",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "DocMind is running", "status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}
