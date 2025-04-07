from unittest.mock import patch, MagicMock
from praktikum.praktikum import main


class TestPraktikum:
    """Tests for the praktikum main module."""

    @patch("praktikum.praktikum.Database")
    @patch("praktikum.praktikum.Burger")
    def test_main(self, mock_burger_class, mock_database_class):
        """Test that the main function returns the correct receipt string."""
        # Arrange
        mock_burger = MagicMock()
        mock_burger_class.return_value = mock_burger

        mock_database = MagicMock()
        mock_database_class.return_value = mock_database

        mock_buns = [MagicMock(), MagicMock(), MagicMock()]
        mock_ingredients = [MagicMock() for _ in range(6)]

        mock_database.available_buns.return_value = mock_buns
        mock_database.available_ingredients.return_value = mock_ingredients

        mock_receipt = "Mock Receipt"
        mock_burger.get_receipt.return_value = mock_receipt

        # Act
        result = main()

        # Assert
        mock_database_class.assert_called_once()
        mock_burger_class.assert_called_once()
        mock_database.available_buns.assert_called_once()
        mock_database.available_ingredients.assert_called_once()
        mock_burger.set_buns.assert_called_once_with(mock_buns[0])
        assert mock_burger.add_ingredient.call_count == 4
        mock_burger.move_ingredient.assert_called_once_with(2, 1)
        mock_burger.remove_ingredient.assert_called_once_with(3)
        mock_burger.get_receipt.assert_called_once()
        assert result == mock_receipt
