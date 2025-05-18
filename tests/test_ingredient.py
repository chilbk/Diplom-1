import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    # Тесты на нормальные случаи инициализации
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_FILLING, "cutlet", 200),
        (INGREDIENT_TYPE_SAUCE, "соус барбекю", 150.50),  # Дробная цена
        (INGREDIENT_TYPE_FILLING, "к", 0.01),  # Минимальные значения
        (INGREDIENT_TYPE_SAUCE, "очень длинное название ингредиента с множеством слов", 999.99)  # Длинное название
    ])
    def test_ingredient_initialization_valid_cases(self, ingredient_type, name, price):
        """Тестирование корректной инициализации ингредиента с валидными параметрами"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    # Тесты на граничные случаи
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "", 100),  # Пустое название
        (INGREDIENT_TYPE_FILLING, " ", 200),  # Пробел в названии
        (INGREDIENT_TYPE_SAUCE, "123", 150),  # Название из цифр
        (INGREDIENT_TYPE_FILLING, "!@#$%^&*()", 200),  # Спецсимволы в названии
        ("UNKNOWN_TYPE", "mystery", 100),  # Неизвестный тип
        (None, "null", 100),  # None в качестве типа
        (INGREDIENT_TYPE_SAUCE, "sauce", 0),  # Нулевая цена
        (INGREDIENT_TYPE_FILLING, "filling", 0.001),  # Очень маленькая цена
        (INGREDIENT_TYPE_SAUCE, "expensive", 999999.99)  # Очень большая цена
    ])
    def test_ingredient_edge_cases(self, ingredient_type, name, price):
        """Тестирование граничных случаев"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    # Тесты на недопустимые типы цены
    @pytest.mark.parametrize("ingredient_type, name, price, expected_valid", [
        (INGREDIENT_TYPE_SAUCE, "sauce", 100, True),
        (INGREDIENT_TYPE_FILLING, "filling", "100", False),  # Цена как строка
        (INGREDIENT_TYPE_SAUCE, "sauce", None, False),  # None в качестве цены
        (INGREDIENT_TYPE_FILLING, "filling", [100], False),  # Цена как список
        (INGREDIENT_TYPE_SAUCE, "sauce", {"price": 100}, False)  # Цена как словарь
    ])
    def test_ingredient_price_type_check(self, ingredient_type, name, price, expected_valid):
        """Проверяем, является ли цена числом"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert isinstance(ingredient.price, (int, float)) == expected_valid

    # Тесты на отрицательные цены
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "negative", -1),
        (INGREDIENT_TYPE_FILLING, "negative", -0.01),
        (INGREDIENT_TYPE_SAUCE, "very negative", -1000000)
    ])
    def test_ingredient_negative_price(self, ingredient_type, name, price):
        """Тестирование отрицательных цен"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
