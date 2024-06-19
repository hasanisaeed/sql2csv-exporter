from db_exporter.config import DB_CONFIG
from db_exporter.postgres import PostgresDatabase
from db_exporter.exporter import Exporter


def main():
    db = PostgresDatabase(
        host=DB_CONFIG['host'],
        database=DB_CONFIG['database'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password']
    )
    db.connect()

    exporter = Exporter(db)
    exporter.export_all_tables(output_dir='output')


if __name__ == "__main__":
    main()
