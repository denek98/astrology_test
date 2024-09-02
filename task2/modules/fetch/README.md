# Fetch Module

## Overview

The `fetch` module is responsible for retrieving historical currency exchange rates from an external API. It handles API requests, processes the received data, and returns it in a usable format for further analysis or forecasting.

## Key Components

- **APIClient**: A class that manages API requests, including retry mechanisms for handling request failures.
- **get_historical_rate**: A function that fetches historical exchange rates for a specified period and returns them as a dictionary.

## Usage

This module is primarily used to gather data that will be fed into the forecasting models. It is designed to be flexible and robust, handling multiple API request attempts in case of network or server errors.
