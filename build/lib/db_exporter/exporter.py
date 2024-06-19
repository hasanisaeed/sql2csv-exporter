import os
from .postgres import PostgresDatabase


class Exporter:
    def __init__(self, db_instance):
        self.db_instance = db_instance

    def export_all_tables(self, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        tables = self.db_instance.get_tables()
        for table in tables:
            self.db_instance.export_table_to_csv(table, output_dir)
