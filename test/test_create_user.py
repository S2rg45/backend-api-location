

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user():
    response = client.post("/api/register/", 
                            json={
                                    "username": "Juan",
                                    "email": "juan@hotmail.com",
                                    "password": "123456"
                            })
    assert response.status_code == 200
    assert response.json() == {"result": "User created successfully"}


def test_create_user_error():
    response = client.post("/api/register/", 
                            json={
                                    "username": "Juan",
                                    "email": "djfkdjfk",
                                    "password": "123456"
                            })
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid email"}

def test_create_user_error2():
    response = client.post("/api/register/", 
                            json={
                                    "username": "Juan",
                                    "email": "  ",
                                    "password": "123456"    
                            })
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid email"}

