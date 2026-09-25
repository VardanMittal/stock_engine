from engine_bridge.interface import BacktestEngine
from portfolio.backtest_config import BacktestConfig

class StubEngine(BacktestEngine):
    """Placeholder engine — pure Python, no C++ yet. Lets us build and
    test the high-level flow before the real pybind11 bridge exists."""

    def run(self, prices: list[float], signals: list[str], config:BacktestConfig) -> dict:
        cash = config.initial_capital
        shares = 0
        trades = 0

        for price, signal in zip(prices, signals):
            fee = price * config.fee_pct
            if signal == "buy" and cash >= price:
                shares += 1
                cash -= (price + fee)
                trades += 1
            elif signal == "sell" and shares > 0:
                shares -= 1
                cash += (price - fee)
                trades += 1

        final_value = cash + shares * prices[-1]
        return {"final_value": round(final_value, 2), "trades": trades, "strategy": config.strategy_name,}