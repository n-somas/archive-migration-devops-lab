from sqlalchemy import Column, Integer, String

from app.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(String, unique=True, index=True, nullable=False)
    source_system = Column(String, nullable=False)
    target_system = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    status = Column(String, nullable=False, default="pending")
