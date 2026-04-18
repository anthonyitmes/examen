from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.basedate import get_db
# Asumiendo que estos son tus esquemas actualizados
from app.schemas.registro import ProductBase, ProductResponse, ProductUpdate
from app.models.modeloproducto import Producto

router = APIRouter()


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_in: ProductBase, db: Session = Depends(get_db)):
    """
    Crea un nuevo producto. 
    Se cambió 'ProductResponse' por 'ProductBase' en la entrada para no pedir el ID.
    """
    # 1. Verificar si el producto ya existe (por nombre o SKU si tuvieras)
    existente = db.query(Producto).filter(Producto.name == product_in.name).first()
    if existente:
        raise HTTPException(
            status_code=400,
            detail="Ya existe un producto con este nombre"
        )

    # 2. Crear instancia del modelo ORM
    # Usamos **product_in.dict() para pasar todos los parámetros automáticamente
    nuevo_producto = Producto(**product_in.dict())

    # 3. Guardar en BD
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto


@router.get("/", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    """
    Retorna la lista de productos con paginación básica.
    """
    productos = db.query(Producto).all()
    return productos



@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db)):
    """
    Actualiza un producto existente de forma parcial.
    """
    db_producto = db.query(Producto).filter(Producto.id == product_id).first()
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")


    db.commit()
    db.refresh(db_producto)
    return db_producto


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Elimina un producto de la base de datos.
    """
    producto = db.query(Producto).filter(Producto.id == product_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    db.delete(producto)
    db.commit()
    return None  # Al usar 204 No Content no se devuelve cuerpo