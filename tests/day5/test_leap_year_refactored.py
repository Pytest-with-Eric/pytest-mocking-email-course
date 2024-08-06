import pytest
from src.refactor.leap_year_refactored import (
    LeapYear,
    RequestsAdapter,
    ApiResponseParser,
)


@pytest.fixture()
def leap_year():
    request_adapter = RequestsAdapter()
    api_response_parser = ApiResponseParser()
    return LeapYear(
        "https://digidates.de/api/v1/leapyear",
        request_adapter,
        api_response_parser,
    )


def test_leap_year_true(leap_year):
    assert leap_year.check_leap_year(year="2024") is True


def test_leap_year_false(leap_year):
    assert leap_year.check_leap_year(year="2023") is False
