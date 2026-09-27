import copy
from portfolio.trade import Trade

class Portfolio:
    """Supports cloning itself for what-if simulations. Cloning must
    be deep — trade_history is a list of mutable Trade objects, and a
    shallow copy would let mutations on the clone leak back into the
    original."""
    def __init__(self, cash: float, shares: int = 0):
        self.cash = cash
        self.shares = shares
        self.trade_history = []  # list[Trade]

    def buy(self, price: float, num_shares: int):
        cost = price * num_shares
        if cost > self.cash:
            return False
        self.cash -= cost
        self.shares += num_shares
        self.trade_history.append(Trade("buy", price, num_shares))
        return True

    def sell(self, price: float, num_shares: int):
        if num_shares > self.shares:
            return False
        self.cash += price * num_shares
        self.shares -= num_shares
        self.trade_history.append(Trade("sell", price, num_shares))
        return True
    def total_value(self, current_price: float) -> float:
        return self.cash + self.shares * current_price

    def clone(self) -> "Portfolio":
        """Deep clone — the returned Portfolio shares NOTHING mutable
        with the original. Mutating the clone's trade_history or
        buying/selling on it never touches self."""
        return copy.deepcopy(self)

    def __repr__(self):
        return f"Portfolio(cash={self.cash:.2f}, shares={self.shares}, trades={len(self.trade_history)})"