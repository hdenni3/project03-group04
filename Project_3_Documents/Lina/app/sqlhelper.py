import sqlalchemy
from sqlalchemy import create_engine, text
import pandas as pd

class SQLHelper:
    #################################################
    # Database Setup
    #################################################

    def __init__(self):
        # Create an engine to connect to the SQLite database
        self.engine = create_engine("sqlite:///static/Youtubedata.sqlite")

    #################################################
    # Database Queries
    #################################################

    def get_map(self, category, country):
        """Retrieve map data based on category and country."""
        category_clause = "1=1" if category == 'All' else f"category = '{category}'"
        country_clause = "1=1" if country == 'All' else f"country = '{country}'"

        query = f"""
            SELECT youtuber, channel_type, subscribers, latitude, longitude
            FROM my_table
            WHERE {category_clause} AND {country_clause}
            """
        df = pd.read_sql(text(query), con=self.engine)
        return df.to_dict(orient="records")

    def get_top_channels(self, country="All"):
        """Retrieve the most subscribed channels by country."""
        where_clause = "1=1" if country == 'All' else f"country = '{country}'"
        
        query = f"""
            SELECT youtuber, subscribers, country, channel_type, category, video_views
            FROM my_table
            WHERE {where_clause}
            ORDER BY subscribers DESC
            LIMIT 25
        """
        df = pd.read_sql(text(query), con=self.engine)
        return df.to_dict(orient="records")

    def get_countries(self):
        """Retrieve a list of distinct countries."""
        query = "SELECT DISTINCT country FROM my_table ORDER BY country"
        df = pd.read_sql(text(query), con=self.engine)
        return df['country'].tolist()

    def get_categories(self):
        """Retrieve a list of distinct categories."""
        query = "SELECT DISTINCT category FROM my_table"
        df = pd.read_sql(text(query), con=self.engine)
        return df['category'].tolist()
