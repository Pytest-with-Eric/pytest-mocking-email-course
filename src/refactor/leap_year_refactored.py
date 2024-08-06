from typing import Dict
import requests
from requests.exceptions import RequestException


class RequestsAdapter:
    def get_response(self, url: str) -> Dict:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error fetching data: {e}")
            return None


class ApiResponseParser:
    def parse_leap_year_response(self, data: Dict) -> bool:
        return data.get("leapyear", None)


class LeapYear:
    def __init__(
        self, endpoint: str, client: requests.Request, parser: ApiResponseParser
    ):
        self.endpoint = endpoint
        self.client = client
        self.parser = parser

    def check_leap_year(self, year: str) -> bool:
        url = f"{self.endpoint}/?year={year}"
        response = self.client.get_response(url)
        if response is None:
            return False

        return self.parser.parse_leap_year_response(response)




