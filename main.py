from tabulate import tabulate
from FuncionesPrograma import nuevo_gasto_man, imprimir_lista
from FormatearLista import FormatearLista

def main():

    print("HERRAMIENTA DE GESTIÓN DE GASTOS")

    while True:
        opcion_usuario = input("Qué desea hacer:\n   1. Imprimir listado de gastos simple\n   2. Imprimir listado de gastos con formato grid\n   3. Crear nuevo gasto\n   4. Salir\n >>> ")

        if opcion_usuario == "1":
            imprimir_lista()
        elif opcion_usuario == "2":
           FormatearLista()
        elif opcion_usuario == "3":
           nuevo_gasto_man()
        elif opcion_usuario == "4":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()