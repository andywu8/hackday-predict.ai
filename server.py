from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)
import pandas as pd

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

from main import *
from regression import *


clean_data(car_insurance_df, test_df)
complete_df = pd.concat([car_insurance_df, test_df])


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/generate_heat_map_button_press/')
def generate_heat_map_button_press():
  generate_heat_map(car_insurance_df)
  return render_template('index.html')
  # return(generate_heat_map(car_insurance_df))

    # return 'heat map button press generation'

@app.route('/machine_learning/')
def machine_learning():
  print(return_projected_value())
  return('check terminal for inputs and outputs')


@app.route('/display_data/')
def display_data_button():
    return render_template("data.html", data=complete_df.to_html())
                 


if __name__ == '__main__':
  app.run(debug=True)