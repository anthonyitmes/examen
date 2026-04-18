from fastapi.testclient import TestClient

# IMPORTANTE: Aquí debes importar la variable 'app' de tu archivo principal.
# Si tu archivo donde definiste `app = FastAPI()` se llama main.py, esto está perfecto.
from main import app

# Iniciamos el cliente de pruebas
client = TestClient(app)

def test_get_products():
    """
    Prueba que el endpoint principal responde con un código 200 (OK)
    y devuelve una lista de productos con la estructura correcta.
    """
    # 1. Ejecutar la petición
    # Nota: Si tu router en main.py tiene un prefijo como '/api' o '/productos',
    # asegúrate de poner la ruta completa aquí (ej. client.get("/productos/"))
    response = client.get("/")

    # 2. Verificar que la petición fue exitosa
    assert response.status_code == 200, f"Error: La API devolvió {response.status_code}"

    # 3. Convertir la respuesta a JSON (diccionario/lista de Python)
    data = response.json()

    # 4. Verificar que la respuesta es una lista
    # (Ya que tu endpoint usa response_model=List[ProductResponse])
    assert isinstance(data, list), "La respuesta debería ser una lista"

    # 5. Si hay datos en la base de datos, verificamos que los campos Pydantic estén ahí
    if len(data) > 0:
        primer_producto = data[0]
        # Gracias a la herencia que hicimos en ProductResponse,
        # estos campos DEBEN existir en el JSON.
        assert "id" in primer_producto
        assert "name" in primer_producto
        assert "precio" in primer_producto
        # Comprobamos que el precio sea mayor a cero, tal como validamos en Pydantic
        assert primer_producto["precio"] > 0