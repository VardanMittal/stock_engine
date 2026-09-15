from abc import ABC, abstractmethod

class Predictable(ABC):
    """ Anything that can produce a Buy/Sell/Hold signal"""

    @abstractmethod
    def predict(self, prices:list[float]) -> str:
        pass

class Trainable(ABC):
    """Only for strategies that can learn from the previous data"""

    @abstractmethod
    def train(self, prev_data:list[dict]) -> None:
        pass

class Backtestable(ABC):
    """Only for tests that supports running against the testable window"""

    @abstractmethod
    def backtest(self,prices:list[float], window:int) -> list[str]:
        pass

