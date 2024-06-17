class ClimaDiario:
    def __init__(self, dia, temperatura):
        self._dia = dia
        self._temperatura = temperatura

    @property
    def dia(self):
        return self._dia

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, nueva_temperatura):
        self._temperatura = nueva_temperatura

    def __str__(self):
        return f"Día {self._dia}: {self._temperatura}°C"


class ClimaSemanal:
    def __init__(self):
        self._dias = []

    def agregar_clima_diario(self, clima_diario):
        if isinstance(clima_diario, ClimaDiario):
            self._dias.append(clima_diario)
        else:
            raise TypeError("Debe ser una instancia de ClimaDiario")

    def calcular_promedio_semanal(self):
        total_temperaturas = sum(dia.temperatura for dia in self._dias)
        return total_temperaturas / len(self._dias)

    def mostrar_informacion_semanal(self):
        for dia in self._dias:
            print(dia)


# Programa principal
def main():
    print("Registro de temperaturas semanales")
    clima_semanal = ClimaSemanal()

    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        clima_diario = ClimaDiario(dia=i + 1, temperatura=temp)
        clima_semanal.agregar_clima_diario(clima_diario)

    clima_semanal.mostrar_informacion_semanal()
    promedio = clima_semanal.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")


if __name__ == "__main__":
    main()
