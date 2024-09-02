
# Project Overview

> Interactive lucidcharts schema can be found [here](https://lucid.app/lucidchart/2eb4b21c-87bf-463b-8876-88410050e8bf/edit?invitationId=inv_547753bd-6760-4d01-8104-30e3ed88fdab)

## Introduction
This project involves building a data pipeline using dbt (data build tool) to analyze interactions between astrologers and users on a platform. The pipeline is organized into three layers: **Bronze**, **Intermediate**, and **Gold**, each serving a specific purpose in the data transformation process.

## Project Structure
The project is organized into three main layers:
- **Bronze Layer**: Contains raw data ingested from various sources without significant transformations. This layer acts as the foundation for subsequent transformations.
- **Intermediate Layer**: Includes models that perform data cleaning, enrichment, and minor transformations. These models are used to prepare data for final aggregation.
- **Gold Layer**: Contains the final models used for reporting and analytics. These models are fully transformed and aggregated to provide insights into the platform's operations.

## Models and Transformations
### Bronze Layer
- **raw_astrologs**: Contains information about astrologers.
- **raw_users**: Contains information about users.
- **raw_astrolog_user_ref**: Links astrologers with users, including the type of relationship and the creation timestamp.
- **raw_astrolog_ping_events**: Records events when astrologers ping users.
- **raw_chat_events**: Records chat sessions between users and astrologers.

### Intermediate Layer
- **int_astrolog_ping_event_extended**: Enriched model of astrologer ping events, with additional information about the astrologer and the relationship type.

### Gold Layer
- **astrologs_activity**: Aggregated data on astrologers' daily ping activity and successful chat sessions.
- **pings_amount**: Aggregated count of pings per day.
- **pings_chat_duration**: Average duration and revenue of chat sessions that originated from pings.
- **pings_conversion**: Conversion rate of pings to successful chat sessions by astrologer.
- **user_type_conversion**: Conversion rate of pings to successful chat sessions by user type.

## Data Sources
The data used in this project comes from the following sources:
- **CSV Files**: Seed data used to populate the initial tables in the Bronze layer.
- **Database**: The project may also connect to a database to retrieve raw data.

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