from fastapi.testclient import TestClient
from scripts.api import app


client = TestClient(app)


def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ALPR app"}


def test_recognize():
    response = client.post(
        "/recognize",
        files={"file": (
            "filename", open('example_img/example_1.jpg', "rb"), "image/jpeg")}
    )
    assert response.text == '["B088BB 88"]'
