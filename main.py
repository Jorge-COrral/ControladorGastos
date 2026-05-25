from tabulate import tabulate
from FuncionesPrograma import nuevo_gasto_man, imprimir_lista

def main():

    print("HERRAMIENTA DE GESTIÓN DE GASTOS")

    while True:
        opcion_usuario = input("Qué desea hacer:\n   1. Imprimir listado de gastos\n   2. Crear nuevo gasto\n   3. Salir\n >>> ")

        if opcion_usuario == "1":
            imprimir_lista()
        elif opcion_usuario == "2":
           nuevo_gasto_man()
        elif opcion_usuario == "3":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()