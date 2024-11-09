import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import AsyncMock

client = TestClient(app)

# Datos de prueba
data = {
    "locations": [
        {"name": "trisl", "latitude": "8.9760567978", "longitude": "5.700796896"},
        {"name": "illkod", "latitude": "1.79477769", "longitude": "3.47776556"},
        {"name": "iollkd", "latitude": "3.6566565477", "longitude": "-5.589098"}
    ]
}

@pytest.fixture
def mock_celery(mocker):
    # Mock de CeleryLocationHandler y su método 'execute'
    mock_handler = mocker.patch("app.main.CeleryLocationHandler", autospec=True)
    mock_handler.return_value.execute = AsyncMock(return_value="mocked-response")
    return mock_handler

@pytest.fixture
def mock_redis(mocker):
    # Mock del cliente Redis (puedes adaptar según tu clase/objeto de Redis)
    mock_redis_client = mocker.patch("app.main.redis_client")
    mock_redis_client.set = mocker.MagicMock(return_value=True)
    return mock_redis_client

@pytest.fixture
def mock_mongo(mocker):
    # Mock del cliente MongoDB
    mock_mongo_client = mocker.patch("app.main.mongo_client")
    mock_mongo_client.db.collection.insert_one = mocker.MagicMock(return_value=True)
    return mock_mongo_client

def test_process_location(mock_celery, mock_redis, mock_mongo):
    response = client.post("/process-location/", json=data)

    # Verifica que el código de estado sea 200
    assert response.status_code == 200

    # Verifica que el contenido de la respuesta tenga 'result' con el valor mockeado
    result = response.json()
    assert result["result"] == "mocked-response"

    # Verifica que el método 'execute' de CeleryLocationHandler fue llamado
    mock_celery.return_value.execute.assert_called_once()

    # Verifica que Redis y MongoDB fueron llamados correctamente
    mock_redis.set.assert_called()
    mock_mongo.db.collection.insert_one.assert_called()