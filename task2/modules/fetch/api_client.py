import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from .models import CurrencyRateParams


class APIClient:
    """
    A class to handle API requests for currency rates.
    """

    def __init__(self, apikey: str) -> None:
        """
        Initializes the APIClient with the provided API key.

        :param apikey: The API key for authentication.
        """
        self._REQUEST_HEADERS = {"apikey": apikey}

    @retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
    def _make_request(self, url: str, params: CurrencyRateParams) -> dict:
        """
        Sends a GET request to the specified URL with the provided parameters.
        Retries the request up to 5 times with a 2-second delay between attempts.

        :param url: The API endpoint URL.
        :param params: An instance of CurrencyRateParams containing the query parameters.
        :return: The JSON response from the API as a dictionary.
        :raises: RequestsException if the request fails after retries.
        """
        response = requests.get(url=url, headers=self._REQUEST_HEADERS, params=params.dict())
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        return response.json()

    def get(self, url: str, params: CurrencyRateParams) -> dict | None:
        """
        Wrapper around the _make_request method to return None after retry attempts if all fail.

        :param url: The API endpoint URL.
        :param params: An instance of CurrencyRateParams containing the query parameters.
        :return: The JSON response from the API as a dictionary, or None if the request fails after retries.
        """
        try:
            return self._make_request(url, params)
        except requests.exceptions.RequestException as e:
            print(f"All retry attempts failed. Error: {e}")
            return None
