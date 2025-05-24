from praktikum.bun import Bun

# Метод для проверки создания булочки
def test_bun_creation():
    bun = Bun(name='Булочка ржаная', price=2.5)
    assert bun.name == 'Булочка ржаная'
    assert bun.price == 2.5
# Метод, который проверяет, что метод get_name() возвращает заданное название
def test_get_name():
    bun = Bun(name='Булочка с кунжутом', price=1.5)
    assert bun.get_name() == 'Булочка с кунжутом'
# Метод, который проверяет, что метод get_price() возвращает заданную цену
def test_get_price():
    bun = Bun(name='Булочка чёрная', price=3.0)
    assert bun.get_price() == 3.0