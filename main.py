from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1. Corregir importaciones: Asegúrate de apuntar a la ruta correcta
from app.api import products  # Verifica que la ruta sea app.api.routes o app.api
from app.db.basedate import engine, Base

# 2. Creación de tablas (Útil para desarrollo)
# creación de tabla de productos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Inventario Pro",
    description="Gestión integral de productos mediante FastAPI y SQLAlchemy",
    version="1.0.0"
)

# 3. Configuración de CORS (Ajustada para mayor claridad)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, cambia "*" por tu dominio real
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Inclusión de Routers (Modularidad)
# Corregido: Usamos el router que importamos arriba
app.include_router(
    products.router,
    prefix="/api/v1/productos", 
    tags=["Productos"]
)

@app.get("/", tags=["Health Check"])
def read_root():
    return {"status": "online", "message": "API funcionando correctamente"}