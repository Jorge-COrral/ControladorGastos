from FuncionesPrograma import Funciones


class UserInterface:
    def menu_inicial(self):
        funciones = Funciones()
        
        print("HERRAMIENTA DE GESTIÓN DE GASTOS")

        while True:
            opcion_usuario = input("\nQué desea hacer:\n   1. Imprimir listado de gastos simple\n   2. Imprimir listado de gastos con formato grid\n   3. Crear nuevo gasto\n   4. Salir\n >>> ")

            if opcion_usuario == "1":
                funciones.imprimir_lista()
            elif opcion_usuario == "2":
                funciones.FormatearLista()
            elif opcion_usuario == "3":
                funciones.nuevo_gasto_man()
            elif opcion_usuario == "4":
                print("¡Adiós!")
                break
            else:
                print("Opción no válida")