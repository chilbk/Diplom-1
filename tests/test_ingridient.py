import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient():
    @pytest.mark.parametrize("ingredient, name, price", [(INGREDIENT_TYPE_SAUCE, "Carry", 350.0), (INGREDIENT_TYPE_FILLING, "Chicken", 2700.0), (INGREDIENT_TYPE_FILLING, "Onion", 170.0)])
    def test_get_ingredient_name_price(self, ingredient, name, price):
        ing = Ingredient(ingredient_type=ingredient, name=name, price=price)
        assert ing.get_type() == ingredient
        assert ing.get_name() == name
        assert ing.get_price() == price
