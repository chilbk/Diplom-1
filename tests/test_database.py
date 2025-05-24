from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING)

# Метод test_available_buns проверяет, что метод available_buns возвращает список из 3 булочек,
def test_available_buns():
    db = Database()
    buns = db.available_buns()

    assert isinstance(buns, list)
    assert len(buns) == 3

    assert all(isinstance(bun, Bun) for bun in buns)
    assert buns[0].name == 'black bun'
    assert buns[1].price == 200

# Метод test_available_ingredients проверяет, что метод available_ingredients возвращает список из 6 ингредиентов,
# где 3 — соусы, 3 — начинки, и все элементы являются экземплярами класса Ingredient.
def test_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()

    assert isinstance(ingredients, list)
    assert len(ingredients) == 6

    assert all(isinstance(ing, Ingredient) for ing in ingredients)

    sauces = [ing for ing in ingredients if ing.type == INGREDIENT_TYPE_SAUCE]
    fillings = [ing for ing in ingredients if ing.type == INGREDIENT_TYPE_FILLING]

    assert len(sauces) == 3
    assert len(fillings) == 3

    assert sauces[0].name == 'hot sauce'
    assert fillings[1].name == 'dinosaur'