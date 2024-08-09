from flask import Flask, render_template, jsonify, request
from sqlalchemy import create_engine, text
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sql = SQLHelper()

#################################################
# Flask Routes
#################################################

class SQLHelper:
    def __init__(self, database_url='sqlite:///Youtubedata.sqlite'):
        self.engine = create_engine(database_url)
        self.Base = automap_base()
        self.Base.prepare(self.engine, reflect=True)
        self.session = Session(self.engine)

    def get_data_from_db(self, param):
        query = text("SELECT title, video_views FROM my_table WHERE category = :category")
        with self.engine.connect() as conn:
            result = conn.execute(query, {'category': param})
            data = result.fetchall()
        return data

    def get_top_subscribers(self):
        query = text("""
            SELECT Rank, Youtuber, subscribers, country, channel_type
            FROM my_table
            ORDER BY subscribers DESC
            LIMIT 25
        """)
        with self.engine.connect() as conn:
            result = conn.execute(query)
            data = result.fetchall()
        return data

# Initialize SQLHelper
sql_helper = SQLHelper()

# HTML ROUTES
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route('/data', methods=['GET'])
def get_data():
    param = request.args.get('param', '')
    data = sql_helper.get_data_from_db(param)
    json_data = [{'title': row[0], 'video_views': row[1]} for row in data]
    return jsonify(json_data)

@app.route('/top-subscribers', methods=['GET'])
def top_subscribers():
    data = sql_helper.get_top_subscribers()
    json_data = [{'rank': row[0], 'youtuber': row[1], 'subscribers': row[2], 'country': row[3], 'channel_type': row[4]} for row in data]
    return jsonify(json_data)

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

# # SQL Queries
# @app.route("/api/v1.0/get_dashboard/<min_attempts>/<region>")
# def get_dashboard(min_attempts, region):
#     min_attempts = int(min_attempts) # cast to int

#     bar_data = sql.get_bar(min_attempts, region)
#     pie_data = sql.get_pie(min_attempts, region)
#     table_data = sql.get_table(min_attempts, region)

#     data = {
#         "bar_data": bar_data,
#         "pie_data": pie_data,
#         "table_data": table_data
#     }
#     return(jsonify(data))

# @app.route("/api/v1.0/get_map/<min_attempts>/<region>")
# def get_map(min_attempts, region):
#     min_attempts = int(min_attempts) # cast to int
#     map_data = sql.get_map(min_attempts, region)

#     return(jsonify(map_data))


# Run the App
if __name__ == '__main__':
    app.run(debug=True)
