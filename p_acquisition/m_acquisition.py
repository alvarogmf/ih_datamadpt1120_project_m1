import pandas as pd
from sqlalchemy import create_engine
import json
import requests


def get_database():
    # connecting to the main database
    print('connecting to the database...')
    db_path = '../data/raw_data_project_m1.db'
    conn_str = f'sqlite:///{db_path}'
    engine = create_engine(conn_str)
    print('connected!')
    return engine


def get_api():
    # connecting to the jobs uuid API
    print('connecting to the API')
    response = requests.get('http://api.dataatwork.org/v1/jobs')
    results = response.json()
    jobs = pd.DataFrame(results)
    print('API connected!')
    return jobs


