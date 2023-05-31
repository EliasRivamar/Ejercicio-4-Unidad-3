from Empleados import Empleados
from EmpleadoPlanta import Planta
from EmpleadoContratado import Contratado
from EmpleadosExternos import Externos
import csv
import numpy as np

class ManejadorEmpleados:
    __cantidad = 0
    __dimension: int
    __incremento = 5

    def __init__(self, dimension, incremento=5):
        self.__empleados = np.empty(dimension, dtype = Empleados)
        self.__cantidad = 0
        self.__dimension = dimension

    def cargarEmpleados(self):
        self.cargarPlanta()
        self.cargarExternos()
        self.cargarContratados()

    def agregarEmpleado(self, unEmpleado):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__empleados.resize(self.__dimension, refcheck=False)
        self.__empleados[self.__cantidad] = unEmpleado
        self.__cantidad += 1
    
    def cargarPlanta(self):
        archivo = open("planta.csv")
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            nombre = fila[0]
            dni = fila[1]
            direccion = fila[2]
            telefono = fila[3]
            sueldo_basico  = fila[4]
            antiguedad = fila[5]
            unEmpleado = Planta(nombre, dni, direccion, telefono, sueldo_basico, antiguedad)
            self.agregarEmpleado(unEmpleado)
        archivo.close()
    
    def cargarExternos(self):
        archivo = open("externos.csv")
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            nombre = fila[0]
            dni = fila[1]
            direccion = fila[2]
            telefono = fila[3]
            tarea = fila[4]
            fecha_inicio = fila[5]
            fecha_finalizacion = fila[6]
            monto_viatico = fila[7]
            costo_obra = fila[8]
            monto_seguro = fila[9]
            unEmpleado = Externos(nombre, dni, direccion, telefono, tarea, fecha_inicio, fecha_finalizacion, monto_viatico, costo_obra, monto_seguro)
            self.agregarEmpleado(unEmpleado)
        archivo.close()

    def cargarContratados(self):
        archivo = open("contratados.csv")
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            nombre = fila[0]
            dni = fila[1]
            direccion = fila[2]
            telefono = fila[3]
            inicio = fila[4]
            finalizacion = fila[5]
            horas_trabajadas = fila[6]
            valor_horas = fila[7]
            unEmpleado = Contratado(nombre, dni, direccion, telefono, inicio, finalizacion, horas_trabajadas, valor_horas)
            self.agregarEmpleado(unEmpleado)
        archivo.close()

    def mostrarEmpleados(self):
        indice = 0
        print(Empleados.mostrarDatos(self.__empleados[indice]))
        print("LISTA DE LOS EMPLEADOS DE LA PLANTA: ")
        while indice < len(self.__empleados):
            if isinstance(self.__empleados[indice], Planta):
                print("EMPLEADO PLANTA: ")
                Planta.mostrarDatos(self.__empleados[indice])
            elif isinstance(self.__empleados[indice], Externos):
                print("EMPLEADO EXTERNO: ")
                Externos.mostrarDatos(self.__empleados[indice])
            elif isinstance(self.__empleados[indice], Contratado):
                print("EMPLEADO CONTRATADO: ")
                Contratado.mostrarDatos(self.__empleados[indice])
            indice += 1

    def buscarDni(self, dni, hora):
        indice = 0
        bandera = False
        while bandera == False and indice < len(self.__empleados):
            print(Empleados.getDni(self.__empleados[indice]))
            if int(Empleados.getDni(self.__empleados[indice])) == int(dni):
                print("Se encontro")
                horas = int(input("Ingrese la nueva cantidad de Horas: "))
                if isinstance(self.__empleados[indice], Contratado):
                    Contratado.modificarHora(self.__empleados[indice], horas)
                    bandera = True
            indice += 1

    def buscarTarea(self, tarea):
        indice = 0
        total = 0
        while indice < len(self.__empleados):
            if isinstance(self.__empleados[indice], Externos):
                if str(tarea) in str(Externos.getTarea(self.__empleados[indice])):
                    print(f"INICIAL: {Externos.getFechaInicial(self.__empleados[indice]) }, FINAL: {Externos.getFechaFinal(self.__empleados[indice])}")
                    if Externos.getFechaInicial(self.__empleados[indice]) < Externos.getFechaFinal(self.__empleados[indice]):
                        total += int(Externos.getMonto(self.__empleados[indice]))
                    else:
                        print("El contrato expiro")
            indice += 1
        print(f"El Total a pagar es: {total}")

    def ayudaEconomica(self):
        indice = 0
        while indice < len(self.__empleados):
            if isinstance(self.__empleados[indice], Planta):
                if 150000 > Planta.sueldo(self.__empleados[indice]):
                    Planta.mostrarInfo(self.__empleados[indice])
            elif isinstance(self.__empleados[indice], Externos):
                if 150000 > Externos.sueldo(self.__empleados[indice]):
                    Externos.mostrarInfo(self.__empleados[indice])
            elif isinstance(self.__empleados[indice], Contratado):
                if 150000 > Contratado.sueldo(self.__empleados[indice]):
                    Contratado.mostrarInfo(self.__empleados[indice])
            indice += 1

    def mostrarSalario(self):
        indice = 0
        while indice < len(self.__empleados):
            if isinstance(self.__empleados[indice],Planta):
                Planta.mostrarSalario(self.__empleados[indice])
            elif isinstance(self.__empleados[indice], Externos):
                Externos.mostrarSalario(self.__empleados[indice])
            elif isinstance(self.__empleados[indice], Contratado):
                Contratado.mostrarSalario(self.__empleados[indice])
            indice += 1

