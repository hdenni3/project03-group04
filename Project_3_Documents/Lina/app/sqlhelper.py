from sqlalchemy import create_engine, text
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pandas as pd
import numpy as np

class SQLHelper:
    def __init__(self, database_url='sqlite:///Youtubedata.sqlite'):
        # Create an engine
        self.engine = create_engine(database_url)
        # Initialize base for ORM
        self.Base = automap_base()
        self.Base.prepare(self.engine, reflect=True)
        # Set up a session
        self.session = Session(self.engine)

    def get_data_from_db(self, param):
        # Use SQLAlchemy to create a query
        query = text("SELECT title, video_views FROM my_table WHERE category = :category")
        with self.engine.connect() as conn:
            result = conn.execute(query, {'category': param})
            data = result.fetchall()
        return data

    def get_top_subscribers(self):
        # Example of a more complex query
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
import sqlite3

class SQLHelper:
    def __init__(self, db_path='database.sqlite'):
        """Initialize the helper with the path to the SQLite database."""
        self.db_path = db_path

    def get_db_connection(self):
        """Create and return a database connection."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Allows dictionary-like row access
        return conn

    def execute_query(self, query, params=()):
        """
        Execute a query and return the results as a list of dictionaries.
        :param query: SQL query to be executed.
        :param params: Optional parameters to pass into the query.
        :return: A list of dictionaries containing the query results.
        """
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [dict(row) for row in rows]

    def execute_update(self, query, params=()):
        """
        Execute an update query (INSERT, UPDATE, DELETE).
        :param query: SQL query to be executed.
        :param params: Optional parameters to pass into the query.
        :return: The number of affected rows.
        """
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows

    def get_top_channels_by_views(self, limit=25):
        """
        Retrieve the top channels by video views.
        :param limit: Number of top channels to return.
        :return: A list of dictionaries containing the top channels by video views.
        """
        query = """
        SELECT Youtuber, "video views"
        FROM youtube_data
        ORDER BY "video views" DESC
        LIMIT ?;
        """
        return self.execute_query(query, (limit,))

    def get_top_channels_by_subscribers(self, limit=25):
        """
        Retrieve the top channels by subscribers.
        :param limit: Number of top channels to return.
        :return: A list of dictionaries containing the top channels by subscribers.
        """
        query = """
        SELECT Youtuber, subscribers
        FROM youtube_data
        ORDER BY subscribers DESC
        LIMIT ?;
        """
        return self.execute_query(query, (limit,))
