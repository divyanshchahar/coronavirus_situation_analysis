# FUNCTION TO CALCULATE AVERAGE CASSES RECORDED (last day cases/ number of days the infections were reported)
# Input Arguments:
#   -   Dataframe with numbers of interest(confirmed cases/deaths/recovered) per day (grouped by country)
# Output Arguments
#   -   Dataframe with country names and average cases
def average_calculator(df):
    countries = df['Country'].values.tolist() # extracting name of the countries
    length_countries = len(countries)
    averagecases = []  # list to hold average cases

    # loop to calculate average cases (total reported cases/days)
    for i in range(0, length_countries):
        df_temp = df.loc[i].values.tolist()  # creating dataframe by country
        length_df_temp = len(df_temp)
        nullcasecount = df_temp.count(0)  # accounting for days with 0 reported cases
        n = int((df_temp[length_df_temp - 1] / (length_df_temp - nullcasecount)))  # performing calculation on last column values
        averagecases.append(n)

    data = {'Country': countries, 'avrg': averagecases}
    df_final = pd.DataFrame(data)

    return df_final


# FUNCTION TO CALCULATE GROWTH RATE
#
# Input Arguments:
#   -   Dataframe with numbers of interest(confirmed cases/deaths/recovered) per day (grouped by country)
# Output Parameters:
#   -   DataFrame with growth rate for each each for all countries
def growthrate_calculator(df):
    countries = df['Country'].values.tolist()  # extracting name of the countries
    dates = df.drop(['Country'], axis=1).columns.values.tolist()  # extracting dates

    length_country = len(countries) # number of countries
    length_dates = len(dates) # number of days

    count = 0
    index_df_final = []  # list to hold dates required after calculation is complete

    # loop to create list of index
    for i in range(1, length_dates):  # first date is skipped as mandated by the formula we are gonna use
        index_df_final.append(dates[i])

    # loop to calculate new cases
    for i in range(0, length_country):  # first loop to select rows by country names
        df_temp = df.loc[i].values.tolist()  # creating dataframe by country (first element of the list will be a country name and not a date)
        length_df_temp = len(df_temp)

        growthrate = [] # list to hold new cases

        for j in range(2, length_df_temp):  # second loop to iterate through columns (going through dates of a country)
            try:
                k = round(int(df_temp[j])/int(df_temp[j-1]), 3)
            except ZeroDivisionError:
                k = 0

            growthrate.append(k)

        if count == 0:
            initial_array = np.array(growthrate)
            count += 1
        else:
            final_array = np.vstack((initial_array, growthrate))
            initial_array = final_array
            count += 1

    df_final = pd.DataFrame(final_array, columns=index_df_final)
    df_final.insert(0, 'Country', countries)

    return df_final


# FUNCTION TO CALCULATE NEW CASES EVERYDAY
#
# Input Arguments:
#   -   Dataframe with numbers of interest(confirmed cases/deaths/recovered) per day (grouped by country)
# Output Parameters:
#   -   DataFrame with new instances of number of interest(confirmed cases/deaths/recovered)
def newinstance_calculator(df):
    countries = df['Country'].values.tolist()  # extracting name of the countries
    dates = df.drop(['Country'], axis=1).columns.values.tolist()  # extracting dates

    length_countries = len(countries) # number of countries
    length_dates = len(dates) # number of days

    count = 0
    index_df_final = []  # list to hold dates required after calculation is complete

    # loop to create list of index
    for i in range(1, length_dates):  # first date is skipped as mandated by the formula we are gonna use
        index_df_final.append(dates[i])

    # loop to calculate new cases
    for i in range(0, length_countries):  # first loop to select rows by country names
        df_temp = df.loc[i].values.tolist()  # creating dataframe by country (first element of the list will be a country name and not a date)
        length_df_temp = len(df_temp)

        newinstance = [] # list to hold new cases

        for j in range(2, length_df_temp):  # second loop to iterate through columns (going through dates of a country)
            k = int(df_temp[j]) - int(df_temp[j-1])
            newinstance.append(k)

        if count == 0:
            initial_array = np.array(newinstance)
            count += 1
        else:
            final_array = np.vstack((initial_array, newinstance))
            initial_array = final_array
            count += 1

    df_final = pd.DataFrame(final_array, columns=index_df_final)
    df_final.insert(0, 'Country', countries)

    return df_final


# FUNCTION TO CALCULATE MOVING AVERAGE
# Input Parameters:
#   -   Dataframe with numbers of interest(confirmed cases/deaths/recovered) per day (grouped by country)
# Output Parameters:
#   -   Dataframe with progression of number of interst(confirmed cases/deaths/recovered)
def cummulativeaverage_calculator(df):
    t = 7 # time period for mooving averages
    countries = df['Country'].values.tolist()  # extracting name of the countries
    dates = df.drop(['Country'], axis=1).columns.values.tolist()  # extracting dates

    length_countries = len(countries) # number of countries
    length_dates = len(dates) # number of days

    count = 0

    list_starting = []  # list to record the position of first non-zero entry

    # loop to calculate mooving average
    for i in range(0, length_countries):  # first loop to select rows by country names
        df_temp = df.loc[i].values.tolist()  # creating dataframe by country (first element of the list will be a country name and not a date)
        length_df_temp = len(df_temp)
        movingaverage = []

        firstzero = True

        for j in range(1, length_df_temp):  # loop to determine first non-zero entry of tthe country
            if df_temp[j] > 0:  # checking for non-zero values
                list_starting.append(j)
                firstzero = False
                break
            if (firstzero == True) & (j == length_df_temp-1):
                list_starting.append(0)

        index_adjustment = int(((t + 1) / 2) - 1)  # index margin due to time period t
        index_starting = int(list_starting[i] + index_adjustment)  # first positin of mooving average
        index_ending = int(length_df_temp - index_adjustment)  # last positin of mooving average

        for j in range(1, length_df_temp):  # loop to iterate through dates

            if (j >= index_starting + 1) & (j <= index_ending-1):  # calculation of moving average
                sum_value = 0
                for k in range(j - index_adjustment, j + index_adjustment):
                    sum_value = sum_value + df_temp[k]
                    append_status = True
            else:
                append_status = False

            if append_status == True:  # appending value
                k = round(sum_value/t, 5)
            else:
                k = -1

            movingaverage.append(k)

        # operations for preparing database
        if count == 0:
            initial_array = np.array(movingaverage)
            count += 1
        else:
            final_array = np.vstack((initial_array, movingaverage))
            initial_array = final_array
            count += 1

    # operation for databse creation
    df_final = pd.DataFrame(final_array, columns=dates)
    df_final.insert(0, 'Country', countries)

    return df_final


# FUNCTION TO CALCULATE GROWTH RATE
#
# Input Arguments:
#   -   Dataframe with numbers of interest(confirmed cases/deaths/recovered) per day (grouped by country)
# Output Parameters:
#   -   DataFrame with growth ratio for each of the countries [df1/df2]
def ratio_calculator(df1,df2):
    countries = df1['Country'].values.tolist()  # extracting name of the countries
    dates = df1.drop(['Country'], axis=1).columns.values.tolist()  # extracting dates

    length_country = len(countries)  # number of countries
    length_dates = len(dates)  # number of days

    count = 0
    index_df_final = []  # list to hold dates required after calculation is complete

    # loop to create list of index
    for i in range(1, length_dates):  # first date is skipped as mandated by the formula we are gonna use
        index_df_final.append(dates[i])

    # loop to calculate new cases
    for i in range(0, length_country):  # first loop to select rows by country names
        df_temp1= df1.loc[i].values.tolist()  # creating dataframe by country (first element of the list will be a country name and not a date)
        df_temp2= df2.loc[i].values.tolist()  # creating dataframe by country (first element of the list will be a country name and not a date)
        length_df_temp = len(df_temp1)

        ratio = [] # list to hold new cases

        for j in range(2, length_df_temp):  # second loop to iterate through columns (going through dates of a country)
            try:
                k = round(int(df_temp1[j])/int(df_temp2[j]), 3)
            except ZeroDivisionError:
                k = 0

            ratio.append(k)

        if count == 0:
            initial_array = np.array(ratio)
            count += 1
        else:
            final_array = np.vstack((initial_array, ratio))
            initial_array = final_array
            count += 1

    df_final = pd.DataFrame(final_array, columns=index_df_final)
    df_final.insert(0, 'Country', countries)

    return df_final


# MAIN BODY OF THE PROGRAM
# importing libraries
import pandas as pd
import numpy as np


####____________________________________________________ Reading the Databases _________________________________________________________________________###

# Confirmed Casses of Corona Virus (Globally) (Database of John Hopkins University)
df_coronaC_global = pd.read_csv(r'COVID-19-master\COVID-19-master\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_global.csv') # Confirmed Cases of Coronavirus
df_coronaD_global = pd.read_csv(r'COVID-19-master\COVID-19-master\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_deaths_global.csv') # Deaths due to Coronavirus
df_coronaR_global = pd.read_csv(r'COVID-19-master\COVID-19-master\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_recovered_global.csv') # Recoveris from Coronavirus

#_________________________________________________________________________________________________________________________________________________________#


###___________________________________________________Operations on Dataframes___________________________________________________________###

# Confirmed Casses of Corona Virus (Globally)
df_coronaC_global = df_coronaC_global.drop(['Province/State', 'Lat', 'Long'], axis=1)  # dropping unnecessary columns
df_coronaC_global = df_coronaC_global.rename(columns={'Country/Region': 'Country'})  # renaming columns for future use
df_coronaC_global = df_coronaC_global.groupby('Country').sum()  # summing up the values for countries
df_coronaC_global.to_csv('confirmedcases.csv') # writing results to a file to be read later
df_coronaC_global = pd.read_csv('confirmedcases.csv') # recreating the dataset (nullifying the effects of groupby objects)

# Deaths due to Corona Virus (Globally)
df_coronaD_global = df_coronaD_global.drop(['Province/State', 'Lat', 'Long'], axis=1)  # dropping unnecessary columns
df_coronaD_global = df_coronaD_global.rename(columns={'Country/Region': 'Country'})  # renaming columns for future use
df_coronaD_global = df_coronaD_global.groupby('Country').sum()  # summing up the values for countries
df_coronaD_global.to_csv('deaths.csv')  # writing results to a file to be read later
df_coronaD_global = pd.read_csv('deaths.csv')  # recreating the dataset (nullifying the effects of groupby objects)

# Recoveries from Coronavirus Globally)
df_coronaR_global = df_coronaR_global.drop(['Province/State', 'Lat', 'Long'], axis=1)  # dropping unnecessary columns
df_coronaR_global = df_coronaR_global.rename(columns={'Country/Region': 'Country'})  # renaming columns for future use
df_coronaR_global = df_coronaR_global.groupby('Country').sum()  # summing up the values for countries
df_coronaR_global.to_csv('recovered.csv')  # writing results to a file to be read later
df_coronaR_global = pd.read_csv('recovered.csv')  # recreating the dataset (nullifying the effects of groupby objects)

#____________________________________________________________________________________________________________________________________________#


###________________________________________________________________Calculations on Dataset _______________________________________________________________________###

df_newcases = newinstance_calculator(df_coronaC_global)  # New Cases of Coronavirus (for calculation of Moving Average of Growth Rate)
df_growthrate = growthrate_calculator(df_newcases)  # growth Rate of confirmed cases (for calculation of Moving Average of Growth Rate) [Not written to file]
df_growthrate_movingaverage = cummulativeaverage_calculator(df_growthrate)  # Moving Average of Growth Rate of Confirmed Cases
df_deaths_average = average_calculator(df_coronaD_global)  # Average Deaths
df_recovered_average = average_calculator(df_coronaR_global)  # Average Recovered
df_mortalityfactor = ratio_calculator(df_coronaD_global, df_coronaC_global)  # Mortality Factor
df_recoveryratio = ratio_calculator(df_coronaR_global, df_coronaC_global)  # Recovery Ratio
df_mortalityfactor_movingaverage = cummulativeaverage_calculator(df_mortalityfactor)  # Moving Average of Mortality Factor
df_recoveryratio_movingaverage = cummulativeaverage_calculator(df_recoveryratio)  # Moving Average of Recovery Ratio

#___________________________________________________________________________________________________________________________________________________________________#


#______________________________________________________ Wrtiting Data To file_________________________________________________________#

df_newcases.to_csv('newcases.csv', index=False)  # New Cases of Coronavirus
df_growthrate.to_csv('growthrate.csv', index=False)  # Growth Rate
df_growthrate_movingaverage.to_csv('growthrate_movingaverage.csv', index=False)  # Moving Average of Growth Rate of Confirmed Cases
df_deaths_average.to_csv('deaths_average.csv', index=False)  # Average Deaths
df_recovered_average.to_csv('recovered_average.csv', index=False)  # Average Recovered
df_mortalityfactor.to_csv('mortalityfactor.csv', index=False)  # Mortality Factor
df_recoveryratio.to_csv('recoveryratio.csv', index=False)  # Recovery Ratio
df_mortalityfactor_movingaverage.to_csv('mortalityfactor_movingaverage.csv', index=False)  # Moving Average of Mortality Factor
df_recoveryratio_movingaverage.to_csv('recoveryratio_movingaverage.csv', index=False)  # Moving Average of Recovery Ratio

###__________________________________________________________________________________________________________________________________###