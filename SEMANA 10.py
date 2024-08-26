import os
class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()
    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario."""
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w') as f:
                pass  # Crea el archivo si no existe
            print("El archivo de inventario no existía, se ha creado uno nuevo.")
            return

        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    nombre, cantidad = linea.strip().split(',')
                    self.productos[nombre] = int(cantidad)
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("Error: El archivo no se encontró.")
        except PermissionError:
            print("Error: No se tienen permisos para acceder al archivo.")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo de inventario."""
        try:
            with open(self.archivo, 'w') as f:
                for nombre, cantidad in self.productos.items():
                    f.write(f"{nombre},{cantidad}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad):
        """Agrega un producto al inventario."""
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad
        self.guardar_inventario()
        print(f"Producto '{nombre}' agregado/actualizado exitosamente.")

    def actualizar_producto(self, nombre, cantidad):
        """Actualiza la cantidad de un producto en el inventario."""
        if nombre in self.productos:
            self.productos[nombre] = cantidad
            self.guardar_inventario()
            print(f"Producto '{nombre}' actualizado exitosamente.")
        else:
            print(f"Error: El producto '{nombre}' no existe en el inventario.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"Producto '{nombre}' eliminado exitosamente.")
        else:
            print(f"Error: El producto '{nombre}' no existe en el inventario.")

    def main():
        inventario = Inventario()

        while True:
            print("\nOpciones:")
            print("1. Agregar producto")
            print("2. Actualizar producto")
            print("3. Eliminar producto")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                inventario.agregar_producto(nombre, cantidad)
            elif opcion == '2':
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Nueva cantidad: "))
                inventario.actualizar_producto(nombre, cantidad)
            elif opcion == '3':
                nombre = input("Nombre del producto a eliminar: ")
                inventario.eliminar_producto(nombre)
            elif opcion == '4':
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    if __name__ == "__main__":
        main()
