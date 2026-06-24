from sqlalchemy.orm import Session

from app import models, schemas


def get_documents(db: Session):
    return db.query(models.Document).all()


def create_document(db: Session, document: schemas.DocumentCreate):
    db_document = models.Document(
        document_id=document.document_id,
        source_system=document.source_system,
        target_system=document.target_system,
        file_name=document.file_name,
        status=document.status
    )

    db.add(db_document)
    db.commit()
    db.refresh(db_document)

    return db_document
