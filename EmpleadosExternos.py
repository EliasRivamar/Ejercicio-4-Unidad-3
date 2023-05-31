from Empleados import Empleados

class Externos(Empleados):
    __tarea: str
    __fecha_inicio: int
    __fecha_finalizacion: int
    __monto_viatico: int
    __costo_obra: int
    __monto_seguro: int

    def __init__(self,nombre, dni, direccion, telefono, tarea, fecha_inicio, fecha_finalizacion, monto_viatico, costo_obra, monto_seguro):
        super().__init__(nombre, dni, direccion, telefono)
        self.__tarea = tarea
        self.__fecha_inicio = fecha_inicio
        self.__fecha_finalizacion = fecha_finalizacion
        self.__monto_viatico = monto_viatico
        self.__costo_obra = costo_obra
        self.__monto_seguro = monto_seguro

    def getTarea(self):
        return self.__tarea
    
    def getFechaInicial(self):
        return self.__fecha_inicio
    
    def getFechaFinal(self):
        return self.__fecha_finalizacion
    
    def getMonto(self):
        return self.__monto_viatico

    def sueldo(self):
        sueldo = int(self.__monto_viatico) - int(self.__monto_seguro) + int(self.__costo_obra)
        return sueldo
    
    def mostrarInfo(self):
        print("-----Empleado Externo-----")
        super().mostrarInfo()

    def mostrarSalario(self):
         super().info()
         sueldo = self.sueldo()
         print(f"Sueldo: {sueldo}")

    def mostrarDatos(self):
        super().mostrarDatos()
        print("Datos Empleado Externo:")
        print(f"Tarea: {self.__tarea}, Fecha de Inicio. {self.__fecha_inicio}, Fecha de Finalizacion: {self.__fecha_finalizacion}, Monto Viatico: {self.__monto_viatico}, Costo de la Obra: {self.__costo_obra}. Monto Seguro: {self.__monto_seguro}")
