import pytest
from src.leap_year import LeapYear


@pytest.fixture()
def leap_year():
    return LeapYear("https://digidates.de/api/v1/leapyear")


def test_leap_year_1(leap_year):
    response = leap_year.check_leap_year(year=2024)
    assert response is True


def test_leap_year_2(leap_year):
    response = leap_year.check_leap_year(year=2023)
    assert response is False
