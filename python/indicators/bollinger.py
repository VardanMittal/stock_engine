from indicators.base import Indicator
import math

class BollingerUpperBand(Indicator):
    def __init__(self, window: int = 20, num_std: float = 2.0):
        self.window = window
        self.num_std = num_std

    def _sma_and_std(self, prices: list[float]):
        relevant = prices[-self.window:]
        mean = sum(relevant) / len(relevant)
        variance = sum((p - mean) ** 2 for p in relevant) / len(relevant)
        return mean, math.sqrt(variance)

    def calculate(self, prices: list[float]) -> float:
        mean, std = self._sma_and_std(prices)
        return mean + self.num_std * std

    def name(self) -> str:
        return f"BB Upper({self.window})"


class BollingerLowerBand(Indicator):
    def __init__(self, window: int = 20, num_std: float = 2.0):
        self.window = window
        self.num_std = num_std

    def calculate(self, prices: list[float]) -> float:
        relevant = prices[-self.window:]
        mean = sum(relevant) / len(relevant)
        variance = sum((p - mean) ** 2 for p in relevant) / len(relevant)
        std = math.sqrt(variance)
        return mean - self.num_std * std

    def name(self) -> str:
        return f"BB Lower({self.window})"