from strategies.interfaces import Predictable
class ThresholdStrategy(Predictable):
    """
    Naive strategy: buy if price rose >1% 
    since last close, sell if it fell >1%.
     """

    def predict(self, prices: list[float]) -> str:
        if len(prices) < 2:
            return "hold"

        change_pct = (prices[-1] - prices[-2]) / prices[-2] * 100
        if change_pct > 1:
            return "buy"
        elif change_pct < -1:
            return "sell"
        return "hold"

    def name(self) -> str:
        return "Threshold"