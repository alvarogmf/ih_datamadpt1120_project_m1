import pandas as pd
import re


def db_cleaning(db):
    """
    This function will standardize the Gender column to have only Male & Female outputs
    """
    db['gender'] = db['gender'].str.capitalize()
    db['gender'] = db['gender'].str.replace(r'\b[f]\w+', 'female')
    db['gender'] = db['gender'].str.replace(r'\b[m]\w+', 'male')
    return db


def countries_clean(countries_df):
    """
    This function will eliminate all the parenthesis and Null rows in the Countries Database
    """
    final_countries = countries_df.dropna()
    final_countries['country_code'] = final_countries['country_code'].str.extract(r'(\b\w\S)')
    return final_countries


def final_table(main_df, jobs_df, countries_df):
    """
    This function merges all the tables to have a unique table with all the information.
    """
    merged_jobs = pd.merge(main_df, jobs_df, on="normalized_job_code")
    merged_countries = pd.merge(merged_jobs, countries_df, on="country_code")
    merged_countries['Quantity'] = 1
    merged_countries['Percentage'] = 1 / len(merged_countries)
    return merged_countries[['Country_Name', 'title', 'gender', 'Quantity', 'Percentage']]

