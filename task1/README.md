
# Project Overview

> Interactive lucidcharts schema can be found [here](https://lucid.app/lucidchart/5fd48fb1-0c1f-4050-8750-3884cc9c1b1f/edit?invitationId=inv_9fbec2a3-a081-487f-b4d4-575096959620)


## Introduction
This project is centered around building a data pipeline using dbt (data build tool) to analyze various metrics related to astrologers and their interactions with users on a platform. The primary focus is on calculating metrics such as average ratings, total earnings, and the share of earnings for each astrologer.

## Project Structure
The project is organized into several components:
- **Models**: SQL files that define the transformations and calculations to be performed on the data. For example, calculating the average rating of astrologers, summing their earnings, and determining the share of earnings relative to the total.
- **Seeds**: CSV files containing the raw data used in the models. This includes data about astrologers, chat sessions, pricing, and ratings.
- **Target**: The directory where dbt stores compiled SQL files, logs, and results of the dbt runs.

## Models and Transformations
### Core Models
- **astrolog_metrics.sql**: Calculates the average rating of each astrologer, their total earnings, and their share of the total earnings.
- **astrolog_metrics2.sql**: Extends the calculations by adding more detailed metrics.
- **astrolog_lvl_chats_amount.sql**: Focuses on the number of chats per astrologer level.

### Seeds
The seed data is essential for populating the initial tables in the Bronze layer:
- **astrologers.csv**: Contains information about astrologers.
- **chats.csv**: Records chat sessions between users and astrologers.
- **chat_pricing.csv**: Defines the pricing per minute for each astrologer level.
- **ratings.csv**: Contains ratings of chat sessions.

## How to Run the Project
To run the project, follow these steps:
1. Navigate to dbt project directory
   ```bash
   cd dbt
   ```
2. Set up your dbt environment and configure the connection settings in `profiles.yml`.
3. Run the dbt models using the following command:
   ```bash
   dbt run
   ```
4. To test the models, use:
   ```bash
   dbt test
   ```
