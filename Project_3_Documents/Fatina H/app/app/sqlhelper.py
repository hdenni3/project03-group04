import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text

class SQLHelper:
    """Helper class to encapsulate database logic."""

    def __init__(self):
        """Initialize the SQLHelper with a database engine."""
        self.engine = create_engine("sqlite:///static/Youtubedata.sqlite")

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
        query = "SELECT DISTINCT country FROM my_table"
        df = pd.read_sql(text(query), con=self.engine)
        return df.to_dict(orient="records")

    def get_categories(self):
        """Retrieve a list of distinct categories."""
        query = "SELECT DISTINCT category FROM my_table"
        df = pd.read_sql(text(query), con=self.engine)
        return df.to_dict(orient="records")
