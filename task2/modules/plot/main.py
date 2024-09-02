import matplotlib.pyplot as plt


def plot_forecast(historical_data: dict[str, float], forecast: dict[str, float]) -> None:
    """
    Plots the actual and forecasted exchange rates against the dates.

    :param historical_data: A dictionary of historical exchange rates.
    :param forecast: A dictionary of forecasted exchange rates.
    """
    combined_data = {**historical_data, **forecast}
    dates = list(combined_data.keys())
    actual_values = list(historical_data.values())
    forecast_values = list(forecast.values())

    plt.plot(dates[: len(historical_data)], actual_values, label="Actual", color="blue", marker="o")

    plt.plot(dates[len(historical_data) :], forecast_values, label="Forecast", color="red", linestyle="--", marker="o")

    plt.xlabel("Date")
    plt.ylabel("Exchange Rate")
    plt.title("Actual vs Forecasted Exchange Rates")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()
