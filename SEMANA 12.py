class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        # Atributos inmutables
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', isbn='{self.isbn}')"

class Usuario:
    def __init__(self, nombre: str, id_usuario: str):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', id_usuario='{self.id_usuario}', libros_prestados={self.libros_prestados})"

class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros por ISBN
        self.usuarios = set()  # Conjunto para almacenar IDs de usuarios únicos

    def añadir_libro(self, libro: Libro):
        """Añadir un libro a la biblioteca."""
        self.libros[libro.isbn] = libro
        print(f"Libro añadido: {libro}")

    def quitar_libro(self, isbn: str):
        """Quitar un libro de la biblioteca por ISBN."""
        if isbn in self.libros:
            removed_book = self.libros.pop(isbn)
            print(f"Libro quitado: {removed_book}")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario: Usuario):
        """Registrar un nuevo usuario en la biblioteca."""
        if usuario.id_usuario not in {u.id_usuario for u in self.usuarios}:
            self.usuarios.add(usuario)
            print(f"Usuario registrado: {usuario}")
        else:
            print("El ID de usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario: str):
        """Dar de baja a un usuario."""
        self.usuarios = {u for u in self.usuarios if u.id_usuario != id_usuario}
        print(f"Usuario con ID {id_usuario} dado de baja.")

    def prestar_libro(self, isbn: str, id_usuario: str):
        """Prestar un libro a un usuario."""
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

        if libro and usuario:
            usuario.libros_prestados.append(libro)
            print(f"Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("El libro o el usuario no existen.")

    def devolver_libro(self, isbn: str, id_usuario: str):
        """Devolver un libro prestado por un usuario."""
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

        if usuario and any(libro.isbn == isbn for libro in usuario.libros_prestados):
            usuario.libros_prestados = [libro for libro in usuario.libros_prestados if libro.isbn != isbn]
            print(f"Libro devuelto: {isbn} por {usuario.nombre}")
        else:
            print("El libro no está prestado a este usuario.")

    def buscar_libro(self, criterio: str):
        """Buscar libros por título, autor o categoría."""
        resultados = [libro for libro in self.libros.values() if
                      criterio.lower() in libro.titulo.lower() or
                      criterio.lower() in libro.autor.lower() or
                      criterio.lower() in libro.categoria.lower()]
        return resultados

    def listar_libros_prestados(self, id_usuario: str):
        """Listar todos los libros prestados a un usuario."""
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            return usuario.libros_prestados
        else:
            print("El usuario no existe.")


# Ejemplo de uso del sistema
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "978-3-16-148410-0")
    libro2 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela", "978-3-16-148411-7")
    libro3 = Libro("1984", "George Orwell", "Distopía", "978-0-452-28423-4")

    # Añadir libros a la biblioteca
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    # Registrar usuarios
    usuario1 = Usuario("Damini Desai", "U001")
    usuario2 = Usuario("Shrusti Desai", "U002")

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("978-3-16-148410-0", "U001")
    biblioteca.prestar_libro("978-0-452-28423-4", "U002")

    # Listar libros prestados
    print("Libros prestados a Damini Desai:", biblioteca.listar_libros_prestados("U001"))
    print("Libros prestados a Shrusti Desai:", biblioteca.listar_libros_prestados("U002"))

    # Devolver un libro
    biblioteca.devolver_libro("978-3-16-148410-0", "U001")

    # Buscar libros
    print("Buscar libros por 'García':", biblioteca.buscar_libro("García"))

    # Quitar un libro
    biblioteca.quitar_libro("978-3-16-148411-7")