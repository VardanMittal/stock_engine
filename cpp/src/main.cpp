#include <iostream>
#include "backtester.hpp"
#include <iomanip>

int main()
{
    using namespace stock;

    Backtester bt({1000.0, 0.001});

    std::vector<double> prices = {100, 102, 101, 105, 103};
    std::vector<Signal> signals = {Signal::Buy, Signal::Buy, Signal::Hold, Signal::Sell, Signal::Sell};

    BacktestResult r = bt.run(prices, signals);

    std::cout << std::fixed << std::setprecision(2) << "Final value: " << r.final_value << " , trades: " << r.num_trades << std::endl;

    try
    {
        bt.run(prices, {Signal::Buy}); // size mismatch
    }
    catch (const std::invalid_argument &e)
    {
        std::cout << "Caught expected error: " << e.what() << std::endl;
    }
    return 0;
}