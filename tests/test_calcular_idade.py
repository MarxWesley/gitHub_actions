from app.calcular_idade import calcular_idade, count_characters

def test_calcular_idade():
    assert calcular_idade(2000) == 23

def test_count_characters():
    assert count_characters("Hello") == 5