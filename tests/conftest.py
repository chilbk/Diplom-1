import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def bun_simple():
    return Bun ("Simple", 1500.0)

@pytest.fixture
def sauce_carry():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "Carry", 350.0)

@pytest.fixture
def filling_chicken():
    return Ingredient(INGREDIENT_TYPE_FILLING, "Chicken", 2700.0)


@pytest.fixture
def burger(self, bun_simple, sauce_carry, filling_chicken):
    burger = Burger()
    burger.set_buns(bun_simple)
    burger.add_ingredient(sauce_carry)
    burger.add_ingredient(filling_chicken)

    return burger

@pytest.fixture
def db():
    return Database()

