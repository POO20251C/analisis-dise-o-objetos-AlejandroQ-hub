from datetime import date

class Habitacion:
    def __init__(self, numero: int, tipo: str, tarifa: float):
        self.numero = numero
        self.tipo = tipo  # Puede ser 'individual', 'doble', 'suite'
        self.tarifa = tarifa
        self.disponible = True  # Estado de la habitación

    def __str__(self):
        return f"Habitación {self.numero} ({self.tipo}) - Tarifa: ${self.tarifa} por noche"


class Huesped:
    def __init__(self, nombre: str, identificacion: str, fecha_registro: date):
        self.nombre = nombre
        self.identificacion = identificacion  # Número único de identificación
        self.fecha_registro = fecha_registro

    def __str__(self):
        return f"Huésped: {self.nombre} - ID: {self.identificacion}"


class Reserva:
    def __init__(self, habitacion: Habitacion, huesped: Huesped, fecha_inicio: date, fecha_fin: date):
        self.habitacion = habitacion
        self.huesped = huesped
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.completada = False  # Estado de la reserva

        # Marcar la habitación como no disponible
        habitacion.disponible = False

    def completar_reserva(self):
        self.completada = True
        self.habitacion.disponible = True  # Liberar la habitación

    def __str__(self):
        estado = "Completada" if self.completada else "Activa"
        return (f"Reserva de {self.huesped.nombre} en Habitación {self.habitacion.numero} "
                f"del {self.fecha_inicio} al {self.fecha_fin} - Estado: {estado}")

# Entrada de datos
print("Ingrese los datos de la habitación:")
numero_habitacion = int(input("Número de habitación: "))
tipo_habitacion = input("Tipo de habitación (individual/doble/suite): ")
tarifa_habitacion = float(input("Tarifa por noche: "))
habitacion1 = Habitacion(numero_habitacion, tipo_habitacion, tarifa_habitacion)

print("\nIngrese los datos del huésped:")
nombre_huesped = input("Nombre del huésped: ")
identificacion_huesped = input("Número de identificación: ")
año_registro = int(input("Año de registro: "))
mes_registro = int(input("Mes de registro: "))
dia_registro = int(input("Día de registro: "))
huesped1 = Huesped(nombre_huesped, identificacion_huesped, date(año_registro, mes_registro, dia_registro))

print("\nIngrese los datos de la reserva:")
año_inicio = int(input("Año de inicio de la reserva: "))
mes_inicio = int(input("Mes de inicio de la reserva: "))
dia_inicio = int(input("Día de inicio de la reserva: "))

año_fin = int(input("Año de fin de la reserva: "))
mes_fin = int(input("Mes de fin de la reserva: "))
dia_fin = int(input("Día de fin de la reserva: "))

reserva1 = Reserva(habitacion1, huesped1, date(año_inicio, mes_inicio, dia_inicio), date(año_fin, mes_fin, dia_fin))

print("\nEstado actual de la reserva:")
print(reserva1)  # Muestra los datos de la reserva

# Preguntar si se desea completar la reserva
completar = input("\n¿Desea completar la reserva? (sí/no): ").strip().lower()
if completar == "sí":
    reserva1.completar_reserva()
    print("\nEstado de la reserva después de completarla:")
    print(reserva1)  # Ahora la reserva está completada
