import requests

class DataFetcher:
    """Responsible only to retreive raw data."""
    def fetch_from_api(self, url: str) -> str:
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def fetch_from_csv(self,filepath:str) -> str:
        with open(filepath, 'r') as file:
            return file.read()
    