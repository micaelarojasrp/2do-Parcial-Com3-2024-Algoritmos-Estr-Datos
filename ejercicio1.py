#EJERCICIO 1
from datetime import datetime, timedelta

class FECHA:
    def __init__(self, dia, mes, año):
        self.fecha = datetime(año, mes, dia)

    def calcular_dif_fecha(self, otra_fecha):
        if not isinstance(otra_fecha, FECHA):
            raise TypeError("El argumento debe ser una instancia de la clase FECHA")
        return abs((self.fecha - otra_fecha.fecha).days)

    def __str__(self):
        return self.fecha.strftime("%d/%m/%Y")

    def __add__(self, dias):
        if not isinstance(dias, int):
            raise TypeError("El argumento debe ser un entero")
        nueva_fecha = self.fecha + timedelta(days=dias)
        return FECHA(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)

    def __eq__(self, otra_fecha):
        if not isinstance(otra_fecha, FECHA):
            return False
        return self.fecha==otra_fecha.fecha


fecha1 = FECHA(15, 6, 2024)
fecha2 = FECHA(26, 6, 2024)

print("Primer fecha", fecha1)  
print("Segunda fecha", fecha2) 
print("Diferencia en días:", fecha1.calcular_dif_fecha(fecha2)
print("Fecha 1 + 10 días:", fecha1 + 10) 
print("Fechas iguales:", fecha1 == fecha2)

#EJERCICIO 2

class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": datetime.strptime(fecha_ingreso, "%d/%m/%Y"),
            "Carrera": carrera
        }

    def cambiar_datos(self, **nuevos_datos):
        for key, value in nuevos_datos.items():
            if key in self.datos:
                if key == "FechaIngreso":
                    self.datos[key] = datetime.strptime(value, "%d/%m/%Y")
                else:
                    self.datos[key] = value
            else:
                raise KeyError(f"El dato '{key}' no es valido para actualizar.")

    def antiguedad(self):
        return (datetime.now() - self.datos["FechaIngreso"]).days // 365

    def __str__(self):
        return f"Nombre: {self.datos['Nombre']}, DNI: {self.datos['DNI']}, Fecha de Ingreso: {self.datos['FechaIngreso'].strftime('%d/%m/%Y')}, Carrera: {self.datos['Carrera']}"

    def __eq__(self, otro_alumno):
        if not isinstance(otro_alumno, Alumno):
            return False
        return self.datos["DNI"] == otro_alumno.datos["DNI"]


alumno1 = Alumno("Juan Perez", 41365678, "15/03/2020", "Ingenieria")
alumno2 = Alumno("Ana Gomez", 32654321, "20/02/2019", "Medicina")

#EJERCICIO 3
import random

class Nodo:
    def __init__(self, alumno=None):
        self.alumno = alumno
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_al_inicio(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def agregar_al_final(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.cola is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def lista_ejemplo(self, cantidad_alumnos):
        for _ in range(cantidad_alumnos):
            nombre = f"Alumno_{random.randint(1000, 9999)}"
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = datetime.today() - timedelta(days=random.randint(0, 365*5))
            carrera = random.choice(["Ingeniería", "Medicina", "Derecho", "Arquitectura"])
            alumno = Alumno(nombre, dni, fecha_ingreso.strftime("%d/%m/%Y"), carrera)
            self.agregar_al_final(alumno)

    def __iter__(self):
        self.nodo_actual = self.cabeza
        return self

    def __next__(self):
        if self.nodo_actual is None:
            raise StopIteration
        else:
            alumno = self.nodo_actual.alumno
            self.nodo_actual = self.nodo_actual.siguiente
            return alumno
    def intercambiar_nodos(self, nodo1, nodo2): #ejercicio 4
        temp = nodo1.alumno
        nodo1.alumno = nodo2.alumno
        nodo2.alumno = temp

     def ordenar_por_fecha_ingreso(self):
        if self.cabeza is None or self.cabeza.siguiente is None:
            return
        
        actual = self.cabeza
        while actual.siguiente is not None:
            siguiente = actual.siguiente
            while siguiente is not None:
                if actual.alumno.fecha_ingreso > siguiente.alumno.fecha_ingreso:
                    self.intercambiar_nodos(actual, siguiente)
                siguiente = siguiente.siguiente
            actual = actual.siguiente
    def _str_(self):
        if self.cabeza is None:
            return "Lista vacía"
        actual = self.cabeza
        lista_str = ""
        while actual is not None:
            lista_str += str(actual.alumno) + "\n"
            actual = actual.siguiente
        return lista_str.strip()

# Iterar
print("Lista de Alumnos:")
for alumno in lista_alumnos:
    print(alumno)

lista_alumnos = ListaDoblementeEnlazada()
lista_alumnos.lista_ejemplo(5)
#lista desordenada
print("Lista de Alumnos (Desordenada):")
print(lista_alumnos)
# Ordenarpor fecha de ingreso
lista_alumnos.ordenar_por_fecha_ingreso()
#ista ordenada
print("\nLista de Alumnos (Ordenada por Fecha de Ingreso):")
print(lista_alumnos)

#EJERCICIO 5
# Función para escribir la lista de alumnos en un archivo
def escribir_lista_alumnos_en_archivo(lista_alumnos, archivo):
    with open(archivo, 'w') as f:
        for alumno in lista_alumnos:
            f.write(str(alumno) + '\n')

#Directorio para el archivo
directorio_actual = os.getcwd()
nombre_directorio = "directorio_alumnos"
ruta_directorio = os.path.join(directorio_actual, nombre_directorio)
os.makedirs(ruta_directorio, exist_ok=True)

archivo_alumnos = os.path.join(ruta_directorio, "alumnos.txt")
escribir_lista_alumnos_en_archivo(lista_alumnos, archivo_alumnos)

nueva_ruta_directorio = os.path.join(directorio_actual, "nueva_ruta", nombre_directorio)
os.rename(ruta_directorio, nueva_ruta_directorio)
ruta_directorio = nueva_ruta_directorio

os.remove(archivo_alumnos)
os.rmdir(ruta_directorio)

print("Operacion realizada con éxito.")
