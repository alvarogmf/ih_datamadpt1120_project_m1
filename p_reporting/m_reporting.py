import pandas as pd


def report(dataframe, country):
    if country.lower() == 'all':
        reporting = pd.DataFrame(dataframe.groupby(['Country_Name','title', 'gender']).agg({'Quantity':['sum'], 'Percentage':['sum']}).reset_index())
        return reporting
    elif (dataframe['Country_Name'] == country.capitalize()).any():
        reporting = pd.DataFrame(dataframe[(dataframe['Country_Name'] == country)].groupby(['Country_Name','title', 'gender']).agg({'Quantity':['sum'], 'Percentage':['sum']}).reset_index())
        return reporting
    else:
        print('ERROR: Country selected is not in Database')


def to_csv(dataframe):
    dataframe.to_csv('../Output/reporting.csv',index = False)
    return print('Converted to CSV!')
