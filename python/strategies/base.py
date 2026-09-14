from abc import abstractmethod, ABC


class PredictionStrategy(ABC):
    """Every strategy takes a list of closing prices and returns a
    signal: 'buy', 'sell', or 'hold'. No subclass may return anything
    else, require extra arguments, or raise on valid input."""
    @abstractmethod
    def predict(self, prices: list[float]) -> str:
        pass

    @abstractmethod
    def name(self) -> str:
        pass
