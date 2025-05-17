import sys
from pathlib import Path
"""
В проекте ругается, что не находит файл data.py, пришлось таким способом выкручиваться, чтобы запускать тесты.
"""
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

import pytest
import data
import generators
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from unittest.mock import Mock

@pytest.fixture()
def create_bun():
    create_bun = Bun(data.DataBun.BUN_NAME, data.DataBun.BUN_PRICE)
    return create_bun

@pytest.fixture()
def create_ingredient():
    create_ingredient = Ingredient(data.DataIngredient.INGREDIENT_TYPE,
                            data.DataIngredient.INGREDIENT_NAME,
                            data.DataIngredient.INGREDIENT_PRICE)
    return create_ingredient

@pytest.fixture()
def create_burger():
    burger = Burger()
    return burger

@pytest.fixture()
def mock_create_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = data.DataBun.BUN_NAME
    mock_bun.get_price.return_value = data.DataBun.BUN_PRICE
    return mock_bun

@pytest.fixture()
def mock_create_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = generators.generate_word()
    mock_ingredient.get_name.return_value = generators.generate_word()
    mock_ingredient.get_price.return_value = generators.generate_price()
    return mock_ingredient

@pytest.fixture()
def mock_ingredients():
    ingredients = []
    for i in range(data.DataIngredient.QUANTITY_INGREDIENT):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = f"type_{i}"
        mock_ingredient.get_name.return_value = f"ingredient_{i}"
        mock_ingredient.get_price.return_value = 10 * (i+1)
        ingredients.append(mock_ingredient)
    return ingredients

@pytest.fixture()
def prepared_burger(create_burger, mock_create_bun, mock_ingredients):
    create_burger.bun = mock_create_bun
    for ingredient in mock_ingredients:
        create_burger.add_ingredient(ingredient)
    return create_burger

@pytest.fixture()
def create_database():
    data_base = Database()
    return data_base