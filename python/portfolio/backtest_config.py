class BacktestConfig:
    """Immutable-by-convention result object. Built exclusively via
    BacktestConfigBuilder — never constructed directly with a long
    argument list."""

    def __init__(self, start_date, end_date, initial_capital, strategy_name, fee_pct):
        self.start_date = start_date
        self.end_date = end_date
        self.initial_capital = initial_capital
        self.strategy_name = strategy_name
        self.fee_pct = fee_pct

    def __repr__(self):
        return (f"BacktestConfig(start={self.start_date}, end={self.end_date}, "
                f"capital={self.initial_capital}, strategy={self.strategy_name}, "
                f"fee={self.fee_pct})")