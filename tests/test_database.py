import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    def test_available_buns(self, db):
        buns = db.available_buns()
        assert isinstance(buns, list)
        assert len(buns) == 3
        assert all(isinstance(b, Bun) for b in buns)
        names = {b.get_name() for b in buns}
        assert names == {"black bun", "white bun", "red bun"}

    def test_available_ingredients(self, db):
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        assert all(isinstance(i, Ingredient) for i in ingredients)
        types = {i.get_type() for i in ingredients}
        assert types <= {INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING}