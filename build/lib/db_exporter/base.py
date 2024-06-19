class BaseDatabase:
    def connect(self):
        raise NotImplementedError

    def get_tables(self):
        raise NotImplementedError

    def export_table_to_csv(self, table_name, output_dir):
        raise NotImplementedError
