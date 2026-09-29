from engine_bridge import stock_native as sn

bt = sn.Backtester(sn.BacktestParams(1000.0, 0.001))

prices  = [100, 102, 101, 105, 103]
signals = [sn.Signal.Buy, sn.Signal.Buy, sn.Signal.Hold,
           sn.Signal.Sell, sn.Signal.Sell]

r = bt.run(prices, signals)
print(f"Final value: {r.final_value:.2f}, trades: {r.num_trades}")

try:
    bt.run(prices, [sn.Signal.Buy])
except ValueError as e:
    print(f"Caught expected error: {e}")

# The mismatch Day 3 must resolve:
try:
    bt.run(prices, ["buy", "buy", "hold", "sell", "sell"])
except TypeError:
    print("Native engine rejects string signals (TypeError)")