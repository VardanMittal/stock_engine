from ingestion.data_source import DataSource

class CSVDataSource(DataSource):

    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_raw_data(self) -> str:
        with open(self.filepath, "r") as f:
            return f.read()

    def describe(self) -> str:
        return f"CSV file:{self.filepath}"