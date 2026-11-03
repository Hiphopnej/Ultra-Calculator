from unittest.mock import patch

from ultra_calculator.text_functions import inquirer_input


def test_inquirer_input():
    with patch("ultra_calculator.text_functions.inquirer.select") as mock_select:
        mock_select.return_value.execute.return_value = "3D"

        result = inquirer_input("Choose a dimension", ["2D", "3D"])

        assert result == "3D"
        mock_select.assert_called_once_with(
            message="Choose a dimension",
            choices=["2D", "3D"]
        )
        mock_select.return_value.execute.assert_called_once()