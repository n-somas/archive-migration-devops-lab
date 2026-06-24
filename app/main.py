from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import Base, engine, get_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Archive Migration DevOps Lab",
    description="Small DevOps lab for archive migration, Docker and database basics.",
    version="0.2.0",
    lifespan=lifespan
)


@app.get("/")
def read_root():
    return {
        "message": "Archive Migration DevOps Lab is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.get("/documents", response_model=list[schemas.DocumentResponse])
def get_documents(db: Session = Depends(get_db)):
    return crud.get_documents(db)


@app.post("/documents", response_model=schemas.DocumentResponse)
def create_document(
    document: schemas.DocumentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_document(db, document)
