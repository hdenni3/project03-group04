from flask import Flask, render_template, request, jsonify
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.io as pio
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from sqlhelper import SQLHelper

#################################################
# Flask Setup 
app = Flask(__name__)
sqlHelper = SQLHelper()
################################################# 

# Home page route
@app.route('/')
def main():
    return render_template('main.html')

# Dashboard page route
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # if request.method == 'POST':
    # Handle POST request data (e.g., form submission)
    form_country = request.form.get('country', 'All')
    most_subs_channels_by_country = sqlHelper.get_most_subs_channels_by_country(form_country)
    # query2_results
    # query3_results
    data = {
        'most_subs_channels_by_country': most_subs_channels_by_country,
        # query2

    }
    # Assuming `result` is a DataFrame, pass it to the template
    return render_template('dashboard.html', data=data)

# Map page route
@app.route('/map')
def map_view():
    return render_template('map.html')

# About page route
@app.route('/about_us')
def about():
    return render_template('about_us.html')

# SQL Queries
@app.route("/api/v1.0/get_dashboard/<min_attempts>/<region>")
def get_dashboard(min_attempts, country):
    min_attempts = int(min_attempts) # cast to int

    bar_data = sql.get_bar(min_attempts, country)
    pie_data = sql.get_pie(min_attempts, country)
    table_data = sql.get_table(min_attempts, country)

    data = {
        "bar_data": bar_data,
        "pie_data": pie_data,
        "table_data": table_data
    }
    return(jsonify(data))

@app.route("/api/v1.0/get_map/<min_attempts>/<country>")
def get_map(min_attempts, country):
    min_attempts = int(min_attempts) # cast to int
    map_data = sql.get_map(min_attempts, country)

    return(jsonify(map_data))




#################################################
# Execute the App
#################################################
if __name__ == "__main__":
    app.run(debug=True)
