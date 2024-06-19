try:
    import psycopg2
except ImportError as e:
    raise ImportError(
        "psycopg2 is required for PostgreSQL support. Please install it using 'pip install db_exporter[postgres]'") from e

import pandas as pd
from .base import BaseDatabase


class PostgresDatabase(BaseDatabase):
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def get_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema='public'
        """)
        tables = cursor.fetchall()
        return [table[0] for table in tables]

    def export_table_to_csv(self, table_name, output_dir):
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, self.connection)
        if 'id' in df.columns:
            df.rename(columns={'id': f'{table_name}_id'}, inplace=True)
        csv_file_path = f"{output_dir}/{table_name}.csv"
        df.to_csv(csv_file_path, index=False)
