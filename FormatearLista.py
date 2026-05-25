from tabulate import tabulate
from FuncionesPrograma import lista_gastos, headers



def FormatearLista():
    print(tabulate(lista_gastos, headers=headers, tablefmt="grid"))