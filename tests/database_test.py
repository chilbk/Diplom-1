import pytest
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Tests for the Database class."""

    @pytest.fixture
    def database(self):
        """Create a database instance for testing."""
        return Database()

    def test_database_creation(self, database):
        """Test that a database is initialized with the correct data."""
        # Assert
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

        # Check that buns are initialized correctly
        assert isinstance(database.buns[0], Bun)
        assert database.buns[0].get_name() == "black bun"
        assert database.buns[0].get_price() == 100

        assert database.buns[1].get_name() == "white bun"
        assert database.buns[1].get_price() == 200

        assert database.buns[2].get_name() == "red bun"
        assert database.buns[2].get_price() == 300

        # Check that ingredients are initialized correctly
        assert isinstance(database.ingredients[0], Ingredient)
        assert database.ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert database.ingredients[0].get_name() == "hot sauce"
        assert database.ingredients[0].get_price() == 100

        assert database.ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert database.ingredients[1].get_name() == "sour cream"
        assert database.ingredients[1].get_price() == 200

        assert database.ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE
        assert database.ingredients[2].get_name() == "chili sauce"
        assert database.ingredients[2].get_price() == 300

        assert database.ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert database.ingredients[3].get_name() == "cutlet"
        assert database.ingredients[3].get_price() == 100

        assert database.ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert database.ingredients[4].get_name() == "dinosaur"
        assert database.ingredients[4].get_price() == 200

        assert database.ingredients[5].get_type() == INGREDIENT_TYPE_FILLING
        assert database.ingredients[5].get_name() == "sausage"
        assert database.ingredients[5].get_price() == 300

    def test_available_buns(self, database):
        """Test that available_buns method returns all buns."""
        # Act
        buns = database.available_buns()

        # Assert
        assert len(buns) == 3
        assert buns == database.buns

    def test_available_ingredients(self, database):
        """Test that available_ingredients method returns all ingredients."""
        # Act
        ingredients = database.available_ingredients()

        # Assert
        assert len(ingredients) == 6
        assert ingredients == database.ingredients
