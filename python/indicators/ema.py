from indicators.base import Indicator

class ExponentialMovingAverage(Indicator):
    def __init__(self, window: int = 5):
        self.window = window
        self.alpha = 2 / (window + 1)

    def calculate(self, prices: list[float]) -> float:
        relevant = prices[-self.window:]
        ema = relevant[0]
        for price in relevant[1:]:
            ema = self.alpha * price + (1 - self.alpha) * ema
        return ema

    def name(self) -> str:
        return f"EMA({self.window})"