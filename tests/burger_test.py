import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Tests for the Burger class."""

    @pytest.fixture
    def empty_burger(self):
        """Create an empty burger for testing."""
        return Burger()

    @pytest.fixture
    def test_bun(self):
        """Create a test bun for testing."""
        return Bun("test bun", 100.0)

    @pytest.fixture
    def sauce_ingredient(self):
        """Create a sauce ingredient for testing."""
        return Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 50.0)

    @pytest.fixture
    def filling_ingredient(self):
        """Create a filling ingredient for testing."""
        return Ingredient(INGREDIENT_TYPE_FILLING, "test filling", 150.0)

    def test_burger_creation(self, empty_burger):
        """Test that a burger can be created."""
        # Assert
        assert empty_burger.bun is None
        assert empty_burger.ingredients == []

    def test_set_buns(self, empty_burger, test_bun):
        """Test that buns can be added to the burger."""
        # Act
        empty_burger.set_buns(test_bun)

        # Assert
        assert empty_burger.bun is test_bun

    def test_add_ingredient(self, empty_burger, sauce_ingredient):
        """Test that ingredients can be added to the burger."""
        # Act
        empty_burger.add_ingredient(sauce_ingredient)

        # Assert
        assert len(empty_burger.ingredients) == 1
        assert empty_burger.ingredients[0] is sauce_ingredient

    def test_remove_ingredient(
        self, empty_burger, sauce_ingredient, filling_ingredient
    ):
        """Test that ingredients can be removed from the burger."""
        # Arrange
        empty_burger.add_ingredient(sauce_ingredient)
        empty_burger.add_ingredient(filling_ingredient)

        # Act
        empty_burger.remove_ingredient(0)

        # Assert
        assert len(empty_burger.ingredients) == 1
        assert empty_burger.ingredients[0] is filling_ingredient

    def test_move_ingredient(self, empty_burger, sauce_ingredient, filling_ingredient):
        """Test that ingredients can be moved within the burger."""
        # Arrange
        empty_burger.add_ingredient(sauce_ingredient)
        empty_burger.add_ingredient(filling_ingredient)

        # Act
        empty_burger.move_ingredient(0, 1)

        # Assert
        assert len(empty_burger.ingredients) == 2
        assert empty_burger.ingredients[0] is filling_ingredient
        assert empty_burger.ingredients[1] is sauce_ingredient

    def test_move_ingredient_backward(
        self, empty_burger, sauce_ingredient, filling_ingredient
    ):
        """Test moving an ingredient from a later position to an earlier position."""
        # Arrange: Add two ingredients
        empty_burger.add_ingredient(sauce_ingredient)
        empty_burger.add_ingredient(filling_ingredient)
        # Act: Move the second ingredient (index 1) to the first position (index 0)
        empty_burger.move_ingredient(1, 0)
        # Assert: The order should be swapped
        assert empty_burger.ingredients[0] is filling_ingredient
        assert empty_burger.ingredients[1] is sauce_ingredient

    def test_get_price(
        self, empty_burger, test_bun, sauce_ingredient, filling_ingredient
    ):
        """Test that get_price method returns the correct total price."""
        # Arrange
        empty_burger.set_buns(test_bun)  # 100.0 * 2 = 200.0
        empty_burger.add_ingredient(sauce_ingredient)  # 50.0
        empty_burger.add_ingredient(filling_ingredient)  # 150.0

        # Act
        result = empty_burger.get_price()

        # Assert
        assert result == 400.0  # 200.0 + 50.0 + 150.0 = 400.0

    def test_get_receipt(
        self, empty_burger, test_bun, sauce_ingredient, filling_ingredient
    ):
        """Test that get_receipt method returns the correct receipt."""
        # Arrange
        empty_burger.set_buns(test_bun)
        empty_burger.add_ingredient(sauce_ingredient)
        empty_burger.add_ingredient(filling_ingredient)

        # Act
        receipt = empty_burger.get_receipt()

        # Assert
        expected_receipt = (
            "(==== test bun ====)\n"
            "= sauce test sauce =\n"
            "= filling test filling =\n"
            "(==== test bun ====)\n\n"
            "Price: 400.0"
        )
        assert receipt == expected_receipt

    def test_get_price_without_bun_raises(self, empty_burger):
        """Test that get_price raises an error if bun is not set."""
        with pytest.raises(ValueError, match="Bun is not set"):
            empty_burger.get_price()

    def test_get_receipt_without_bun_raises(self, empty_burger):
        """Test that get_receipt raises an error if bun is not set."""
        with pytest.raises(ValueError, match="Bun is not set"):
            empty_burger.get_receipt()
