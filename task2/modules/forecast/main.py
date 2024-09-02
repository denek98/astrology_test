from .model import ForecastModel
from .utils import split_data, generate_future_dates
from .config import VALIDATION_DAYS, FORECAST_DAYS


def forecast_exchange_rates(historical_data: dict[str, float]) -> dict:
    """
    Prepares data, trains the model, and returns the forecast for future exchange rates.

    :param historical_data: A dictionary of historical exchange rates.
    :return: A dictionary with predicted future dates and corresponding exchange rates.
    """
    x_train, y_train, x_valid, y_valid = split_data(historical_data, VALIDATION_DAYS)

    model = ForecastModel(validation_days=VALIDATION_DAYS, forecast_days=FORECAST_DAYS)
    model.train_model(x_train, y_train, x_valid, y_valid)

    last_index = len(historical_data) - 1
    last_date = sorted(historical_data.keys())[-1]

    y_predict = model.predict_next_days(last_index)
    float_predicts = [float(predict) for predict in y_predict]

    future_dates = generate_future_dates(last_date, FORECAST_DAYS)

    forecast = dict(zip(future_dates, float_predicts))
    return forecast


if __name__ == "__main__":
    historical_data = {
        "2024-08-01": 1.0987,
        "2024-08-02": 1.1015,
        "2024-08-03": 1.0992,
        "2024-08-04": 1.1023,
        "2024-08-05": 1.1050,
        "2024-08-06": 1.1038,
        "2024-08-07": 1.1011,
        "2024-08-08": 1.1004,
        "2024-08-09": 1.0989,
        "2024-08-10": 1.0972,
        "2024-08-11": 1.0955,
        "2024-08-12": 1.0968,
        "2024-08-13": 1.0981,
        "2024-08-14": 1.0994,
        "2024-08-15": 1.1007,
        "2024-08-16": 1.1019,
        "2024-08-17": 1.1032,
        "2024-08-18": 1.1045,
        "2024-08-19": 1.1060,
        "2024-08-20": 1.1072,
        "2024-08-21": 1.1085,
        "2024-08-22": 1.1098,
        "2024-08-23": 1.1080,
        "2024-08-24": 1.1063,
        "2024-08-25": 1.1047,
        "2024-08-26": 1.1030,
        "2024-08-27": 1.1042,
        "2024-08-28": 1.1055,
        "2024-08-29": 1.1067,
        "2024-08-30": 1.1079,
        "2024-08-31": 1.1092,
        "2024-09-01": 1.1104,
        "2024-09-02": 1.1117,
        "2024-09-03": 1.1130,
        "2024-09-04": 1.1143,
        "2024-09-05": 1.1126,
        "2024-09-06": 1.1109,
    }

    forecast = forecast_exchange_rates(historical_data)
    print(forecast)
