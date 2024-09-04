import pytest
from unittest.mock import patch
from src.leap_year_refactored import LeapYearAPIAdaptor, LeapYear


@pytest.fixture()
def leap_year():
    api_adaptor = LeapYearAPIAdaptor("https://digidates.de/api/v1/leapyear")
    leap_year = LeapYear(api_adaptor)
    return leap_year


def test_leap_year_true(leap_year):
    assert leap_year.check_leap_year(year="2024") is True


def test_leap_year_false(leap_year):
    assert leap_year.check_leap_year(year="2023") is False


@patch(
    "src.leap_year_refactored.LeapYearAPIAdaptor.get_leap_year_info",
    return_value={"leapyear": True},  # Mock the return value to simulate API response
    autospec=True,  # Ensure the mock respects the method signature
)
def test_leap_year_mocked(mocked_get_leap_year_info):
    # Create the LeapYear instance after the patch is applied
    api_adaptor = LeapYearAPIAdaptor("https://digidates.de/api/v1/leapyear")
    leap_year = LeapYear(api_adaptor)

    # Perform the test
    assert leap_year.check_leap_year(year="2023") is True

    # Verify that the mock was called with the correct argument
    mocked_get_leap_year_info.assert_called_once_with(api_adaptor, "2023")
