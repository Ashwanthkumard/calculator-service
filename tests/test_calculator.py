from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add():
    response = client.get("/calculator/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {"operation": "add", "result": 5}

def test_subtract():
    response = client.get("/calculator/subtract?a=5&b=2")
    assert response.status_code == 200
    assert response.json() == {"operation": "subtract", "result": 3}

def test_multiply():
    response = client.get("/calculator/multiply?a=4&b=3")
    assert response.status_code == 200
    assert response.json() == {"operation": "multiply", "result": 12}

def test_divide():
    response = client.get("/calculator/divide?a=10&b=2")
    assert response.status_code == 200
    assert response.json() == {"operation": "divide", "result": 5}

def test_divide_by_zero():
    response = client.get("/calculator/divide?a=10&b=0")
    assert response.status_code == 400
    assert response.json()["detail"] == "Division by zero"
