from flask import Flask, render_template, request, jsonify
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.io as pio
from SQLHelper import SQLHelper

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('database.sqlite')
    conn.row_factory = sqlite3.Row
    return conn

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

# Dashboard page route
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    conn = get_db_connection()
    
    # Default query for top 25 channels by video views
    query_top_views = """
    SELECT Youtuber, "video views"
    FROM youtube_data
    ORDER BY "video views" DESC
    LIMIT 25;
    """
    
    if request.method == 'POST':
        category = request.form.get('category', 'All')
        if category != 'All':
            query_top_views = f"""
            SELECT Youtuber, "video views"
            FROM youtube_data
            WHERE category = ?
            ORDER BY "video views" DESC
            LIMIT 25;
            """
            top_views = pd.read_sql_query(query_top_views, conn, params=(category,))
        else:
            top_views = pd.read_sql_query(query_top_views, conn)
    else:
        top_views = pd.read_sql_query(query_top_views, conn)
    
    # Convert DataFrame to JSON for Plotly
    top_views_json = top_views.to_json(orient='records')

    # Generate Plotly figure
    fig = px.bar(top_views, x='Youtuber', y='video views', title='Top 25 YouTube Channels by Video Views')
    graphJSON = pio.to_json(fig)

    conn.close()
    return render_template('dashboard.html', graphJSON=graphJSON, top_views_json=top_views_json)

# Map page route
@app.route('/map')
def map_view():
    return render_template('map.html')

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Works Cited page route
@app.route('/works_cited')
def works_cited():
    return render_template('works_cited.html')

# API endpoint for earnings estimates
@app.route('/api/earnings', methods=['GET'])
def api_earnings():
    conn = get_db_connection()
    query_earnings = """
    SELECT Youtuber, lowest_monthly_earnings, highest_monthly_earnings, lowest_yearly_earnings, highest_yearly_earnings
    FROM youtube_data
    ORDER BY highest_yearly_earnings DESC
    LIMIT 25;
    """
    earnings_data = pd.read_sql_query(query_earnings, conn)
    conn.close()
    return jsonify(earnings_data.to_dict(orient='records'))

# API endpoint for country comparisons
@app.route('/api/country_comparisons', methods=['GET'])
def api_country_comparisons():
    conn = get_db_connection()
    query_country_comparisons = """
    SELECT Country, AVG(subscribers) AS avg_subscribers, AVG("video views") AS avg_views
    FROM youtube_data
    GROUP BY Country;
    """
    country_comparisons = pd.read_sql_query(query_country_comparisons, conn)
    conn.close()
    return jsonify(country_comparisons.to_dict(orient='records'))

# API endpoint for educational impact
@app.route('/api/education_impact', methods=['GET'])
def api_education_impact():
    conn = get_db_connection()
    query_education_impact = """
    SELECT Country, AVG("Gross tertiary education enrollment (%)") AS avg_education, AVG(subscribers) AS avg_subscribers
    FROM youtube_data
    GROUP BY Country;
    """
    education_impact = pd.read_sql_query(query_education_impact, conn)
    conn.close()
    return jsonify(education_impact.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)


db_helper = SQLHelper()

@app.route('/top_channels')
def top_channels():
    channels = db_helper.get_top_channels_by_views()
    return render_template('top_channels.html', channels=channels)
