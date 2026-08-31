from app.database import SessionLocal
from app.models import Usuario, Producto, Pedido, ItemPedido

def test_db():
    db = SessionLocal()
    try:
        # Crear un usuario de prueba
        usuario = db.query(Usuario).filter(Usuario.email == "juan@example.com").first()
        if not usuario:
            usuario = Usuario(nombre="Juan Perez", email="juan@example.com", password_hash="1234")
            db.add(usuario)
            db.commit()
            db.refresh(usuario)
            print(f"EXITO: Usuario creado: {usuario.nombre} (ID: {usuario.id})")
        else:
            print(f"EXITO: Usuario existente utilizado: {usuario.nombre} (ID: {usuario.id})")

        # Obtener un producto existente (o crear uno si no hay)
        producto = db.query(Producto).first()
        if not producto:
            producto = Producto(nombre="Producto Test", precio_final=100.0, cuotas_cantidad=1, cuotas_valor=100.0, garantia_meses=12, stock=10)
            db.add(producto)
            db.commit()
            db.refresh(producto)
            print(f"EXITO: Producto creado: {producto.nombre} (ID: {producto.id})")
        else:
            print(f"EXITO: Producto existente utilizado: {producto.nombre} (ID: {producto.id})")

        # Crear un pedido para el usuario
        pedido = Pedido(usuario_id=usuario.id, total=producto.precio_final * 2)
        db.add(pedido)
        db.commit()
        db.refresh(pedido)
        print(f"EXITO: Pedido creado: ID {pedido.id}, Total: ${pedido.total}")

        # Crear un ítem de pedido
        item = ItemPedido(pedido_id=pedido.id, producto_id=producto.id, cantidad=2, precio_unitario=producto.precio_final)
        db.add(item)
        db.commit()
        db.refresh(item)
        print(f"EXITO: Ítem de pedido creado: {item.cantidad}x {producto.nombre} en Pedido {pedido.id}")

        print("\n¡Todas las inserciones relacionadas funcionaron correctamente! Las Foreign Keys y Modelos son validos.")

    except Exception as e:
        print("ERROR al probar la base de datos:", e)
    finally:
        db.close()

if __name__ == "__main__":
    test_db()
