cmake_minimum_required(VERSION 3.20.3 FATAL_ERROR)

project(cplusplus)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(exec
./WorkerExt3.hpp
./WorkerExt3.cpp
../VisitorRequestStatus.hpp
./VisitorGeneratorExt3.hpp
./VisitorGeneratorExt3.cpp
./VisitorExt3.hpp
./VisitorExt3.cpp
../Settings.hpp
../RecipeStep.hpp
../RecipeStep.cpp
../Recipe.hpp
../Recipe.cpp
../Product.hpp
../Product.cpp
../KitchenMachine.hpp
../KitchenMachine.cpp
../Ingredient.hpp
../Ingredient.cpp
../CoffeeHouse.hpp
../CoffeeHouse.cpp
../CashDesk.hpp
../CashDesk.cpp
./ApplicationExt3.hpp
./ApplicationExt3.cpp
./main.cpp)