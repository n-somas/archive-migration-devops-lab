from fastapi import FastAPI

# Erstellt die FastAPI-Anwendung.
# Diese App simuliert später eine kleine Dokument-Migrationsplattform.
app = FastAPI(
    title="Archive Migration DevOps Lab",
    description="Small DevOps lab for document migration, Docker, database and CI/CD basics.",
    version="0.1.0"
)


# Startseite der API.
# Damit prüfen wir schnell, ob die Anwendung grundsätzlich erreichbar ist.
@app.get("/")
def read_root():
    return {
        "message": "Archive Migration DevOps Lab is running"
    }


# Healthcheck-Endpunkt.
# Solche Endpunkte werden im Betrieb genutzt, um zu prüfen, ob ein Dienst lebt.
@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


# Einfacher Beispiel-Endpunkt.
# Später ersetzen wir diese statischen Daten durch Daten aus PostgreSQL.
@app.get("/documents")
def get_documents():
    return [
        {
            "document_id": "DOC-1001",
            "source_system": "old_archive",
            "target_system": "new_archive",
            "file_name": "invoice_2024_001.pdf",
            "status": "pending"
        },
        {
            "document_id": "DOC-1002",
            "source_system": "old_archive",
            "target_system": "new_archive",
            "file_name": "contract_2024_002.pdf",
            "status": "success"
        }
    ]