from datetime import datetime, timedelta
from typing import Dict, Tuple
import numpy as np


def split_data(historical_rates: Dict[str, float], validation_days: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Splits the historical data into training and validation datasets.

    :param historical_rates: A dictionary of dates and their corresponding exchange rates.
    :param validation_days: The number of days to be used as validation data.
    :return: x_train, y_train, x_valid, y_valid
    """
    sorted_dates = sorted(historical_rates.keys())
    x = np.array(range(len(sorted_dates))).reshape(-1, 1)
    y = np.array([historical_rates[date] for date in sorted_dates])

    x_train, x_valid = x[:-validation_days], x[-validation_days:]
    y_train, y_valid = y[:-validation_days], y[-validation_days:]

    return x_train, y_train, x_valid, y_valid


def generate_future_dates(last_date: str, forecast_days: int) -> list:
    """
    Generates a list of future dates for the forecast period.

    :param last_date: The last known date in the historical data.
    :param forecast_days: The number of days to forecast into the future.
    :return: A list of future dates as strings in the format 'YYYY-MM-DD'.
    """
    last_date_obj = datetime.strptime(last_date, "%Y-%m-%d")
    next_dates = [last_date_obj + timedelta(days=i) for i in range(1, forecast_days + 1)]
    next_dates_str = [date.strftime("%Y-%m-%d") for date in next_dates]

    return next_dates_str
