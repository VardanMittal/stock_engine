from indicators.base import Indicator

class SimpleMovingAverage(Indicator):
    def __init__(self, window:int=5):
        self.window = window

    def calculate(self, prices: list[float]) -> float:
        relevant = prices[-self.window:]
        return sum(relevant)/len(relevant)

    def name(self) -> str:
        return f"SMA({self.window})"

