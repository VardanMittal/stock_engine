import requests
from ingestion.data_source import DataSource

class APIDataSource(DataSource):
    def __init__(self, url: str):
        self.url = url

    def get_raw_data(self) -> str:
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text

    def describe(self) -> str:
        return f"API endpoint: {self.url}"