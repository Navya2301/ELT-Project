# CUSTOM ETL PROJECT

This repo contains a custom Extract, Transform, Load project that uses Docker, PostgresSQL to show a simple ETL process

Checking if the dumped data in source postgres DB is getting transferred to Destination postgres DB

## Repo Structure

1. **docker-compose.yaml**: This file contains the configuration for Docker Compose, this file is used to run multiple docker containers It defines three services:
   - `source_postgres`: The source PostgreSQL DB.
   - `destination_postgres`: The destination PostgreSQL DB.
   - `elt_script`: The service that runs the ELT script.

2. **elt_script/Dockerfile**: This Dockerfile sets up a Python environment and installs the PostgreSQL client. It also copies the ELT script into the container and sets it as the default command.

3. **elt_script/elt_script.py**: This Python script performs the ELT process. It waits for the source PostgreSQL database to become available, then dumps its data to a SQL file named data_dump.sql and loads this data into the destination PostgreSQL database.

4. **source_db/init.sql**: This SQL script initializes the source database with sample fake data. It creates tables for users, films, film categories, actors, and film actors, and inserts sample data into these tables.


## Process

1. **Docker Compose**: Using the `docker-compose.yaml` file, three Docker containers are spun up:
   - A source PostgreSQL database with sample data.
   - A destination PostgreSQL database.
   - A Python environment that runs the ELT script.

2. **ELT Process**: The `elt_script.py` waits for the source PostgreSQL database to become available. Once it's available, the script uses `pg_dump` to dump the source database to a SQL file. Then, it uses `psql` to load this SQL file into the destination PostgreSQL database.

3. **Database Initialization**: The `init.sql` script initializes the source database with sample data. It creates several tables and populates them with sample data.



## DBT

To automate the script to run every day we can use DBT. DBT is a open source tool we can utilise to write custom transformations, custom models.

## CRON Job Implementation

In this branch, a CRON job has been implemented to automate the ELT process. The CRON job is scheduled to run the ELT script at specified intervals, ensuring that the data in the destination PostgreSQL database is regularly updated with the latest data from the source database.

To configure the CRON job:

1. Currently, the CRON job is setup to run every day at 10am.
2. You can adjust the time as needed within the Dockerfile found in the `elt` folder.

## Getting Started

1. Ensure you have Docker and Docker Compose installed on your machine.
2. Clone this repository.
3. Navigate to the repository directory and run `docker-compose up`.
4. Once all containers are up and running, the ELT process will start automatically.
5. After the ELT process completes, you can access the source and destination PostgreSQL databases on ports 5433 and 5434, respectively.
