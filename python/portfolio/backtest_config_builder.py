from portfolio.backtest_config import BacktestConfig

class BacktestConfigBuilder:
    """Step-by-step construction of BacktestConfig. Required fields
    have no default; optional fields do. .build() is the only place
    the actual BacktestConfig gets created."""

    def __init__(self):
        self._start_date = None
        self._end_date = None
        self._initial_capital = 10000.0   # sensible default
        self._strategy_name = None
        self._fee_pct = 0.001             # sensible default (0.1%)

    def with_date_range(self, start_date: str, end_date: str):
        self._start_date = start_date
        self._end_date = end_date
        return self

    def with_capital(self, amount: float):
        self._initial_capital = amount
        return self

    def with_strategy(self, strategy_name: str):
        self._strategy_name = strategy_name
        return self

    def with_fee(self, fee_pct: float):
        self._fee_pct = fee_pct
        return self

    def build(self) -> BacktestConfig:
        if self._start_date is None or self._end_date is None:
            raise ValueError("Date range is required — call with_date_range()")
        if self._strategy_name is None:
            raise ValueError("Strategy is required — call with_strategy()")

        return BacktestConfig(
            start_date=self._start_date,
            end_date=self._end_date,
            initial_capital=self._initial_capital,
            strategy_name=self._strategy_name,
            fee_pct=self._fee_pct,
        )