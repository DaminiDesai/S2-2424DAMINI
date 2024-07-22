import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        '2': 'Unidad 2/2.1. Programacion Orientada a Objetos/2.1-1. Ejemplo POO.py',
        '3': 'Unidad 3/3.2. Bases de Datos/3.2-1. Ejemplo Bases de Datos.py',
        '4': 'Unidad 4/4.1. Desarrollo Web/4.1-1. Ejemplo Desarrollo Web.py',
        '5': 'Unidad 5/5.3. Analisis de Datos/5.3-1. Ejemplo Analisis de Datos.py',
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def generar_reporte():
    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Generar el reporte
    reporte = f"Reporte generado el {fecha_actual}\n\n"
    reporte += "Proyectos en desarrollo:\n"
    reporte += "- Proyecto A\n"
    reporte += "- Proyecto B\n"
    reporte += "- Proyecto C\n\n"
    reporte += "Tareas pendientes:\n"
    reporte += "- Tarea 1\n"
    reporte += "- Tarea 2\n"
    reporte += "- Tarea 3\n"

    # Guardar el reporte en un archivo
    with open('reporte.txt', 'w') as archivo:
        archivo.write(reporte)

    print("Reporte generado y guardado en 'reporte.txt'.")

# Ejecutar el dashboard
if __name__ == "__main__":
    while True:
        print("\nBienvenido al Dashboard de Gestión de Proyectos")
        print("Selecciona una opción:")
        print("1. Ver código de scripts")
        print("2. Generar reporte")
        print("0. Salir")

        eleccion = input("Ingresa el número de opción: ")

        if eleccion == '0':
            print("Saliendo del Dashboard...")
            break
        elif eleccion == '1':
            mostrar_menu()
        elif eleccion == '2':
            generar_reporte()
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")