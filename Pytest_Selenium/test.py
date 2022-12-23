def test_deve_ser_verdadeiro():
    assert True
    
    
def soma(x, y):
    return x + y


def test_soma_x_y():
    esperado = 3  # Configurando teste
    
    resultado = soma(1, 2)  # Ação
    
    assert esperado == resultado  # Assertiva