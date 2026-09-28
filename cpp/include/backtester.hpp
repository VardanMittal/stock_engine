#pragma once
#include <vector>

namespace stock
{
    enum class Signal : int
    {
        Sell = -1,
        Hold = 0,
        Buy = 1
    };
    struct BacktestParams
    {
        double initial_capital;
        double fee_rate; // craction of price charged per trade, e.g. 0.001
    };

    struct BacktestResult
    {
        double final_value;
        int num_trades;
    };
    class Backtester
    {
    public:
        explicit Backtester(const BacktestParams &params);

        BacktestResult run(const std::vector<double> &prices, const std::vector<Signal> &signals) const;

    private:
        BacktestParams params_;
    };
} // namespace stock
