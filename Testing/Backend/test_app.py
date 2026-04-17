from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Flask API is running" in response.data

def test_add_positive():
    client = app.test_client()
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json["result"] == 5

def test_add_negative():
    client = app.test_client()
    response = client.get("/add?a=-2&b=-3")
    assert response.json["result"] == -5

def test_add_invalid():
    client = app.test_client()
    response = client.get("/add?a=abc&b=3")
    assert response.status_code == 400