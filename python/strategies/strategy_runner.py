from strategies.interfaces import Predictable
from strategies.execution_mode import ExecutionMode

class StrategyRunner:
    """Bridges a PredictionStrategy (what signal) to an ExecutionMode
    (what to do about it). Swap either side independently — this
    class never needs to change for new strategies or new execution modes."""

    def __init__(self, strategy: Predictable, execution_mode: ExecutionMode):
        self.strategy = strategy
        self.execution_mode = execution_mode

    def run(self, prices: list[float], initial_cash: float = 10000.0) -> dict:
        state = {"cash": initial_cash, "shares": 0}
        for i in range(len(prices)):
            signal = self.strategy.predict(prices[:i + 1])
            state = self.execution_mode.execute(signal, prices[i], state)
        return state