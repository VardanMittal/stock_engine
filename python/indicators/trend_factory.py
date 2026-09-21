from indicators.factory_interface import IndicatorFactory
from indicators.sma import SimpleMovingAverage
from indicators.ema import ExponentialMovingAverage

class TrendIndicatorFactory(IndicatorFactory):
    """Produces the trend-following family: SMA as primary,
    EMA as the faster-reacting secondary."""

    def create_primary(self) -> SimpleMovingAverage:
        return SimpleMovingAverage(window=10)

    def create_secondary(self) -> ExponentialMovingAverage:
        return ExponentialMovingAverage(window=5)