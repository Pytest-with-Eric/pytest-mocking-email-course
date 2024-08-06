import requests
from requests.exceptions import RequestException


class LeapYear:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def check_leap_year(self, year: str) -> bool:
        try:
            response = requests.get(f"{self.endpoint}/?year={year}")
            response.raise_for_status()  # Raise an HTTPError for bad responses
            if response.status_code == 200 and response.json()["leapyear"] is True:
                return True
            elif response.status_code == 200 and response.json()["leapyear"] is False:
                return False
            else:
                return response.json()
        except RequestException as e:
            print(f"Error fetching data: {e}")
            return False


if __name__ == "__main__":
    leap_year = LeapYear("https://digidates.de/api/v1/leapyear")
    print(leap_year.check_connection())
    print(leap_year.check_leap_year(year="2024"))


