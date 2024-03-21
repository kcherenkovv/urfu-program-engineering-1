from fastapi.testclient import TestClient
from api import app


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

def test_translate():
    response = client.post("/tranlslate/",
                          json={"text":"I love machine learning"})
    assert response.status_code == 200
    assert response.json()["translated_text"] == "Я люблю машинное обучение!"
