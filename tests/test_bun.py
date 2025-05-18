import pytest
from praktikum.bun import Bun

class TestBun:
    # Тесты на нормальные случаи
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
        ("булочка с кунжутом", 150.50),  # Дробная цена
        ("b", 0.01),  # Минимальные значения
        ("очень длинное название булочки с множеством слов и символов", 999.99)  # Длинное название
    ])
    def test_bun_initialization_valid_cases(self, name, price):
        """Тестирование корректной инициализации булочки с валидными параметрами"""
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    # Тесты на граничные случаи
    @pytest.mark.parametrize("name, price", [
        ("", 100),  # Пустое название
        (" ", 100),  # Пробел в названии
        ("black bun", 0),  # Нулевая цена
        ("black bun", 0.001),  # Очень маленькая цена
        ("black bun", 999999.99),  # Очень большая цена
        ("123", 100),  # Название из цифр
        ("!@#$%^&*()", 100)  # Спецсимволы в названии
    ])
    def test_bun_edge_cases(self, name, price):
        """Тестирование граничных случаев"""
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    # Тесты на недопустимые типы цены
    @pytest.mark.parametrize("name, price, is_valid", [
        ("bun", 100, True),
        ("bun", "100", False),
        ("bun", None, False),
        ("bun", [100], False),
        ("bun", {"price": 100}, False)
    ])
    def test_bun_price_type_check(self, name, price, is_valid):
        """Проверяем, является ли цена числом"""
        bun = Bun(name, price)
        assert isinstance(bun.price, (int, float)) == is_valid

    # Тесты на отрицательные цены
    @pytest.mark.parametrize("name, price", [
        ("negative bun", -1),
        ("negative bun", -0.01),
        ("negative bun", -1000000)
    ])
    def test_bun_negative_price(self, name, price):
        """Тестирование отрицательных цен"""
        bun = Bun(name, price)
        assert bun.get_price() == price
