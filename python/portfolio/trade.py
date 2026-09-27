class Trade:
    def __init__(self, action:str,price:float,shares:int) -> None:
        self.action = action
        self.price = price
        self.shares = shares

    def __repr__(self) -> str:
        return f"Trade({self.action}, {self.price}, {self.shares})"