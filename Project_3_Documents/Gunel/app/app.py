import os
from flask import Flask, render_template, request, jsonify
from sqlhelper import SQLHelper

# Set the working directory to the location of this file
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Flask setup
app = Flask(__name__)
sql_helper = SQLHelper()

# Home page route
@app.route('/')
def main():
    return render_template('main.html')


# Dashboard page route
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    selected_country = request.form.get('country', 'All')
    
    data = {
        'countries': sql_helper.get_countries(),
        'top_channels': sql_helper.get_top_channels(),
        'top_channels_by_country': sql_helper.get_top_channels(selected_country),
    }
    
    return render_template('dashboard.html', data=data)


# Map page route
@app.route('/map')
def map_view():
    data = {
        'countries': sql_helper.get_countries(),
        'categories': sql_helper.get_categories(),
    }
    
    return render_template('map.html', data=data)


# About page route
@app.route('/about_us')
def about():
    return render_template('about_us.html')


# API route to get map data based on category and country
@app.route('/api/v1.0/get_map/<string:category>/<string:country>')
def get_map(category, country):
    map_data = sql_helper.get_map(category, country)
    return jsonify(map_data)


# API route to get top channels data based on country
@app.route('/api/v1.0/get_data/<string:country>')
def get_data(country):
    top_channels_by_country = sql_helper.get_top_channels(country)
    return jsonify(top_channels_by_country)


# Execute the app
if __name__ == '__main__':
    app.run(debug=True)
