from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_health_check():
    """
    Prueba que la API responde en la ruta raíz con su mensaje de estado.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API funcionando correctamente", "status": "online"}


def test_get_products():
    """
    Prueba que el endpoint de productos devuelve una lista.
    """
    # IMPORTANTE: Cambia "/productos" por la ruta real que configuraste en tu main.py
    # Si usaste prefix="/api/productos", pon "/api/productos" aquí.
    response = client.get("/productos")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

    if len(data) > 0:
        primer_producto = data[0]
        assert "id" in primer_producto
        assert "name" in primer_producto
        assert "precio" in primer_producto