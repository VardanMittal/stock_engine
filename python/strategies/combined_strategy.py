from strategies.interfaces import Predictable
from indicators.factory_interface import IndicatorFactory

class CombinedIndicatorStrategy(Predictable):
    """Combines a trend signal and a momentum signal from whichever
    IndicatorFactory it's given. Doesn't know or care if that factory
    produces SMA/EMA or something else entirely."""

    def __init__(self, trend_factory: IndicatorFactory, momentum_factory: IndicatorFactory):
        self.trend_primary = trend_factory.create_primary()      # e.g. SMA
        self.trend_secondary = trend_factory.create_secondary()  # e.g. EMA
        self.momentum_primary = momentum_factory.create_primary()  # e.g. RSI

    def predict(self, prices: list[float]) -> str:
        if len(prices) < 15:  # RSI(14) needs enough history
            return "hold"

        trend_up = self.trend_secondary.calculate(prices) > self.trend_primary.calculate(prices)
        rsi_value = self.momentum_primary.calculate(prices)

        if trend_up and rsi_value < 70:
            return "buy"
        elif not trend_up and rsi_value > 30:
            return "sell"
        return "hold"

    def name(self) -> str:
        return "Combined Trend+Momentum"