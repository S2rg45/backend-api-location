


from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_product():
    response = client.post("/api/product/", 
                            json={
                                    "name": "Product 1",
                                    "description": "Description 1",
                                    "price": 1000,
                                    "stock": True
                            })
    assert response.status_code == 200
    assert response.json() == {"result": "Product created successfully"}


def test_create_product_error():
    response = client.post("/api/product/", 
                            json={
                                    "name": "Product 1",
                                    "description": "Description 1",
                                    "price": 1000,
                                    "stock": "True"
                            })
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid stock"}


def test_get_product():
    response = client.get("/api/product/")
    assert response.status_code == 200
    assert response.json() == {"result": "Product information"}


def test_get_product_error():
    response = client.get("/api/product/")
    assert response.status_code == 400
    assert response.json() == {"message": "Product not found"}


def test_delete_product():
    response = client.delete("/api/product/",
                            json={
                                    "id": ""
                            })

    assert response.status_code == 200
    assert response.json() == {"result": "Product deleted successfully"}


def test_update_product():
    response = client.put("/api/product/", 
                            json={
                                    "id": "",
                                    "name": "Product 1",
                                    "description": "Description 1",
                                    "price": 1000,
                                    "stock": True
                            })
    assert response.status_code == 200
    assert response.json() == {"result": "Product updated successfully"}