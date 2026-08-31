from app.database import SessionLocal
from app.models import Producto, ItemPedido, Pedido

def seed():
    db = SessionLocal()
    try:
        # Limpiar datos anteriores para evitar conflictos de claves foráneas
        db.query(ItemPedido).delete()
        db.query(Pedido).delete()
        db.query(Producto).delete()
        db.commit()

        # Nuevos productos solicitados en 3 cuotas
        productos = [
            Producto(nombre="Hamburguesa", precio_final=9500.0, cuotas_cantidad=3, cuotas_valor=round(9500.0/3, 2), garantia_meses=0, stock=15),
            Producto(nombre="Esponja", precio_final=12500.0, cuotas_cantidad=3, cuotas_valor=round(12500.0/3, 2), garantia_meses=0, stock=15),
            Producto(nombre="Huevo", precio_final=6000.0, cuotas_cantidad=3, cuotas_valor=round(6000.0/3, 2), garantia_meses=0, stock=15),
            Producto(nombre="Vela", precio_final=9000.0, cuotas_cantidad=3, cuotas_valor=round(9000.0/3, 2), garantia_meses=0, stock=15),
            Producto(nombre="Tomate", precio_final=11000.0, cuotas_cantidad=3, cuotas_valor=round(11000.0/3, 2), garantia_meses=0, stock=15)
        ]
        
        db.add_all(productos)
        db.commit()
        print("Productos actualizados correctamente.")
    except Exception as e:
        print("Error:", e)
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed()
