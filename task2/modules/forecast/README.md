# Forecast Module

## Overview

The `forecast` module is responsible for configuring and executing the currency exchange rate forecasting model. It uses historical data to predict future exchange rates over a specified period.

## Key Components

- **ForecastModel**: A class that implements the forecasting logic using linear regression or other predictive algorithms.
- **VALIDATION_DAYS** and **FORECAST_DAYS**: Configuration settings that define the number of days used for model validation and prediction, respectively.

## Usage

This module is used to create and train forecasting models. It requires historical exchange rate data, which can be provided by the `fetch` module, to make accurate predictions.
