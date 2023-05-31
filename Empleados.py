class Empleados(object):
    __nombre: str
    __dni: int
    __direccion: str
    __telefono: int

    def __init__(self, nombre, dni, direccion, telefono):
        self.__nombre = nombre
        self.__dni = dni
        self.__direccion = direccion
        self.__telefono = telefono
    
    def getDni(self):
        return self.__dni
    
    def sueldo(self):
        pass

    def mostrarInfo(self):
        print(f"Nombre: {self.__nombre}, Direccion: {self.__direccion}, DNI: {self.__dni}")

    def info(self):
        print(f"Nombre: {self.__nombre}, Telefono: {self.__telefono}")

    def mostrarDatos(self):
        print("Datos Empleado")
        print(f"Nombre: {self.__nombre}, DNI: {self.__dni}, Direccion: {self.__direccion}, Telefono: {self.__telefono}")

