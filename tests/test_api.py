import pytest
from fastapi.testclient import TestClient
from app.main import app  # Adjust this to match your app structure

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the MLOps application"}

def test_prediction_endpoint():
    payload = {"feature1": 25, "feature2": 75}
    response = client.post("/predict", json=payload)
    
    # Print the response to verify its structure (optional)
    print(response.json())
    
    # Assert response contains the "prediction" key
    assert response.status_code == 200
    assert "prediction" in response.json()
    
    # Optional: Assert the prediction is a numeric value (int or float)
    prediction_value = response.json()["prediction"]
    assert isinstance(prediction_value, (int, float)), f"Prediction is not numeric: {prediction_value}"