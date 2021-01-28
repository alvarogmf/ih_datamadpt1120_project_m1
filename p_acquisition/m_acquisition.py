import pandas as pd
from sqlalchemy import create_engine
import json
import requests
from functools import reduce


def get_database():
    """
    Function to connect to the database.
    The file must be called raw_data_project_m1.db and has to be in the data folder.
    """
    print('connecting to the database...')
    db_path = 'data/raw_data_project_m1.db'
    conn_str = f'sqlite:///{db_path}'
    engine = create_engine(conn_str)
    table_names = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", engine)
    tables_names_lst = table_names['name'].to_list()
    all_dfs = [pd.read_sql_query(f'select * from {i}', engine) for i in tables_names_lst]
    merged_tables = reduce(lambda left, right: pd.merge(left, right, on='uuid'), all_dfs)
    print('connected!')
    return merged_tables


def job_ids(merged_tables):
    """
    This function is used to extract the list of all the jobs from the main DB.
    """
    jobs_ids = list(merged_tables['normalized_job_code'].unique())
    print('Import finsihed :)')
    return jobs_ids


def get_jobs(jobs_id):
    """
    This functions connects to the API and
    extracts in a DF all the names of the Jobs listed in the function above.
    """
    print('Calling the api...')
    jobs_list = []
    for id in jobs_id:
        if id is None:
            pass
        else:
            api_url = requests.get(f'http://api.dataatwork.org/v1/jobs/{id}')
            json_data = api_url.json()
            jobs_list.append(json_data)
    jobs_df_raw = pd.DataFrame(jobs_list)
    jobs_df = jobs_df_raw.rename(columns={'uuid': "normalized_job_code"})
    print('API connection completed!')
    return jobs_df


def get_countries():
    """
    Function WIP. Functional but needs to be improved.
    It retrieves the countries with their codes from the web scrapper.
    """
    print('connecting to the countries web...')
    url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    table_0 = pd.read_html(url)[0]
    table_1 = pd.read_html(url)[1]
    table_2 = pd.read_html(url)[2]
    table_3 = pd.read_html(url)[3]
    table_4 = pd.read_html(url)[4]
    table_5 = pd.read_html(url)[5]
    table_6 = pd.read_html(url)[6]
    table_7 = pd.read_html(url)[7]
    table_8 = pd.read_html(url)[8]

    countries_table = pd.concat([table_0, table_1, table_2, table_3, table_4, table_5, table_6, table_7, table_8])

    country_names = countries_table[0].append(countries_table[2]).append(countries_table[4]).append(
        countries_table[6]).append(countries_table[9]).reset_index(drop=True)
    country_ids = countries_table[1].append(countries_table[3]).append(countries_table[5]).append(
        countries_table[7]).append(countries_table[10]).reset_index(drop=True)

    full_countries_list = pd.DataFrame({'Country_Name': country_names, 'country_code': country_ids})
    print('countries retrieved!')

    return full_countries_list

