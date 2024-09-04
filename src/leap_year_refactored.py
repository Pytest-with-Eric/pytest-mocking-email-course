import requests
from requests.exceptions import RequestException


class LeapYearAPIAdaptor:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def get_leap_year_info(self, year: str) -> dict:
        try:
            response = requests.get(f"{self.endpoint}/?year={year}")
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except RequestException as e:
            print(f"Error fetching data: {e}")
            return {"leapyear": None}


class LeapYear:
    def __init__(self, api_adaptor: LeapYearAPIAdaptor):
        self.api_adaptor = api_adaptor

    def check_leap_year(self, year: str) -> bool:
        data = self.api_adaptor.get_leap_year_info(year)
        return data.get("leapyear", False) is True


if __name__ == "__main__":
    # Inject the real API adaptor during normal usage
    api_adaptor = LeapYearAPIAdaptor("https://digidates.de/api/v1/leapyear")
    leap_year = LeapYear(api_adaptor)
    print(leap_year.check_leap_year(year="2024"))
