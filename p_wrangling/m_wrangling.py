import pandas as pd
from p_acquisition import m_acquisition as acq

def db_cleaning(db):
    db['gender'] = db['gender'].str.capitalize()
    db['gender'] = db['gender'].str.replace(r'\b[f]\w+', 'female')
    db['gender'] = db['gender'].str.replace(r'\b[m]\w+', 'male')
    return db


def countries_clean(countries_df):
    final_countries = countries_df.dropna()
    final_countries['Country_ID'] = final_countries['Country_ID'].str.replace("(","")
    countries_df['Country_ID'] = countries_df['Country_ID'].str.replace(")","")
    return final_countries


def final_table(main_df, jobs_df, countries_df):
    merged_jobs = pd.merge(main_df, jobs_df, on="normalized_job_code")
    merged_countries = pd.merge(merged_jobs, countries_df, on="country_code")
    merged_countries['Quantity'] = 1
    merged_countries['Percentage'] = 1 / len(merged_countries)
    return merged_countries[['Country_Name', 'title', 'gender', 'Quantity', 'Percentage']]

