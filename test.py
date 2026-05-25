import pytest
from FuncionesPrograma import nuevo_gasto_importado, lista_gastos

def test_nuevo_gasto_importado():
    nuevo_gasto_importado("Galletas", 3.49)
    assert lista_gastos[-1] == ["Galletas", 3.49]