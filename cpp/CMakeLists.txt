cmake_minimum_required(VERSION 3.15)
project(stock_engine)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_library(stock_core STATIC src/backtester.cpp)
target_include_directories(stock_core PUBLIC include)

add_executable(engine src/main.cpp)
target_link_libraries(engine PRIVATE stock_core)