from sqlalchemy.orm import Session
from app import models, schemas
from typing import Optional

def crear_producto(db: Session, producto: schemas.ProductoCreate):
    nuevo_producto = models.Producto(**producto.model_dump())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

def listar_productos(db: Session, skip: int = 0, limit: int = 100, nombre: Optional[str] = None, precio_max: Optional[float] = None):
    query = db.query(models.Producto)
    
    if nombre:
        query = query.filter(models.Producto.nombre.ilike(f"%{nombre}%"))
    if precio_max is not None:
        query = query.filter(models.Producto.precio_final <= precio_max)
        
    return query.offset(skip).limit(limit).all()
