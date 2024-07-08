# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo encapsulado
        self._edad = edad  # Atributo encapsulado

    # Método para obtener el nombre del animal (getter)
    def get_nombre(self):
        return self._nombre

    # Método para obtener la edad del animal (getter)
    def get_edad(self):
        return self._edad

    # Método para establecer la edad del animal (setter)
    def set_edad(self, edad):
        if edad > 0:
            self._edad = edad
        else:
            print("La edad debe ser un número positivo")

    # Método común para emitir sonido
    def emitir_sonido(self):
        print(f"{self._nombre} hace un sonido.")


# Clase derivada
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.raza = raza

    # Método sobrescrito para emitir sonido
    def emitir_sonido(self):
        print(f"{self._nombre} ladra.")

    # Método adicional específico de la clase Perro
    def mostrar_raza(self):
        print(f"{self._nombre} es un {self.raza}.")


# Crear instancias de las clases y demostrar funcionalidad
if __name__ == "__main__":
    # Crear una instancia de Animal
    animal = Animal("Luna", 4)
    animal.emitir_sonido()  # Genérico hace un sonido.

    # Crear una instancia de Perro
    perro = Perro("Firulais", 3, "Labrador")
    perro.emitir_sonido()  # Firulais ladra.
    perro.mostrar_raza()  # Firulais es un Labrador.

    # Utilizando encapsulación
    print(f"Nombre del animal: {animal.get_nombre()}")
    print(f"Edad del animal: {animal.get_edad()}")

    # Cambiando la edad usando el setter
    animal.set_edad(6)
    print(f"Edad del animal actualizada: {animal.get_edad()}")

    # Intentar establecer una edad negativa
    animal.set_edad(-1)  # La edad debe ser un número positivo
