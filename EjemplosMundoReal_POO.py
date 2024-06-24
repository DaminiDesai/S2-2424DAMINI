class Hotel:
    def __init__(self, nombre, capacidad):
        """
        Constructor de la clase Hotel. Inicializa los atributos del hotel.

        Args:
            nombre (str): El nombre del hotel.
            capacidad (int): La capacidad del hotel.
        """
        self.nombre = nombre
        self.capacidad = capacidad
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        """
        Agrega una habitación al hotel.

        Args:
            habitacion (Habitacion): La habitación a agregar.
        """
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        """
        Muestra las habitaciones del hotel.
        """
        for habitacion in self.habitaciones:
            print(f"Habitación {habitacion.numero}: {habitacion.tipo}")


class Habitacion:
    def __init__(self, numero, tipo):
        """
        Constructor de la clase Habitacion. Inicializa los atributos de la habitación.

        Args:
            numero (int): El número de la habitación.
            tipo (str): El tipo de la habitación (sencilla o doble).
        """
        self.numero = numero
        self.tipo = tipo
        self.reserva = None

    def asignar_reserva(self, reserva):
        """
        Asigna una reserva a la habitación.

        Args:
            reserva (Reserva): La reserva a asignar.
        """
        self.reserva = reserva

    def mostrar_reserva(self):
        """
        Muestra la reserva de la habitación.
        """
        if self.reserva:
            print(f"Habitación {self.numero} - Reserva: {self.reserva.nombre}")
        else:
            print(f"Habitación {self.numero} - Sin reserva")


class Reserva:
    def __init__(self, nombre, fecha_inicio, fecha_fin):
        """
        Constructor de la clase Reserva. Inicializa los atributos de la reserva.

        Args:
            nombre (str): El nombre del huésped.
            fecha_inicio (str): La fecha de inicio de la reserva.
            fecha_fin (str): La fecha de fin de la reserva.
        """
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def __str__(self):
        """
        Representación en cadena de la reserva.

        Returns:
            str: La representación en cadena de la reserva.
        """
        return f"Reserva de {self.nombre} desde {self.fecha_inicio} hasta {self.fecha_fin}"


# Crear un hotel
hotel = Hotel("Hotel El Marino", 100)

# Crear habitaciones
habitacion1 = Habitacion(10, "Doble")
habitacion2 = Habitacion(5, "Sencilla")
habitacion3 = Habitacion(3, "Doble")

# Agregar habitaciones al hotel
hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)
hotel.agregar_habitacion(habitacion3)

# Mostrar habitaciones
hotel.mostrar_habitaciones()

# Crear reservas
reserva1 = Reserva("Damini", "2024-05-15", "2024-05-17")
reserva2 = Reserva("Dayana", "2024-03-20", "2024-03-22")

# Asignar reservas a habitaciones
habitacion1.asignar_reserva(reserva1)
habitacion2.asignar_reserva(reserva2)

# Mostrar reservas
habitacion1.mostrar_reserva()
habitacion2.mostrar_reserva()
"Implementa la clase Hotel, Habitacion y Reserva"