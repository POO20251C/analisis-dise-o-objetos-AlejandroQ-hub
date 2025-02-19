from datetime import date

class Libro:
    def __init__(self, titulo: str, isbn: str, anio_publicacion: int):
        self.titulo = titulo
        self.isbn = isbn
        self.anio_publicacion = anio_publicacion
        self.disponible = True

    def __str__(self):
        return f"{self.titulo} (ISBN: {self.isbn}, Año: {self.anio_publicacion})"


class Lector:
    def __init__(self, nombre: str, numero_socio: int, fecha_registro: date):
        self.nombre = nombre
        self.numero_socio = numero_socio
        self.fecha_registro = fecha_registro

    def __str__(self):
        return f"{self.nombre} (Socio No.: {self.numero_socio})"


class Prestamo:
    def __init__(self, libro: Libro, lector: Lector, fecha_prestamo: date):
        if not libro.disponible:
            raise ValueError("El libro ya está prestado.")
        
        self.libro = libro
        self.lector = lector
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None
        libro.disponible = False

    def devolver_libro(self):
        self.fecha_devolucion = date.today()
        self.libro.disponible = True

    def __str__(self):
        estado = "Devuelto" if self.fecha_devolucion else "En préstamo"
        return f"{self.libro.titulo} prestado a {self.lector.nombre} el {self.fecha_prestamo} ({estado})"


# Entrada de datos
libro_titulo = input("Ingrese el título del libro: ")
libro_isbn = input("Ingrese el ISBN del libro: ")
libro_anio = int(input("Ingrese el año de publicación del libro: "))

lector_nombre = input("Ingrese el nombre del lector: ")
lector_numero = int(input("Ingrese el número de socio del lector: "))
lector_fecha_registro = date.today()

libro = Libro(libro_titulo, libro_isbn, libro_anio)
lector = Lector(lector_nombre, lector_numero, lector_fecha_registro)

prestamo = Prestamo(libro, lector, date.today())
print(prestamo)

# Opción de devolución
devolver = input("¿Desea devolver el libro? (s/n): ")
if devolver.lower() == 's':
    prestamo.devolver_libro()
    print(prestamo)
