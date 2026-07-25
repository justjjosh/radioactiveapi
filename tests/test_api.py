from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

#api layer tests
def test_isotopes_endpoint():
    response = client.get("/isotopes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_decay_endpoint():
    # Assuming isotope_id 1 exists in the database
    request_data = {
        "isotope_id": 1,
        "initial_quantity": 100.0,
        "elapsed_time_seconds": 20.0
    }
    response = client.post("/decay", json=request_data)
    assert response.status_code == 200
    data = response.json()
    assert "isotope_name" in data
    assert "initial_quantity" in data
    assert "remaining_quantity" in data
    assert "elapsed_time_seconds" in data

def test_decay_not_found():
    # Assuming isotope_id 999 does not exist in the database
    request_data = {
        "isotope_id": 999,
        "initial_quantity": 100.0,
        "elapsed_time_seconds": 20.0
    }
    response = client.post("/decay", json=request_data)
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Isotope not found"

def test_decay_curve_endpoint():
    #Assumimg isotope_id 1 exists in the database
    params = {
        "initial_quantity": 100.0,
        "duration_seconds": 50.0,
        "n_points": 100
    }
    response = client.get("/isotopes/1/decay-curve", params=params)
    assert response.status_code == 200
    data = response.json()
    assert "isotope" in data
    assert "time_points" in data
    assert "remaining_quantities" in data
