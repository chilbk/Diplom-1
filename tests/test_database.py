import pytest
from data import DataBaseBurger
from unittest.mock import Mock

class TestDatabase:
    @pytest.mark.parametrize('index, name, price', DataBaseBurger.DATA_LIST_BUNS)
    def test_database_buns(self, create_database, index, name, price):
        assert name == create_database.buns[index].get_name()
        assert price == create_database.buns[index].get_price()


    @pytest.mark.parametrize('index, type_ingredient, name, price', DataBaseBurger.DATA_LIST_INGREDIENTS)
    def test_database_ingredients(self, create_database, index, type_ingredient, name, price):
        assert type_ingredient == create_database.ingredients[index].get_type()
        assert name == create_database.ingredients[index].get_name()
        assert price == create_database.ingredients[index].get_price()

    def test_available_buns(self, create_database):
        mock_buns = Mock()
        create_database.buns = [mock_buns]
        assert mock_buns in create_database.available_buns()

    def test_available_ingredients(self, create_database):
        mock_ingredients = Mock()
        create_database.ingredients = [mock_ingredients]
        assert mock_ingredients in create_database.available_ingredients()