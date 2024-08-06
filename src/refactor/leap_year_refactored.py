import requests
from requests.exceptions import RequestException


class RequestsAdapter:
    def get(self, url: str) -> requests.Response:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except RequestException as e:
            print(f"Error fetching data: {e}")
            return None


class ApiResponseParser:
    def parse_leap_year_response(self, response: requests.Response) -> bool:
        data = response.json()
        return data.get("leapyear", False)


class LeapYear:
    def __init__(
        self, endpoint: str, client: requests.Request, parser: ApiResponseParser
    ):
        self.endpoint = endpoint
        self.client = client
        self.parser = parser

    def check_leap_year(self, year: str) -> bool:
        url = f"{self.endpoint}/?year={year}"
        response = self.client.get(url)
        if response is None:
            return False

        return self.parser.parse_leap_year_response(response)
