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

    def get_top_channels_by_subscribers(self, country="All"):
        """
        Retrieves the top 25 YouTube channels by subscribers, optionally filtered by country.
        :param country: Optional country to filter the results.
        :return: List of dictionaries with the query results.
        """
        # Build the WHERE clause
        if country == 'All':
            where_clause = "1=1"
        else:
            where_clause = f"country = '{country}'"

        # Define the query
        query = f"""
        SELECT Rank, Youtuber, subscribers, country, channel_type
        FROM my_table
        WHERE {where_clause}
        ORDER BY subscribers DESC
        LIMIT 25
        """

        # Execute the query and fetch results into a DataFrame
        df = pd.read_sql(text(query), con=self.engine)
        # Convert DataFrame to a list of dictionaries
        data = df.to_dict(orient="records")
        return data

    def get_most_subs_channels_by_country(self, country="All"):
        """
        Retrieves the top 25 YouTube channels by subscribers, optionally filtered by country.
        :param country: Optional country to filter the results.
        :return: List of dictionaries with the query results.
        """
        # Build the WHERE clause
        if country == 'All':
            where_clause = "1=1"
        else:
            where_clause = f"country = '{country}'"

        # Define the query
        query = f"""
        SELECT Rank, Youtuber, subscribers, country, channel_type
        FROM my_table
        WHERE {where_clause}
        ORDER BY subscribers DESC
        LIMIT 25
        """

        # Execute the query and fetch results into a DataFrame
        df = pd.read_sql(text(query), con=self.engine)
        # Convert DataFrame to a list of dictionaries
        data = df.to_dict(orient="records")
        return data
