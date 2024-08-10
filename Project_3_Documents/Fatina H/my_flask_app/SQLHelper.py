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

    # Add more methods as needed for your specific queries

