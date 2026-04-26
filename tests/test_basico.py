def test_suma():
    resultado = 2 + 2
    assert resultado == 4

def test_lista():
    frutas = ["manzana", "pera", "uva"]
    assert "pera" in frutas
    assert len(frutas) == 3