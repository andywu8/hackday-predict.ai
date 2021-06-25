import pandas
from sklearn import linear_model
from main import *
import numpy as geek
import tkinter as tk


def return_cleaned_full(car_insurance_df, test_df):
    clean_data(car_insurance_df, test_df)
    complete_df = pd.concat([car_insurance_df, test_df])
    complete_df = complete_df.dropna()
    complete_df['pop_change'] = complete_df['pop_change'].str.rstrip('%').astype('float') / 100.0
    complete_df['percent_change_price_premiums'] = complete_df['percent_change_price_premiums'].str.rstrip('%').astype('float') / 100.0
    complete_df['population'] = complete_df['population'].replace({'/"':''}, regex = True)
    complete_df.replace(',','', regex=True, inplace=True)
    complete_df['population'] = complete_df['population'].astype(float)

    complete_df['death_rate'] = complete_df['death_rate'].astype(float)


    
    return complete_df


def linear_regression(clean_full_df,future_year, future_population, future_median_age, future_premium, inflation_rate_adj, future_death_rate):
    X = clean_full_df[['year', 'population', 'median_age_2021', 'avg_premium_price_2021', 'death_rate']]
    Y = clean_full_df['auto_insurance_expenditure']
    regr = linear_model.LinearRegression()
    regr.fit(X, Y)
    arg_x = [[future_year, future_population, future_median_age, future_premium, future_death_rate]]
    y_pred = regr.predict(arg_x)
    return y_pred * inflation_rate_adj
    # predicted_expenditure = regr.

def return_values_function(complete_df, state, year):
    row = complete_df.loc[(complete_df['state'] == state) & (complete_df['year'] == 2018)]
    # print("row is", row)
    row_2014 = complete_df.loc[(complete_df['state'] == state) & (complete_df['year'] == 2014)]
    # print("row_2014", row_2014)
    change_years = (year - 2021.0)
    future_population  = float(row['population']) * ((1.0+row['pop_change']) ** change_years)
    future_median_age = row['median_age_2021'] + (row['median_age_change'] * change_years)
    future_premium = row['avg_premium_price_2021'] * (row['percent_change_price_premiums'] ** change_years)
    inflation_rate_adj = 1.05 ** change_years

    death_rate_2018 = pd.to_numeric((row['death_rate']),  downcast='float')
    death_rate_2014 = pd.to_numeric((row_2014['death_rate']),  downcast='float')
    death_rate_diff = death_rate_2018 - (death_rate_2014 * 1.0)
    # bug with_death_Rate

    # future_death_rate = row['death_rate'] * ((1.0+change_death_rate) ** change_years)
    # print("future_death_Rate is ", future_death_rate)
    future_death_rate = 11
    return future_population, inflation_rate_adj, future_median_age, future_premium, future_death_rate

def main():
    clean_full_df = return_cleaned_full(car_insurance_df, test_df)


    # print(clean_full_df[(clean_full_df['state'] == 'Alaska')])
    # print(clean_full_df['year'])
    state = input("state you want, first letter must be capitalized and must be spelled correctly \n")
    year = float(input("future year you want(must be past 2021) \n"))
    future_population, inflation_rate_adj, future_median_age, future_premium, future_death_rate = return_values_function(clean_full_df, state, float(year))
    # print("alaska in 2025" , linear_regression(clean_full_df,year, future_population, future_median_age, future_premium, inflation_rate_adj))
    return (linear_regression(clean_full_df,year, future_population, future_median_age, future_premium, inflation_rate_adj, future_death_rate))



def return_projected_value():
    clean_full_df = return_cleaned_full(car_insurance_df, test_df)
    # print(clean_full_df[(clean_full_df['state'] == 'Alaska')])
    # print(clean_full_df['year'])
    state = input("state you want, first letter must be capitalized and must be spelled correctly")
    year = float(input("future year you want(must be past 2021)"))
    future_population, inflation_rate_adj, future_median_age, future_premium, future_death_rate = return_values_function(clean_full_df, state, float(year))
    # print("alaska in 2025" , linear_regression(clean_full_df,year, future_population, future_median_age, future_premium, inflation_rate_adj))
    result = linear_regression(clean_full_df,year, future_population, future_median_age, future_premium, inflation_rate_adj, future_death_rate)
    return result
if __name__ == "__main__":
    main()