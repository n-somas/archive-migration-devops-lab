import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# DATABASE_URL wird später über Docker Compose gesetzt.
# Wenn keine Umgebungsvariable vorhanden ist, wird lokal SQLite genutzt.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./archive_migration.db")


# SQLite benötigt connect_args, PostgreSQL nicht.
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(DATABASE_URL)


# SessionLocal erzeugt Datenbank-Sessions für einzelne API-Anfragen.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base ist die Grundlage für alle SQLAlchemy-Modelle.
Base = declarative_base()


# Dependency für FastAPI.
# Öffnet eine Datenbankverbindung und schließt sie nach der Anfrage wieder.
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
