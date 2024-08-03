from unittest.mock import Mock, MagicMock, patch
import requests
from src.calculator import Calculator


def test_mock():
    # Create a mock object
    mock_obj = Mock()
    # Set return value
    mock_obj.some_method.return_value = "mocked value"
    # Call the method
    result = mock_obj.some_method()
    assert result == "mocked value"


def test_magic_mock():
    magic_mock = MagicMock()
    # Set a magic method return value
    magic_mock.__str__.return_value = "magic mock"
    assert str(magic_mock) == "magic mock"


@patch("src.calculator.Calculator.add")
def test_patch(patched_method_add):
    patched_method_add.return_value = 10
    calculator = Calculator()
    result = calculator.add(1, 2)
    assert result == 10


def fetch_data(url):
    response = requests.get(url)
    return response.json()


@patch("requests.get")
def test_fetch_data(patch_get):
    patch_get.return_value.json.return_value = {"key": "value"}

    result = fetch_data(
        "https://digidates.de/api/v1/unixtime?timestamp=2023-01-01%2000:00:00"
    )
    patch_get.assert_called_once_with(
        "https://digidates.de/api/v1/unixtime?timestamp=2023-01-01%2000:00:00"
    )

    assert result == {"key": "value"}
