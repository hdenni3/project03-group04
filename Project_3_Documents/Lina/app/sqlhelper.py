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
