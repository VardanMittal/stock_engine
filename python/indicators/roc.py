from indicators.base import Indicator

class RateOfChange(Indicator):
    """Momentum indicator: % change over N periods."""

    def __init__(self, window: int = 5):
        self.window = window

    def calculate(self, prices: list[float]) -> float:
        if len(prices) <= self.window:
            return 0.0
        past_price = prices[-self.window - 1]
        current_price = prices[-1]
        return (current_price - past_price) / past_price * 100

    def name(self) -> str:
        return f"ROC({self.window})"