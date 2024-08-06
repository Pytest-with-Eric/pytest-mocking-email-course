import pytest
from unittest.mock import patch
from src.leap_year import LeapYear


@pytest.fixture()
def leap_year():
    return LeapYear("https://digidates.de/api/v1/leapyear")


@patch("requests.get")
def test_fetch_data(mocked_requests, leap_year):
    expected_json = {"leapyear": True}
    mocked_requests.return_value.json.return_value = expected_json
    result = leap_year.check_leap_year(year="2023")  # 2023 is not a leap year
    assert result == expected_json
    mocked_requests.assert_called_once_with(
        "https://digidates.de/api/v1/leapyear/?year=2023"
    )
