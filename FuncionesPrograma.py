from tabulate import tabulate

lista_gastos = [
        ["Recibo luz mayo 2026", 42.57],
        ["Recibo agua marzo-abril 2026", 31.23],
        ["Fruta semana 21", 28.96]
    ]

headers = ["Gasto", "Precio (€)"]

def nuevo_gasto_man():
    nombre = input("Nombre del gasto:\n >>>")
    precio_str = input("Precio del gasto:\n >>>")
    precio = float(precio_str)
    lista_gastos.append([nombre, precio])
    print(f"Gasto {nombre} por un importe de {precio} € añadido a la lista")

def nuevo_gasto_importado(nombre: str, precio: float) -> list:
    lista_gastos.append([nombre, precio])
    print(f"Gasto {nombre} por un importe de {precio} € añadido a la lista")

def imprimir_lista():
    print(tabulate(lista_gastos, headers=headers))