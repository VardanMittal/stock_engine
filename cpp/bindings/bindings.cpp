#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // list <-> std::vector conversion
#include "backtester.hpp"

namespace py = pybind11;
using namespace stock;

PYBIND11_MODULE(stock_native, m)
{
    m.doc() = "Native C++ backtesting engine";

    py::enum_<Signal>(m, "Signal")
        .value("Sell", Signal::Sell)
        .value("Hold", Signal::Hold)
        .value("Buy", Signal::Buy);

    py::class_<BacktestParams>(m, "BacktestParams")
        .def(py::init([](double capital, double fee)
                      { return BacktestParams{capital, fee}; }),
             py::arg("initial_capital"), py::arg("fee_rate"))
        .def_readwrite("initial_capital", &BacktestParams::initial_capital)
        .def_readwrite("fee_rate", &BacktestParams::fee_rate);

    py::class_<BacktestResult>(m, "BacktestResult")
        .def_readonly("final_value", &BacktestResult::final_value)
        .def_readonly("num_trades", &BacktestResult::num_trades);

    py::class_<Backtester>(m, "Backtester")
        .def(py::init<const BacktestParams &>())
        .def("run", &Backtester::run, py::arg("prices"), py::arg("signals"));
}