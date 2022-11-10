#ifndef APPLICATION_HPP
#define APPLICATION_HPP

#include "CoffeeHouse.hpp"
#include "VisitorGenerator.hpp"
#include "CashDesk.hpp"
#include "Worker.hpp"
#include "Product.hpp"
#include "Ingredient.hpp"
#include "KitchenMachine.hpp"
#include "Recipe.hpp"
#include "RecipeStep.hpp"

class Application
{
public:
	Application();

	CoffeeHouse *build();
};

#endif