from engine_bridge.interface import BacktestEngine

class AnalysisEngine:
    """High-level orchestrator. Depends only on the BacktestEngine
    abstraction — doesn't know or care if it's backed by Python,
    C++, or a test mock."""

    def __init__(self, engine: BacktestEngine):
        self.engine = engine

    def analyze(self, prices: list[float], strategy) -> dict:
        signals = [strategy.predict(prices[:i+1]) for i in range(len(prices))]
        result = self.engine.run(prices, signals)
        return result