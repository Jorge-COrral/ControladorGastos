from tabulate import tabulate

class Funciones:
    def __init__(self):
        
        self.lista_gastos = [
                ["Recibo luz mayo 2026", 42.57],
                ["Recibo agua marzo-abril 2026", 31.23],
                ["Fruta semana 21", 28.96]
            ]

        self.headers = ["Gasto", "Precio (€)"]

    def nuevo_gasto_man(self):
        nombre = input("Nombre del gasto:\n >>>")
        precio_str = input("Precio del gasto:\n >>>")
        precio = float(precio_str)
        self.lista_gastos.append([nombre, precio])
        print(f"Gasto {nombre} por un importe de {precio} € añadido a la lista")

    def nuevo_gasto_importado(self, nombre: str, precio: float) -> list:
        self.lista_gastos.append([nombre, precio])
        print(f"Gasto {nombre} por un importe de {precio} € añadido a la lista")

    def imprimir_lista(self):
        print(tabulate(self.lista_gastos, headers=self.headers))
    
    def FormatearLista(self):
        print(tabulate(self.lista_gastos, headers=self.headers, tablefmt="grid"))