from Empleados import Empleados

class Contratado(Empleados):
    __inicio: str
    __finalizacion: str
    __horas_trabajadas: int
    __valor_hora: int

    def mostrarSalario(self):
         super().info()
         sueldo = self.sueldo()
         print(f"Sueldo: {sueldo}")

    def mostrarInfo(self):
         print("-----Empleado Contratado-----")
         super().mostrarInfo()

    def sueldo(self):
         sueldo = int(self.__horas_trabajadas)*int(self.__valor_hora)
         return sueldo

    def modificarHora(self, hora):
         self.__horas_trabajadas = hora
         print("Se modifico la Hora")
         
    def __init__(self, nombre, dni, direccion, telefono, inicio, finalizacion, horas_trabajadas, valor_hora):
         super().__init__(nombre, dni, direccion, telefono)
         self.__inicio = inicio
         self.__finalizacion = finalizacion
         self.__horas_trabajadas = horas_trabajadas
         self.__valor_hora = valor_hora

    def mostrarDatos(self):
         super().mostrarDatos()
         print("Datos Empleado Contratado")
         print(f"Fecha Inicio: {self.__inicio}, Finalizacion: {self.__finalizacion}, Horas Trabajadas: {self.__horas_trabajadas}, Valor Hora: {self.__valor_hora}")

