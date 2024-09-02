from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np


class ForecastModel:
    """
    A class to build and apply a forecasting model for currency exchange rates using Linear Regression.
    """

    def __init__(self, validation_days: int = 7, forecast_days: int = 7) -> None:
        """
        Initializes the ForecastModel with specified validation and forecast periods.

        :param validation_days: The number of days to be used as validation data.
        :param forecast_days: The number of days to be forecasted.
        """
        self.validation_days = validation_days
        self.forecast_days = forecast_days
        self.model = None
        self.validation_error = None

    def train_model(self, x_train: np.ndarray, y_train: np.ndarray, x_valid: np.ndarray, y_valid: np.ndarray) -> None:
        """
        Trains a linear regression model using the provided training data, and calculates validation error.

        :param x_train: Features for training.
        :param y_train: Target values for training.
        :param x_valid: Features for validation.
        :param y_valid: Target values for validation.
        """
        self.model = LinearRegression()
        self.model.fit(x_train, y_train)

        y_pred_valid = self.model.predict(x_valid)
        self.validation_error = mean_squared_error(y_valid, y_pred_valid)
        print(f"Validation MSE: {self.validation_error:.10f}")

    def predict_next_days(self, last_index: int) -> np.ndarray:
        """
        Predicts the exchange rates for the next 'forecast_days' using the trained model.

        :param last_index: The index of the last known data point.
        :return: An array of predicted exchange rates for the next 'forecast_days'.
        """
        if not self.model:
            raise ValueError("The model has not been trained yet. Please train the model first.")

        x_predict = np.array(range(last_index + 1, last_index + 1 + self.forecast_days)).reshape(-1, 1)
        y_predict = self.model.predict(x_predict)

        return y_predict
