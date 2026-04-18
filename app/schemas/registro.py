from pydantic import BaseModel
from datetime import datetime
from typing import Optional

#1. Equema Base: Campos que comparten todos
class ProductBase(BaseModel):
    name: str
    precio: int #balida que tenga un formato de correo @

##El esquema para RESPONDER (Lo que el servidor devuelve)
class ProductResponse(ProductBase):
    id: int
    created_at: Optional[datetime] = None
    update_at: Optional[datetime] = None

#4. Esquema para actualizar: Campos opcionales para actualizar
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    precio: Optional[str] = None


