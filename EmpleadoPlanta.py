from Empleados import Empleados
import math

class Planta(Empleados):
    __sueldo_basico: int
    __antiguedad: int

    def __init__(self, nombre, dni, direccion, telefono,  sueldo_basico, antiguedad):
        super().__init__(nombre, dni, direccion, telefono)
        self.__sueldo_basico =sueldo_basico
        self.__antiguedad = antiguedad

    def sueldo(self):
        sueldo = int(self.__sueldo_basico)+int(self.__sueldo_basico)*int(self.__antiguedad)
        return sueldo
    
    def mostrarDatos(self):
        super().mostrarDatos()
        print("Datos Empleados Planta")
        print(f"Sueldo Basico: {self.__sueldo_basico}, Antiguedad: {self.__antiguedad}")

    def mostrarInfo(self):
        print("-----Empleado Planta----")
        super().mostrarInfo()
    
    def mostrarSalario(self):
         super().info()
         sueldo = self.sueldo()
         print(f"Sueldo: {sueldo}")
