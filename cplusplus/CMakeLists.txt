cmake_minimum_required(VERSION 3.20.3 FATAL_ERROR)

project(cplusplus)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(exec
./Worker.hpp
./Worker.cpp
./VisitorRequestStatus.hpp
./VisitorGenerator.hpp
./VisitorGenerator.cpp
./Visitor.hpp
./Visitor.cpp
./Settings.hpp
./RecipeStep.hpp
./RecipeStep.cpp
./Recipe.hpp
./Recipe.cpp
./Product.hpp
./Product.cpp
./KitchenMachine.hpp
./KitchenMachine.cpp
./Ingredient.hpp
./Ingredient.cpp
./CoffeeHouse.hpp
./CoffeeHouse.cpp
./CashDesk.hpp
./CashDesk.cpp
./Application.hpp
./Application.cpp
./main.cpp)