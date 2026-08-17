from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


# Tupla: opciones estables del menú principal.
OPCIONES_MENU: tuple[str, ...] = (
    "Registrar producto",
    "Buscar producto",
    "Actualizar producto",
    "Eliminar producto",
    "Listar productos",
    "Registrar usuario",
    "Listar usuarios",
    "Mostrar categorías",
    "Salir"
)


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")

    for numero, opcion in enumerate(OPCIONES_MENU, start=1):
        print(f"{numero}. {opcion}")

    print("========================================")


def leer_precio() -> float:
    while True:
        try:
            precio = float(input("Ingrese el precio: $"))

            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                return precio

        except ValueError:
            print("Ingrese un valor numérico válido.")


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    if not codigo:
        print("El código no puede estar vacío.")
        return

    if restaurante.buscar_producto(codigo) is not None:
        print("Ya existe un producto con ese código.")
        return

    nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría: ").strip()

    if not nombre or not categoria:
        print("El nombre y la categoría son obligatorios.")
        return

    precio = leer_precio()

    producto = Producto(
        codigo=codigo,
        nombre=nombre,
        categoria=categoria,
        precio=precio
    )

    if restaurante.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print("No se pudo registrar el producto.")


def buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- BUSCAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is not None:
        print("\nProducto encontrado:")
        print(producto)
    else:
        print("No se encontró un producto con ese código.")


def actualizar_producto(restaurante: Restaurante) -> None:
    print("\n--- ACTUALIZAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("No se encontró un producto con ese código.")
        return

    print(f"Producto actual: {producto}")

    nombre = input("Ingrese el nuevo nombre: ").strip()
    categoria = input("Ingrese la nueva categoría: ").strip()
    precio = leer_precio()

    actualizado = restaurante.actualizar_producto(
        codigo,
        nombre,
        categoria,
        precio
    )

    if actualizado:
        print("Producto actualizado correctamente.")
    else:
        print("No se pudo actualizar el producto.")


def eliminar_producto(restaurante: Restaurante) -> None:
    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("No se encontró un producto con ese código.")
        return

    print(f"Producto encontrado: {producto}")

    confirmacion = input(
        "¿Está seguro de eliminarlo? (s/n): "
    ).strip().lower()

    if confirmacion == "s":
        if restaurante.eliminar_producto(codigo):
            print("Producto eliminado correctamente.")
        else:
            print("No se pudo eliminar el producto.")
    else:
        print("Operación cancelada.")


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- LISTA DE PRODUCTOS ---")

    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos registrados.")
        return

    for producto in productos:
        print(producto)


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- REGISTRAR USUARIO ---")

    identificacion = input(
        "Ingrese la identificación: "
    ).strip()

    if not identificacion:
        print("La identificación no puede estar vacía.")
        return

    if restaurante.buscar_usuario(identificacion) is not None:
        print("Ya existe un usuario con esa identificación.")
        return

    nombre = input("Ingrese el nombre: ").strip()
    correo = input("Ingrese el correo: ").strip()

    if not nombre or not correo:
        print("El nombre y el correo son obligatorios.")
        return

    usuario = Usuario(
        identificacion=identificacion,
        nombre=nombre,
        correo=correo
    )

    if restaurante.registrar_usuario(usuario):
        print("Usuario registrado correctamente.")
    else:
        print("No se pudo registrar el usuario.")


def listar_usuarios(restaurante: Restaurante) -> None:
    print("\n--- LISTA DE USUARIOS ---")

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No existen usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario)


def mostrar_categorias(restaurante: Restaurante) -> None:
    print("\n--- CATEGORÍAS DE PRODUCTOS ---")

    categorias = restaurante.obtener_categorias()

    if not categorias:
        print("No existen categorías registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")


def main() -> None:
    restaurante = Restaurante()

    # Diccionario: relaciona cada opción con la función que debe ejecutarse.
    acciones = {
        1: registrar_producto,
        2: buscar_producto,
        3: actualizar_producto,
        4: eliminar_producto,
        5: listar_productos,
        6: registrar_usuario,
        7: listar_usuarios,
        8: mostrar_categorias
    }

    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 9:
                print("\nGracias por utilizar el sistema de restaurante.")
                break

            accion = acciones.get(opcion)

            if accion is not None:
                accion(restaurante)
            else:
                print("Opción no válida. Seleccione una opción del 1 al 9.")

        except ValueError:
            print("Debe ingresar un número válido.")


if __name__ == "__main__":
    main()