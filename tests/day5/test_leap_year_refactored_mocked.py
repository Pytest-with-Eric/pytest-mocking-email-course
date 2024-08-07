import pytest
from unittest.mock import Mock
from src.refactor.leap_year_refactored import (
    LeapYear,
    RequestsAdapter,
    ApiResponseParser,
)


@pytest.fixture
def mock_client():
    return Mock(spec=RequestsAdapter)


@pytest.fixture
def mock_parser():
    return Mock(spec=ApiResponseParser)


@pytest.fixture
def leap_year(mock_client, mock_parser):
    return LeapYear("https://api.example.com", mock_client, mock_parser)


def setup_mock_response(mock_client, mock_parser, response_data, parser_result):
    mock_client.get_response.return_value = response_data
    mock_parser.parse_leap_year_response.return_value = parser_result


def test_check_leap_year_true(leap_year, mock_client, mock_parser):
    # Setup mock response
    setup_mock_response(
        mock_client=mock_client,
        mock_parser=mock_parser,
        response_data={"leapyear": True},
        parser_result=True,
    )

    # Assertions
    assert leap_year.check_leap_year("2023") is True
    mock_client.get_response.assert_called_once_with(
        "https://api.example.com/?year=2023"
    )
    mock_parser.parse_leap_year_response.assert_called_once_with({"leapyear": True})


    