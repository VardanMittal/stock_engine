from indicators.factory_interface import IndicatorFactory
from indicators.rsi import RSI
from indicators.roc import RateOfChange

class MomentumIndicatorFactory(IndicatorFactory):
    """Produces the momentum family: RSI as primary,
    Rate of Change as secondary."""

    def create_primary(self) -> RSI:
        return RSI(window=14)

    def create_secondary(self) -> RateOfChange:
        return RateOfChange(window=5)