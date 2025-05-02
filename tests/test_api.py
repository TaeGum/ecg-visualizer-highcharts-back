from fastapi.testclient import TestClient
from app.main import app  # FastAPI 앱이 정의된 모듈 경로에 맞게 수정

client = TestClient(app)

def test_get_ecg():
    response = client.get("/api/ecg?lead=II&start=0&end=1")
    assert response.status_code == 200
    json_data = response.json()
    assert "lead" in json_data
    assert json_data["lead"] == "II"
    assert "data" in json_data
    assert isinstance(json_data["data"], list)
