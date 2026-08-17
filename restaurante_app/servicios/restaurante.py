from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    def __init__(self) -> None:
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []

    # -----------------------------
    # OPERACIONES DE PRODUCTOS
    # -----------------------------

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo) is not None:
            return False

        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> bool:
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio

        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)
        return True

    def listar_productos(self) -> list[Producto]:
        return self.productos.copy()

    # -----------------------------
    # OPERACIONES DE USUARIOS
    # -----------------------------

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion) is not None:
            return False

        self.usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios.copy()

    # -----------------------------
    # CONJUNTO DE CATEGORÍAS
    # -----------------------------

    def obtener_categorias(self) -> set[str]:
        categorias: set[str] = set()

        for producto in self.productos:
            categorias.add(producto.categoria)

        return categorias