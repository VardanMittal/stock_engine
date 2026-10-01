from abc import ABC, abstractmethod

class ExecutionMode(ABC):
    """How a signal gets acted on. Independent of WHICH strategy
    produced the signal — a Bridge implementation hierarchy."""

    @abstractmethod
    def execute(self, signal: str, price: float, state: dict) -> dict:
        """Takes a signal + current price + mutable state dict,
        returns the updated state."""
        pass


class BacktestExecutionMode(ExecutionMode):
    """Executes against historical prices with real portfolio tracking."""

    def execute(self, signal: str, price: float, state: dict) -> dict:
        cash, shares = state["cash"], state["shares"]
        if signal == "buy" and cash >= price:
            cash -= price
            shares += 1
        elif signal == "sell" and shares > 0:
            cash += price
            shares -= 1
        return {"cash": cash, "shares": shares}


class PaperTradeExecutionMode(ExecutionMode):
    """Logs what WOULD happen without touching real cash/shares —
    useful for watching a strategy live before trusting it."""

    def execute(self, signal: str, price: float, state: dict) -> dict:
        if signal in ("buy", "sell"):
            print(f"[PAPER] Would {signal} at {price:.2f}")
        return state  # state never actually changes