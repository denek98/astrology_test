from datetime import datetime, timedelta


class ApiDataProcessor:
    """
    A class to process data received from the API.
    """

    @staticmethod
    def parse_response(response: dict, rate_currency: str) -> dict[str, float]:
        """
        Parses the API response and extracts the exchange rates for a specific currency.

        :param response: The JSON response from the API containing exchange rates.
        :param rate_currency: The currency for which to extract the exchange rate.
        :return: A dictionary with dates as keys and exchange rates as values.
        """
        rate_result_dict = {}
        for response_rate_date, response_rate_dict in response["data"].items():
            rate_result_dict[response_rate_date] = response_rate_dict[rate_currency]
        return rate_result_dict

    @staticmethod
    def generate_list_of_dates(start_date: str, end_date: str) -> list[str]:
        """
        Generates a list of dates between the start and end dates.

        :param start_date: The start date in 'YYYY-MM-DD' format.
        :param end_date: The end date in 'YYYY-MM-DD' format.
        :return: A list of dates in 'YYYY-MM-DD' format between start_date and end_date.
        """
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        return [(start + timedelta(days=x)).strftime("%Y-%m-%d") for x in range((end - start).days + 1)]
