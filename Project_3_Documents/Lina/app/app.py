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
 
    countries = sqlHelper.get_countries()
    top_channels = sqlHelper.get_top_channels()
    top_channels_by_country = sqlHelper.get_top_channels(form_country)
 
    data = {
        'countries': countries,
        'top_channels': top_channels,
        'top_channels_by_country': top_channels_by_country
    }
    
    return render_template('dashboard.html', data=data)

# Map page route
@app.route('/map')
def map_view():
    countries = sqlHelper.get_countries()
    categories = sqlHelper.get_categories()
    
    data = {
        'countries': countries,
        'categories': categories
    }
    
    return render_template('map.html', data=data)

@app.route("/api/v1.0/get_map/<string:category>/<string:country>")
def get_map(category, country):
    map_data = sqlHelper.get_map(category, country)
    return jsonify(map_data)


# About page route
@app.route('/about_us')
def about():
    return render_template('about_us.html')

# Execute the App
if __name__ == "__main__":
    app.run(debug=True)