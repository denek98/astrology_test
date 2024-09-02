from .config import BASE_CURRENCY, RATE_CURRENCY, BASE_CURRENCY_API_ENDPOINT, API_KEY, START_DATE, END_DATE
from .models import CurrencyRateParams
from .data_processor import ApiDataProcessor
from .api_client import APIClient


class CurrencyRateFetcher:
    """
    A class to fetch and store historical currency rates.
    """

    def __init__(
        self, start_date: str = START_DATE, end_date: str = END_DATE, base_currency: str = BASE_CURRENCY, rate_currency: str = RATE_CURRENCY
    ) -> None:
        """
        Initializes the CurrencyRateFetcher with the provided date range.

        :param start_date: The start date for fetching currency rates.
        :param end_date: The end date for fetching currency rates.
        :param base_currency: The base currency to fetch rates for.
        :param rate_currency: The currency to get rates against the base currency.
        """
        self.api_client = APIClient(apikey=API_KEY)
        self._historical_rate_dict = {}
        self.start_date = start_date
        self.end_date = end_date
        self.base_currency = base_currency
        self.rate_currency = rate_currency

    def get_historical_rate_dict(
        self,
    ) -> dict:
        """
        Fetches and returns a dictionary of historical currency rates for the specified date range.


        :return: A dictionary where the keys are dates and the values are the exchange rates.
        """
        for rate_date in ApiDataProcessor.generate_list_of_dates(start_date=self.start_date, end_date=self.end_date):
            self._populate_historical_rate_dict(rate_date=rate_date)
        return self._historical_rate_dict

    def _populate_historical_rate_dict(self, rate_date: str) -> None:
        """
        Populates the dictionary with historical currency rates for the given date.
        :param rate_date: The date for which to fetch the rate.
        """
        currency_rate_params = CurrencyRateParams(base_currency=self.base_currency, currencies=self.rate_currency, date=rate_date)
        if response := self.api_client.get(url=BASE_CURRENCY_API_ENDPOINT, params=currency_rate_params):
            self._historical_rate_dict.update(ApiDataProcessor.parse_response(response=response, rate_currency=self.rate_currency))


def get_historical_rate():
    fetcher = CurrencyRateFetcher()
    return fetcher.get_historical_rate_dict()
