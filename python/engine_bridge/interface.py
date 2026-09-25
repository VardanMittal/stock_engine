from abc import ABC, abstractmethod
from portfolio.backtest_config import BacktestConfig

class BacktestEngine(ABC):
    """Abstract contract for any backtesting engine — C++-backed,
    Python-only, or a test double. High-level code depends on this,
    never on a concrete engine class."""

    @abstractmethod
    def run(self, prices: list[float], signals: list[str], config:BacktestConfig) -> dict:
        """Runs a backtest given prices and buy/sell/hold signals.
        Returns a result dict, e.g. {"final_value": ..., "trades": ...}."""
        pass