from engine_bridge.stub_engine import StubEngine
from engine_bridge.cpp_engine import CppEngine
from engine_bridge.analysis_engine import AnalysisEngine
from strategies.ma_crossover import MovingAverageCrossoverStrategy
from portfolio.backtest_config_builder import BacktestConfigBuilder

prices = [100, 102, 101, 105, 103, 104, 106, 102, 108, 110]
strategy = MovingAverageCrossoverStrategy(short_window=2, long_window=4)
config = (BacktestConfigBuilder()
    .with_date_range("2026-08-01", "2026-09-01")
    .with_strategy("ma_crossover")
    .with_capital(10000.0)
    .with_fee(0.001)
    .build())

for name, engine in [("StubEngine", StubEngine()), ("CppEngine", CppEngine())]:
    analysis = AnalysisEngine(engine)
    result = analysis.analyze(prices, strategy, config)
    print(f"{name}: {result}")