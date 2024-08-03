import pytest
import os
from unittest.mock import Mock, patch
from src.calculator import Calculator


# Using Mock Object as a fixture
@pytest.fixture
def mock_calculator():
    return Mock()


def test_addition(mock_calculator):
    mock_calculator.add.return_value = 10
    result = mock_calculator.add(1, 2)
    assert result == 10
    mock_calculator.add.assert_called_once_with(1, 2)


## Using the `mocker` fixture from pytest-mock to patch the `subtract` method
def test_subtraction(mocker):
    mocker.patch("src.calculator.Calculator.subtract", return_value=10)
    calculator = Calculator()
    result = calculator.subtract(1, 2)
    assert result == 10


@patch("src.calculator.Calculator.multiply")
def test_multiply(patched_multiply):
    patched_multiply.return_value = 10
    calculator = Calculator()
    result = calculator.multiply(1, 2)
    assert result == 10
    patched_multiply.assert_called_once_with(1, 2)


# Patching the method without using autospec
@patch("src.calculator.Calculator.multiply")
def test_multiply_no_autospec(patched_multiply):
    patched_multiply.return_value = 10
    calculator = Calculator()
    result = calculator.multiply(1, 2, 3)  # Extra argument, false positive
    assert result == 10


# Patching the method with autospec
@pytest.mark.xfail(
    reason="This test is expected to fail because of the incorrect arguments"
)
@patch("src.calculator.Calculator.multiply", autospec=True)
def test_multiply_autospec(patched_multiply):
    patched_multiply.return_value = 10
    calculator = Calculator()
    result = calculator.multiply(1, 2, 3)  # Fails because of the extra argument
    assert result == 10


# Patching the os.environ dictionary
@patch.dict("os.environ", {"ENV_VAR": "mocked_value"})
def test_env_var():
    assert os.environ["ENV_VAR"] == "mocked_value"


# Using the `patch` decorator to mock the `divide` method
@patch.object(Calculator, "divide")
def test_divide(mock_divide):
    mock_divide.return_value = 10
    calculator = Calculator()
    result = calculator.divide(1, 2)
    assert result == 10
    mock_divide.assert_called_once_with(1, 2)
