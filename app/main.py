from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas

from app.database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from typing import List, Optional
from app.services import productos as productos_service

@app.get("/productos", response_model=List[schemas.ProductoOut])
def obtener_productos(skip: int = 0, limit: int = 100, nombre: Optional[str] = None, precio_max: Optional[float] = None, db: Session = Depends(get_db)):
    return productos_service.listar_productos(db=db, skip=skip, limit=limit, nombre=nombre, precio_max=precio_max)

@app.post("/productos", response_model=schemas.ProductoOut)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return productos_service.crear_producto(db=db, producto=producto)