class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    # Métodos para obtener y establecer atributos
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio
class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print(f"El producto con ID {producto.get_id()} ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print(f"Producto {producto.get_nombre()} agregado al inventario.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print(f"Producto con ID {id} eliminado del inventario.")
        else:
            print(f"Producto con ID {id} no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id].set_precio(precio)
            print(f"Producto con ID {id} actualizado.")
        else:
            print(f"Producto con ID {id} no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [str(producto) for producto in self.productos.values() if producto.get_nombre() == nombre]
        if resultados:
            print("Resultados de búsqueda:")
            for resultado in resultados:
                print(resultado)
        else:
            print(f"No se encontraron productos con el nombre {nombre}.")

    def mostrar_todos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")
import json

class Inventario:
    # Resto del código

    def guardar_en_archivo(self, filename):
        with open(filename, 'w') as file:
            json.dump({id: vars(prod) for id, prod in self.productos.items()}, file)
        print(f"Inventario guardado en {filename}.")

    def cargar_desde_archivo(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for id, atributos in data.items():
                    self.productos[id] = Producto(**atributos)
            print(f"Inventario cargado desde {filename}.")
        except FileNotFoundError:
            print(f"El archivo {filename} no existe.")


def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario en archivo")
    print("7. Cargar inventario desde archivo")
    print("8. Salir")


def main():
    inventario = Inventario()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            filename = input("Nombre del archivo para guardar: ")
            inventario.guardar_en_archivo(filename)

        elif opcion == "7":
            filename = input("Nombre del archivo para cargar: ")
            inventario.cargar_desde_archivo(filename)

        elif opcion == "8":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()
