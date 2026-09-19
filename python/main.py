from ingestion.parser import DataParser
from ingestion.cache import DataCache
from indicators.sma import SimpleMovingAverage
from indicators.ema import ExponentialMovingAverage
from indicators.rsi import RSI
from strategies.ma_crossover import MovingAverageCrossoverStrategy
from strategies.threshold import ThresholdStrategy
from strategies.lstm_stub import LSTMStrategy
from engine_bridge.analysis_engine import AnalysisEngine
from engine_bridge.stub_engine import StubEngine
from ingestion.factory import DataSourceFactory

from config import Config
from logger import Logger

def get_stock_data(source_type: str, **source_kwargs):
    """source_type and kwargs decide WHICH source, but everything below
    this line is identical no matter what comes in — that's the payoff."""

    cache_key = str(source_kwargs)  # simple cache key for now
    cache = DataCache()
    cached = cache.get(cache_key)

    if cached:
        print("Loaded from cache")
        return cached

    source = DataSourceFactory.create(source_type, **source_kwargs)
    print(f"Fetching from: {source.describe()}")

    raw = source.get_raw_data()
    parser = DataParser()
    rows = parser.parse_csv(raw)

    cache.set(cache_key, rows)
    print(f"Fetched and parsed {len(rows)} rows")
    return rows


if __name__ == "__main__":
    data = get_stock_data("api", url="https://example.com/data.csv")
    closes = [float(row["close"]) for row in data]

    indicators = [
        SimpleMovingAverage(window=3),
        ExponentialMovingAverage(window=3),
        RSI(window=3),
    ]

    for ind in indicators:
        print(f"{ind.name()}: {ind.calculate(closes):.2f}")

    strategies = [
        MovingAverageCrossoverStrategy(short_window=2, long_window=3),
        ThresholdStrategy(),
        LSTMStrategy(),  # untrained — will just return "hold"
    ]

    for strategy in strategies:
        print(f"{strategy.name()}: {strategy.predict(closes)}")

    engine = StubEngine()
    analysis = AnalysisEngine(engine)  # dependency injected here

    strategy = MovingAverageCrossoverStrategy(short_window=2, long_window=3)
    result = analysis.analyze(closes, strategy)
    print(f"Backtest result: {result}")

    config = Config()
    config2 = Config()  # "new" instance, but actually the same object
    print(f"Same instance? {config is config2}")  # True

    logger = Logger()
    logger.log(f"Starting analysis with initial cash: {config.get('initial_cash')}")

    engine = StubEngine()
    analysis = AnalysisEngine(engine)
    strategy = MovingAverageCrossoverStrategy(short_window=2, long_window=3)
    result = analysis.analyze(closes, strategy)

    logger.log(f"Backtest result: {result}")

    # source = DataSourceFactory.create("csv", filepath="sample_data.csv")
    # print(source.describe())
    # raw = source.get_raw_data()
    # print(f"Got {len(raw)} characters of raw data")