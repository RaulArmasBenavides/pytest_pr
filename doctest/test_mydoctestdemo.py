import pytest
from mydoctestdemo import doblar, invertir_cadena, es_primo, mcd, suma

@pytest.mark.parametrize("entrada,esperado", [
    ([1,2,3], [2,4,6]),
    ([], []),
    ([-1,0,1], [-2,0,2]),
])
def test_doblar(entrada, esperado):
    assert doblar(entrada) == esperado

@pytest.mark.parametrize("txt,rev", [
    ("Hola Mundo", "odnuM aloH"),
    ("", ""),
    ("😀ab", "ba😀"),
])
def test_invertir_cadena(txt, rev):
    assert invertir_cadena(txt) == rev

@pytest.mark.parametrize("n,esperado", [
    (11, True), (4, False), (2, True), (1, False), (-7, False)
])
def test_es_primo(n, esperado):
    assert es_primo(n) == esperado

@pytest.mark.parametrize("a,b,esperado", [
    (60,48,12), (7,5,1), (0,10,10), (0,0,0)
])
def test_mcd(a,b,esperado):
    assert mcd(a,b) == esperado

def test_suma():
    assert suma(1,1) == 2
    assert suma(-3,5) == 2
    assert suma(2.5,0.5) == 3.0
