import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger():
    def test_set_bun(self, bun_simple):
        burger = Burger()
        burger.set_buns(bun_simple)
        assert burger.bun is bun_simple

    def test_add_ingredient(self, bun_simple, sauce_carry):
        burger = Burger()
        burger.set_buns(bun_simple)
        burger.add_ingredient(sauce_carry)
        assert burger.ingredients == [sauce_carry]

    def test_remove_ingredient(self, bun_simple, sauce_carry, filling_chicken):
        burger = Burger()
        burger.set_buns(bun_simple)
        burger.add_ingredient(sauce_carry)
        burger.add_ingredient(filling_chicken)
        burger.remove_ingredient(0)
        assert burger.ingredients == [filling_chicken]

    def test_remove_ingredient_with_invalid_index(self, bun_simple, sauce_carry, filling_chicken):
        burger = Burger()
        burger.set_buns(bun_simple)
        burger.add_ingredient(sauce_carry)
        burger.add_ingredient(filling_chicken)
        with pytest.raises(IndexError):
            burger.remove_ingredient(7)


    def test_move_ingredients(self, bun_simple, sauce_carry, filling_chicken):
        burger = Burger()
        burger.set_buns(bun_simple)
        burger.add_ingredient(sauce_carry)
        burger.add_ingredient(filling_chicken)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [filling_chicken, sauce_carry]


    def test_move_ingredients_with_invalid_index(self, bun_simple, sauce_carry, filling_chicken):
        burger = Burger()
        burger.set_buns(bun_simple)
        burger.add_ingredient(filling_chicken)
        with pytest.raises(IndexError):
            burger.move_ingredient(1, 0)


    def test_get_price_bun_with_mock(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 1200.0
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.get_price() == 2400.0
        mock_bun.get_price.assert_called()


    def test_get_price_with_ingredient_mock(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 700.0
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = 300.0
        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = 600.0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        assert burger.get_price() == 2300.0
        assert mock_ingredient_1.get_price.called
        assert mock_ingredient_2.get_price.called


    def test_get_receipt_with_mock(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Bulka"
        mock_bun.get_price.return_value = 750.0

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "Carry"
        mock_ingredient.get_price.return_value = 150.0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        assert burger.get_price() == 1650.0
        assert "(==== Bulka ====)" in receipt
        assert "= sauce Carry =" in receipt
        assert f"Price: {burger.get_price()}" in receipt











