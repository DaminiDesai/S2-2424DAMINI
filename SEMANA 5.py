"""
Programa para calcular el área de diferentes figuras geométricas.
Autor: [Damini
Fecha: [30/06/2024]

Este programa permite calcular el área de un círculo, un cuadrado o un triángulo.
El usuario puede seleccionar la figura y proporcionar los datos necesarios.
"""


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    PI = 3.14159  # Definición de la constante PI
    area = PI * radio ** 2
    return area


def calcular_area_cuadrado(lado):
    """
    Calcula el área de un cuadrado dado el tamaño de su lado.

    :param lado: Longitud del lado del cuadrado (float)
    :return: Área del cuadrado (float)
    """
    area = lado ** 2
    return area


def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dada su base y altura.

    :param base: Longitud de la base del triángulo (float)
    :param altura: Altura del triángulo (float)
    :return: Área del triángulo (float)
    """
    area = (base * altura) / 2
    return area


def main():
    """
    Función principal del programa. Gestiona la interacción con el usuario.
    """
    print("Calculadora de áreas de figuras geométricas")
    print("1. Círculo")
    print("2. Cuadrado")
    print("3. Triángulo")
    opcion = int(input("Seleccione una figura (1-3): "))

    if opcion == 1:
        radio = float(input("Ingrese el radio del círculo: "))
        area = calcular_area_circulo(radio)
        figura = "círculo"
    elif opcion == 2:
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = calcular_area_cuadrado(lado)
        figura = "cuadrado"
    elif opcion == 3:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        figura = "triángulo"
    else:
        print("Opción no válida")
        return

    print(f"El área del {figura} es: {area}")


if __name__ == "__main__":
    main()
