MLOps Weather Data Pipeline
This project demonstrates the construction of a data engineering pipeline for weather data using Apache Airflow and Data Version Control (DVC). The goal is to provide a comprehensive MLOps workflow, including data collection, preprocessing, versioning, and model training.

Objective
The aim of this project is to gain practical experience in:

Using DVC to manage datasets and machine learning models.
Streamlining data workflows with Airflow.
Implementing data versioning and model versioning.
Project Overview
Data Collection:

Gather live weather data through an API (e.g., OpenWeatherMap).
Collected data includes fields like Temperature, Humidity, Wind Speed, Weather Condition, Date, and Time.
Data is saved as raw_data.csv and tracked with DVC.
Data Preprocessing:

Handle missing values and standardize numerical fields.
Preprocessed data is saved as processed_data.csv and versioned with DVC.
Workflow Automation:

Automate data collection and preprocessing workflows using Airflow.
Model Training:

Train a simple linear regression model to predict temperature based on other features.
Save and version the model as model.pkl using DVC.
DVC Pipeline:

Define steps for data collection, preprocessing, and model training using DVC.
Technologies Used
Apache Airflow: For workflow automation.
DVC (Data Version Control): For versioning datasets and machine learning models.
Python: For data collection, preprocessing, and model training.
Instructions
Set up a Git repository and initialize DVC (dvc init).
Set up remote storage for DVC (e.g., Google Drive, AWS S3).
Automate data workflows using Airflow and version control using DVC.