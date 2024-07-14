class Archivo:
    def __init__(self, nombre_archivo):
        """
        Constructor de la clase Archivo.
        Inicializa el objeto y abre el archivo en modo lectura.

        :param nombre_archivo: Nombre del archivo a abrir
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = None
        try:
            self.archivo = open(self.nombre_archivo, 'r')
            print(f"Archivo '{self.nombre_archivo}' abierto correctamente.")
        except IOError:
            print(f"No se pudo abrir el archivo '{self.nombre_archivo}'.")

    def leer_contenido(self):
        """
        Lee y retorna el contenido del archivo si está abierto.

        :return: Contenido del archivo o un mensaje de error
        """
        if self.archivo:
            return self.archivo.read()
        else:
            return "El archivo no está abierto."

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Cierra el archivo si está abierto.
        """
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")


class ConexionBaseDeDatos:
    def __init__(self, nombre_bd):
        """
        Constructor de la clase ConexionBaseDeDatos.
        Inicializa el objeto y simula la apertura de una conexión a la base de datos.

        :param nombre_bd: Nombre de la base de datos a conectar
        """
        self.nombre_bd = nombre_bd
        self.conexion = None
        self.abrir_conexion()

    def abrir_conexion(self):
        """
        Simula la apertura de una conexión a la base de datos.
        """
        self.conexion = f"Conexión a la base de datos '{self.nombre_bd}'"
        print(f"Conexión a la base de datos '{self.nombre_bd}' abierta correctamente.")

    def ejecutar_query(self, query):
        """
        Simula la ejecución de una consulta en la base de datos.

        :param query: Consulta SQL a ejecutar
        :return: Resultado simulado de la consulta
        """
        if self.conexion:
            return f"Ejecutando query: {query} en {self.conexion}"
        else:
            return "No hay conexión a la base de datos."

    def __del__(self):
        """
        Destructor de la clase ConexionBaseDeDatos.
        Simula el cierre de la conexión a la base de datos.
        """
        if self.conexion:
            print(f"Conexión a la base de datos '{self.nombre_bd}' cerrada correctamente.")
            self.conexion = None


# Uso de las clases

# Crear y usar la clase Archivo
archivo = Archivo('ejemplo.txt')
print(archivo.leer_contenido())

# Crear y usar la clase ConexionBaseDeDatos
conexion_bd = ConexionBaseDeDatos('mi_base_de_datos')
print(conexion_bd.ejecutar_query('SELECT * FROM usuarios'))

# Los destructores se llamarán automáticamente cuando los objetos se eliminen
# o cuando el programa termine de ejecutarse.
