from app.database import SessionLocal, engine, Base
from app.models import Producto

# Create tables just in case
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Check if there are any products
if db.query(Producto).count() == 0:
    print("Database is empty. Adding dummy products...")
    productos = [
        Producto(nombre="Laptop Gamer", precio_final=1200.50, cuotas_cantidad=12, cuotas_valor=100.04, garantia_meses=24, stock=10),
        Producto(nombre="Monitor 144hz", precio_final=300.00, cuotas_cantidad=6, cuotas_valor=50.00, garantia_meses=12, stock=5),
        Producto(nombre="Teclado Mecánico", precio_final=80.00, cuotas_cantidad=3, cuotas_valor=26.66, garantia_meses=6, stock=20),
        Producto(nombre="Mouse Inalámbrico", precio_final=45.00, cuotas_cantidad=1, cuotas_valor=45.00, garantia_meses=12, stock=15)
    ]
    db.add_all(productos)
    db.commit()
    print("Products added successfully!")
else:
    print("Database already has products.")

db.close()
