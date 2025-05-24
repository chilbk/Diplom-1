
from praktikum.ingredient import Ingredient
# Метод  test_ingredient_creation проверяет, что можно  создать ингредиент
def test_ingredient_creation():
    ingredient = Ingredient(ingredient_type='соус', name='Барбекю', price=1.2)
    assert ingredient.type == 'соус'
    assert ingredient.name == 'Барбекю'
    assert ingredient.price == 1.2

# Метод test_get_name проверяет название ингредиента. Название сходится с заданным
def test_get_name():
    ingredient = Ingredient(ingredient_type='начинка', name='Котлета', price=3.5)
    assert ingredient.get_name() == 'Котлета'

# Метод test_get_price проверяет цену ингредиента. Цена сходится заданной
def test_get_price():
    ingredient = Ingredient(ingredient_type='соус', name='Сырный', price=0.8)
    assert ingredient.get_price() == 0.8

# Метод test_get_type проверяет тип ингредиента. Тип сходится с заданным
def test_get_type():
    ingredient = Ingredient(ingredient_type='начинка', name='Салат', price=0.5)
    assert ingredient.get_type() == 'начинка'