# PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# Cálculo del promedio semanal del clima

class ClimaSemanal:
    """
    Clase que maneja las temperaturas semanales
    """

    def __init__(self):
        # Atributo privado (encapsulamiento)
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas diarias
        """
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método para calcular el promedio semanal
        """
        return sum(self.__temperaturas) / len(self.__temperaturas)


def main():
    print("Promedio semanal del clima - Programación Orientada a Objetos")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal es: {promedio:.2f} °C")


# Ejecutar el programa
main()
