from celery import Celery
from celery.result import AsyncResult
from time import sleep
import math

# Configuración de Celery
task_name='geolocation_task'
broker_url = 'redis://redis:6379/2'
backend_url = 'mongodb+srv://root-location:9ccYP1yHw0pwzgzB@cluster-location.gejme.mongodb.net/locations?retryWrites=true&w=majority&tls=true&tlsAllowInvalidCertificates=true'

celery_app = Celery(
    task_name,
    broker=broker_url,
    backend=backend_url,
    include=['celery_adapter']
)

# Configura las opciones adicionales de Celery
celery_app.conf.update(
    result_extended=True,
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True
)


@celery_app.task(name='geolocation_task.test_task')
def test_task(p, q):
    px, py = math.radians(float(p['x'])), math.radians(float(p['y']))
    qx, qy = math.radians(float(q['x'])), math.radians(float(q['y']))
    delta_lat = px - qx
    delta_lon = py - qy

    # Fórmula de Haversine
    a = math.sin(delta_lat / 2) ** 2 + math.cos(px) * math.cos(py) * math.sin(delta_lon / 2) ** 2
    a = min(max(a, 0), 1)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 6371  # Radio de la Tierra en kilómetros
    distance = R * c
    # distance = math.sqrt((px - qx) ** 2 + (py - qy) ** 2)
    # print(f"Distancia calculada entre {p} y {q}: {distance}")
    return distance


def run_test_task(p,q):
    """Ejecuta la tarea test_task de forma asíncrona."""
    print(f"Ejecutando tarea... task")
    task = test_task.delay(p,q)
    print("Tarea enviada con ID:", task.id)
    return task.id


def get_task_result(task_id):
    """Recupera el resultado de una tarea usando su ID."""
    result = AsyncResult(task_id, app=celery_app)
    return {
        "result": result.result,
        "state": result.state
    }


