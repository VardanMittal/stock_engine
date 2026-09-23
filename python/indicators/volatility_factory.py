from indicators.factory_interface import IndicatorFactory
from indicators.bollinger import BollingerUpperBand, BollingerLowerBand

class VolatilityIndicatorFactory(IndicatorFactory):
    """Produces the volatility family: upper band as primary,
    lower band as secondary — always used as a pair."""

    def create_primary(self) -> BollingerUpperBand:
        return BollingerUpperBand(window=10, num_std=2.0)

    def create_secondary(self) -> BollingerLowerBand:
        return BollingerLowerBand(window=10, num_std=2.0)