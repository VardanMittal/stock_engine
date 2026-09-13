from indicators.base import Indicator

class RSI(Indicator):
    def __init__(self, window: int = 14):
        self.window = window

    def calculate(self, prices: list[float]) -> float:
        relevant = prices[-self.window - 1:]
        gains, losses = [], []
        for i in range(1, len(relevant)):
            change = relevant[i] - relevant[i - 1]
            (gains if change > 0 else losses).append(abs(change))

        avg_gain = sum(gains) / self.window if gains else 0
        avg_loss = sum(losses) / self.window if losses else 0

        if avg_loss == 0:
            return 100.0
        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))

    def name(self) -> str:
        return f"RSI({self.window})"