from fastapi.testclient import TestClient
from app.main import app

# TestClient simuliert HTTP-Anfragen an unsere FastAPI-App,
# ohne dass wir den Server manuell starten müssen.
client = TestClient(app)


# Dieser Test prüft, ob der Healthcheck-Endpunkt funktioniert.
def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    