from engine_bridge import stock_native as sn
from engine_bridge.interface import BacktestEngine
from portfolio.backtest_config import BacktestConfig

_SIGNAL_MAP = {"buy": sn.Signal.Buy, "sell": sn.Signal.Sell, "hold": sn.Signal.Hold}

class CppEngine(BacktestEngine):
    """Adapts the native C++ Backtester to the BacktestEngine contract.
    AnalysisEngine sees BacktestEngine.run(prices, signals, config) -> dict
    and never knows an enum, a struct, or C++ is involved."""

    def run(self, prices: list[float], signals: list[str], config: BacktestConfig) -> dict:
        native_signals = [_SIGNAL_MAP[s] for s in signals]
        params = sn.BacktestParams(config.initial_capital, config.fee_pct)
        engine = sn.Backtester(params)

        result = engine.run(prices, native_signals)

        return {
            "final_value": round(result.final_value, 2),
            "trades": result.num_trades,
            "strategy": config.strategy_name,
        }