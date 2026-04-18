from sqlalchemy import Column, Integer, String, DateTime, NUMERIC
from sqlalchemy.sql import func
from app.db.basedate import Base


class Producto(Base):
    __tablename__ = "productos"
    #tabla de productos # productos
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    precio = Column(NUMERIC(100), nullable=False)

    # SQLAlchemy se encarga de las fechas automáticamente
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # mejoras