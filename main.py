import pandas as pd
import plotly.express as px  # Be sure to import express
from IPython.display import display



car_insurance_df = pd.read_csv (r'export_car_dataset.csv')
test_df = pd.read_csv('test_2018.csv')
# print (car_insurance_df)

# did some data cleaning to remove commas, dollar sign from avg_premium_price_2021, then converted it into a float for the continuous color scale

def clean_data(car_insurance_df, train_df):
    car_insurance_df['state'] = car_insurance_df['state'].astype(str)
    car_insurance_df['avg_premium_price_2021'] = car_insurance_df['avg_premium_price_2021'].replace({'\$':''}, regex = True)
    car_insurance_df['avg_premium_price_2021'] = car_insurance_df['avg_premium_price_2021'].replace({',':''}, regex = True)
    car_insurance_df['avg_premium_price_2021'] = car_insurance_df['avg_premium_price_2021'].astype(float)

    car_insurance_df['auto_insurance_expenditure'] = car_insurance_df['auto_insurance_expenditure'].replace({'\$':''}, regex = True)
    car_insurance_df['auto_insurance_expenditure'] = car_insurance_df['auto_insurance_expenditure'].replace({',':''}, regex = True)
    car_insurance_df['auto_insurance_expenditure'] = car_insurance_df['auto_insurance_expenditure'].astype(float)

    car_insurance_df.to_csv("export_car_dataset.csv", index=False)

    test_df['state'] = car_insurance_df['state'].astype(str)
    test_df['avg_premium_price_2021'] = test_df['avg_premium_price_2021'].replace({'\$':''}, regex = True)
    test_df['avg_premium_price_2021'] = test_df['avg_premium_price_2021'].replace({',':''}, regex = True)
    test_df['avg_premium_price_2021'] = test_df['avg_premium_price_2021'].astype(float)

    test_df['auto_insurance_expenditure'] = test_df['auto_insurance_expenditure'].replace({'\$':''}, regex = True)
    test_df['auto_insurance_expenditure'] = test_df['auto_insurance_expenditure'].replace({',':''}, regex = True)
    test_df['auto_insurance_expenditure'] = test_df['auto_insurance_expenditure'].astype(float)

    test_df.to_csv("test_2018.csv", index=False)
def generate_heat_map(car_insurance_df):
    fig = px.choropleth(car_insurance_df,  # Input Pandas DataFrame
                        locations="state_code",  # DataFrame column with locations
                        color="avg_premium_price_2021",  # DataFrame column with color values
                        hover_name="state_code", # DataFrame column hover info
                        locationmode = 'USA-states',
                        color_continuous_scale=px.colors.sequential.Plasma) # Set to plot as US States
    fig.update_layout(
        title_text = 'State Rankings', # Create a Title
        geo_scope='usa',  # Plot only the USA instead of globe
    )
    fig.show()  # Output the plot to the screen

def display_data(complete_df):
    display(complete_df)

def main():
    clean_data(car_insurance_df, test_df)
#     generate_heat_map(car_insurance_df)



if __name__ == "__main__":
    main()