from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel

router = APIRouter()

class QueryRequest(BaseModel):
    question: str
    top_k: int = 5

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]

@router.post("/ingest")
async def ingest_document(file: UploadFile = File(...)):
    return {"message": f"File {file.filename} received", "status": "pending"}

@router.post("/query", response_model=QueryResponse)
async def query_document(request: QueryRequest):
    return QueryResponse(
        answer="RAG pipeline not yet connected",
        sources=[]
    )

@router.get("/documents")
async def list_documents():
    return {"documents": []}
