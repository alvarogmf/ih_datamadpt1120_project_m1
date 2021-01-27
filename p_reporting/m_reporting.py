import pandas as pd


def report(dataframe, country):
    """
    This function will create the final report, using the columns required and choosing between a specific Country or All
    """
    if country == 'All':
        reporting = pd.DataFrame(dataframe.groupby(['Country_Name','title', 'gender']).agg({'Quantity':['sum'], 'Percentage':['sum']}).reset_index())
        reporting.to_csv('Output/reporting.csv', index=False)
        print('Converted to CSV!')
    elif (dataframe['Country_Name'] == country).any():
        reporting = pd.DataFrame(dataframe[(dataframe['Country_Name'] == country)].groupby(['Country_Name','title', 'gender']).agg({'Quantity':['sum'], 'Percentage':['sum']}).reset_index())
        reporting.to_csv('Output/reporting.csv', index=False)
        print('Converted to CSV!')
    else:
        print('ERROR: Country selected is not in Database')


#def to_csv(dataframe):
#    """
#    This function will convert the previous DF to a CSV and save it into the Output Folder
#    """
#    dataframe.to_csv('../Output/reporting.csv',index = False)
#    return print('Converted to CSV!')
