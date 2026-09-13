from ingestion.fetcher import DataFetcher
from ingestion.parser import DataParser
from ingestion.cache import DataCache
from indicators.sma import SimpleMovingAverage
from indicators.ema import ExponentialMovingAverage
from indicators.rsi import RSI

def get_stock_data(filepath: str):
    cache = DataCache()
    cached = cache.get(filepath)
    if cached:
        print("Loaded from cache")
        return cached

    fetcher = DataFetcher()
    raw = fetcher.fetch_from_csv(filepath)
    parser = DataParser()
    rows = parser.parse_csv(raw)
    cache.set(filepath, rows)
    return rows

if __name__ == "__main__":
    data = get_stock_data("sample_data.csv")
    closes = [float(row["close"]) for row in data]

    indicators = [
        SimpleMovingAverage(window=3),
        ExponentialMovingAverage(window=3),
        RSI(window=3),
    ]

    for ind in indicators:
        print(f"{ind.name()}: {ind.calculate(closes):.2f}")