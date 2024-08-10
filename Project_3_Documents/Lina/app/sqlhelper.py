import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, func
import datetime
import pandas as pd
import numpy as np

# The Purpose of this Class is to separate out any Database logic
class SQLHelper():
    #################################################
    # Database Setup
    #################################################

    # define properties
    def __init__(self):
        self.engine = create_engine("sqlite:///static/Youtubedata.sqlite")
        # self.Base = None

        # automap Base classes
        # self.init_base()

    # COMMENT BACK IN IF USING THE ORM

    # def init_base(self):
    #     # reflect an existing database into a new model
    #     self.Base = automap_base()
    #     # reflect the tables
    #     self.Base.prepare(autoload_with=self.engine)

    #################################################
    # Database Queries
    #################################################

    # USING RAW SQL
    def get_most_subs_channels_by_country(self, country="All"):

        # switch on user_region
        if country == 'All':
            where_clause = "1=1"
        else:
            where_clause = f"country = '{country}'"

        # build the query
        query = f"""
            SELECT Rank, Youtuber, subscribers, country, channel_type
            FROM my_table
            WHERE {where_clause}
            ORDER BY subscribers DESC
            LIMIT 25
            """

        df = pd.read_sql(text(query), con=self.engine)
        data = df.to_dict(orient="records")
        return(data)


    def get_pie(self, youtuber, country):

        # switch on user_region
        if region == 'All':
            where_clause = "and 1=1"
        else:
            where_clause = f"and region = '{country}'"

        # build the query
        query = f"""
            SELECT Rank, Youtuber, subscribers, country, channel_type, category
            FROM my_table
            GROUP BY country 
            ORDER BY channel_type DESC
            LIMIT 25;
             """

        df = pd.read_sql(text(query), con=engine)
        data = df.to_dict(orient="records")
        return(data)


    def get_table(self, video_views, channel_type):

        # switch on user_region
        if region == 'All':
            where_clause = "and 1=1"
        else:
            where_clause = f"and country = '{country}'"

    #     # build the query
    #     query = f"""
    #         SELECT
    #             name,
    #             full_name,
    #             region,
    #             latitude,
    #             longitude,
    #             launch_attempts,
    #             launch_successes,
    #             launch_attempts - launch_successes as launch_failures
    #         FROM
    #             launchpads
    #         WHERE
    #             launch_attempts >= {min_attempts}
    #             {where_clause}
    #         ORDER BY
    #             launch_attempts DESC;
    #     """

    #     df = pd.read_sql(text(query), con = self.engine)
    #     data = df.to_dict(orient="records")
    #     return(data)

    # def get_map(self, min_attempts, region):

    #     # switch on user_region
    #     if region == 'All':
    #         where_clause = "and 1=1"
    #     else:
    #         where_clause = f"and region = '{region}'"

    #     # build the query
    #     query = f"""
    #         SELECT
    #             name,
    #             full_name,
    #             region,
    #             latitude,
    #             longitude,
    #             launch_attempts,
    #             launch_successes,
    #             launch_attempts - launch_successes as launch_failures
    #         FROM
    #             launchpads
    #         WHERE
    #             launch_attempts >= {min_attempts}
    #             {where_clause}
    #         ORDER BY
    #             launch_attempts DESC;
    #     """

    #     df = pd.read_sql(text(query), con = self.engine)
    #     data = df.to_dict(orient="records")
    #     return(data)