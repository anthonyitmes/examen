from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API funcionando correctamente", "status": "online"}


def test_get_products():


    response = client.get("/api/v1/productos")

    assert response.status_code == 200, f"Error: La API devolvió {response.status_code}"

    data = response.json()
    assert isinstance(data, list), "La respuesta debería ser una lista"

    if len(data) > 0:
        primer_producto = data[0]
        assert "id" in primer_producto
        assert "name" in primer_producto
        assert "precio" in primer_producto