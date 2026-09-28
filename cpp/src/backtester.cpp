#include "backtester.hpp"
#include <stdexcept>

namespace stock
{
    Backtester::Backtester(const BacktestParams &params) : params_(params) {}

    BacktestResult Backtester::run(const std::vector<double> &prices, const std::vector<Signal> &signals) const
    {
        if (prices.empty() || prices.size() != signals.size())
        {
            throw std::invalid_argument("prices & signals must be non-empty and equal length");
        }

        double cash = params_.initial_capital;
        int shares = 0;
        int trades = 0;

        for (std::size_t i = 0; i < prices.size(); ++i)
        {
            const double price = prices[i];
            const double fee = price * params_.fee_rate;

            if (signals[i] == Signal::Buy && cash >= price + fee)
            {
                cash -= price + fee;
                ++shares;
                ++trades;
            }
            else if (signals[i] == Signal::Sell && shares > 0)
            {
                cash += price - fee;
                --shares;
                ++trades;
            }
        }
        return {cash + shares * prices.back(), trades};
    }

} // namespace stock