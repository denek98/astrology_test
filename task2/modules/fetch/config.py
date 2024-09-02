import os
from datetime import datetime, timedelta

API_KEY: str = os.getenv("CURRENCY_RATE_APIKEY", "")
BASE_CURRENCY_API_ENDPOINT: str = "https://api.freecurrencyapi.com/v1/historical"
BASE_CURRENCY: str = "EUR"
RATE_CURRENCY: str = "USD"
START_DATE: str = (datetime.now().date() - timedelta(days=37)).strftime("%Y-%m-%d")
END_DATE: str = (datetime.now().date() - timedelta(days=1)).strftime("%Y-%m-%d")
