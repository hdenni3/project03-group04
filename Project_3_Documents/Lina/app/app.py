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
    form_country = request.form.get('country', 'All')

    try:
        # Fetch data using SQLHelper
        most_subs_channels_by_country = sqlHelper.get_most_subs_channels_by_country(form_country)
        top_channels_by_subscribers = sqlHelper.get_top_channels_by_subscribers(form_country)
        
        # Prepare data for the template
        data = {
            'most_subs_channels_by_country': most_subs_channels_by_country,
            'top_channels_by_subscribers': top_channels_by_subscribers,
        }
        
        return render_template('dashboard.html', data=data)
    
    except Exception as e:
        # Handle errors gracefully
        return render_template('dashboard.html', data={}, error=str(e))

# Map page route
@app.route('/map')
def map_view():
    return render_template('map.html')

# About page route
@app.route('/about_us')
def about():
    return render_template('about_us.html')

# Execute the App
if __name__ == "__main__":
    app.run(debug=True)
