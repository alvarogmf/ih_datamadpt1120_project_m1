import pandas as pd


def main_table(engine):

    table_query = """SELECT country_info.country_code, 
career_info.normalized_job_code, 
personal_info.gender AS 'Gender',
count(country_info.uuid) AS 'Quantity'
FROM country_info
JOIN career_info ON career_info.uuid = country_info.uuid
JOIN personal_info ON personal_info.uuid = country_info.uuid
GROUP BY country_info.country_code"""

    table = pd.read_sql_query(table_query, engine)
    return table
