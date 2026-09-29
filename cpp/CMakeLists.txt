cmake_minimum_required(VERSION 3.15)
project(stock_engine)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_library(stock_core STATIC src/backtester.cpp)
target_include_directories(stock_core PUBLIC include)

add_executable(engine src/main.cpp)
target_link_libraries(engine PRIVATE stock_core)

# --- Python binding ---
set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(stock_native bindings/bindings.cpp)
target_link_libraries(stock_native PRIVATE stock_core)

# Statically link MinGW runtime so the .pyd doesn't need MinGW DLLs on PATH
if(MINGW)
    target_link_options(stock_native PRIVATE -static -static-libgcc -static-libstdc++)
endif()

# Drop the built module next to the Python code that imports it
set_target_properties(stock_native PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/../python/engine_bridge)