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
from indicators.trend_factory import TrendIndicatorFactory
from indicators.momentum_factory import MomentumIndicatorFactory
from strategies.combined_strategy import CombinedIndicatorStrategy
from indicators.volatility_factory import VolatilityIndicatorFactory
from portfolio.backtest_config_builder import BacktestConfigBuilder

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
    data = get_stock_data("yfinance", ticker="RELIANCE.NS", period="3mo")
    valid_data = [
    row for row in data
    if row.get("close", "").strip()
    ]
    closes = [float(row["close"]) for row in valid_data]

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

    combined_strategy = CombinedIndicatorStrategy(
        trend_factory=TrendIndicatorFactory(),
        momentum_factory=MomentumIndicatorFactory()
    )

    strategies = [
        MovingAverageCrossoverStrategy(short_window=2, long_window=3),
        ThresholdStrategy(),
        LSTMStrategy(),
        combined_strategy,
        ]
    for strategy in strategies:
        print(f"{strategy.name()}: {strategy.predict(closes)}")

    for factory in [TrendIndicatorFactory(), MomentumIndicatorFactory(), VolatilityIndicatorFactory()]:
        primary = factory.create_primary()
        secondary = factory.create_secondary()
        print(f"{type(factory).__name__}: {primary.name()}={primary.calculate(closes):.2f}, "
              f"{secondary.name()}={secondary.calculate(closes):.2f}")
    config_obj = (
        BacktestConfigBuilder()
        .with_date_range("2026-08-01", "2026-09-01")
        .with_strategy("ma_crossover")
        .with_capital(15000.0)
        .build()
    )
    print(config_obj)

    # test the validation guard - required fields missing
    try:
        bad_config = BacktestConfigBuilder().with_capital(5000).build()
    except ValueError as e:
        print(f"Caught expected error: {e}")