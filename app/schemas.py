from pydantic import BaseModel, ConfigDict


class DocumentBase(BaseModel):
    document_id: str
    source_system: str
    target_system: str
    file_name: str
    status: str = "pending"


class DocumentCreate(DocumentBase):
    pass


class DocumentResponse(DocumentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
