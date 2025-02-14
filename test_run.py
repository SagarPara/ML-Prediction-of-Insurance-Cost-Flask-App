import requests
import pytest
from predict_insurance import app


#proxy to a live server
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client  # This ensures a clean test client for each test
#    return app.test_client

def test_home(client):
    resp = client.get("/")
    print(resp)
    assert resp.status_code == 200

def test_submit(client):
    test_home = {"age": 25, "diabetes": 0, "bp": 0, "transplants": 0, "disease": 0, "height": 150, "weight": 50, "allergy": 0,
                 "cancer": 0, "surgery": 0}  # Example payload
    resp = client.post("/submit", json=test_home)
    assert resp.status_code == 200

    
