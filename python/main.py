from ingestion.fetcher import DataFetcher
from ingestion.cache import DataCache
from ingestion.parser import DataParser

def get_stock_data(filepath:str):
    cache = DataCache()
    cached = cache.get(filepath)

    if  cached:
        print("Load from the cache")
        return cached

    fetcher = DataFetcher()
    raw = fetcher.fetch_from_csv(filepath)

    parser = DataParser()
    rows = parser.parse_csv(raw)

    cache.set(filepath, rows)

    print(f"Fetched and parsed {len(rows)} rows")
    return rows


if __name__ == "__main__":
    data = get_stock_data("sample_data.csv")
    print(data[:3])