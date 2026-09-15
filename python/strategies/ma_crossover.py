from strategies.interfaces import Predictable

class MovingAverageCrossoverStrategy(Predictable):

    def __init__(self, short_window:int=3, long_window:int=5) -> None:
        self.short_window = short_window
        self.long_window = long_window

    def predict(self, prices: list[float]) -> str:
        if len(prices) < self.long_window:
            return "hold"

        short_ma = sum(prices[-self.short_window:])/self.short_window
        long_ma = sum(prices[-self.long_window:]) / self.long_window

        if short_ma > long_ma:
            return "buy"
        elif short_ma < long_ma:
            return "sell"

        return "hold"

    def name(self) -> str:
        return f"ma crossover(Short window:{self.short_window}, Long window:{self.long_window})"