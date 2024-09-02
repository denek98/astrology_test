from modules.forecast import forecast_exchange_rates
from modules.plot import plot_forecast
from modules.fetch import get_historical_rate

if __name__ == "__main__":
    historical_rate_data = get_historical_rate()
    forecast = forecast_exchange_rates(historical_rate_data)
    plot_forecast(historical_rate_data, forecast)
