from ManejadorEmpleados import ManejadorEmpleados

if __name__=="__main__":
    dimension = int(input("Ingrese la dimension del arreglo"))
    ME = ManejadorEmpleados(dimension=4)
    ME.cargarEmpleados()
    ME.mostrarEmpleados()
    dni = int(input("Ingrese el dni de un Empleado: "))
    horas = input("Ingrese la cantidad de Horas Trabajadas en el Dia: ")
    ME.buscarDni(dni, horas)
    tarea = input("Ingrese una Tarea a buscar: ")
    ME.buscarTarea(tarea)
    ME.ayudaEconomica()
    ME.mostrarSalario()
