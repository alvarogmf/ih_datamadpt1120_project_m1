import argparse
from p_acquisition import m_acquisition as acq
from p_wrangling import m_wrangling as wra
from p_reporting import m_reporting as rep


def argument_parser():
    """
    documentation: parse arguments to script
    """
    parser = argparse.ArgumentParser(description='select country..')
    parser.add_argument("-c","--country",help="Choose a country by full name or choose All",type=str, required=True)
    args = parser.parse_args()
    return args


def main(arguments):
    country_filter = arguments.country
    print('Getting data...')
    main_database = acq.get_database()
    jobs_list = acq.job_ids(main_database)
    jobs_database = acq.get_jobs(jobs_list)
    countries_database = acq.get_countries()

    print('Cleaning data...')
    main_database_clean = wra.db_cleaning(main_database)
    countries_database_clean = wra.countries_clean(countries_database)

    print('Preparing the database')
    final_database = wra.final_table(main_database_clean, jobs_database, countries_database_clean)
    rep.report(final_database, country_filter)

    print('Reporting complete!')


if __name__ == '__main__':
    args = argument_parser()
    main(args)

