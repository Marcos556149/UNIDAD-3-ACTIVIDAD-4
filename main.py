from datetime import date
from datetime import datetime
from ClaseManejadorEmpleados import ManejadorEmpleados
if __name__=='__main__':
    dimension= int(input('Ingrese la dimension del arreglo de Empleados: '))
    Empleados= ManejadorEmpleados(dimension,5)
    Empleados.leerPlantas()
    Empleados.leerContratados()
    Empleados.leerExternos()
    while True:
        print("_____MENU DE OPCIONES_____")
        print("[1]...Registrar Horas")
        print("[2]...Total de Tarea")
        print("[3]...Ayuda Solidaria")
        print("[4]...Calcular Sueldo")
        print("[0]...Salir")
        try:
            op= int(input('Seleccione una opcion: '))
            if op in range(5):
                if op == 1:
                    Empleados.incrementarHoras()
                if op == 2:
                    Empleados.TotalTarea()
                if op == 3:
                    Empleados.Ayuda()
                if op == 4:
                    Empleados.CalcularSueldo()
                if op == 0:
                    print("_____MENU FINALIZADO_____")
                    break
            else:
                print("ERROR, solo puede seleccionar numeros del 0 al 4")
        except ValueError:
            print("ERROR, ingrese solamente numeros")
