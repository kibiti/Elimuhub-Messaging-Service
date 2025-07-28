import pytest
from src.handlers.whatsapp_webhook import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_admission_inquiry(client):
    data = {
        "message": "I want to know about admission",
        "from": "+254700000000"
    }
    response = client.post('/webhook', json=data)
    assert response.status_code == 200
    assert "Admission template sent" in response.json["response"]
