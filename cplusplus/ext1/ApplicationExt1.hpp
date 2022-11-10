#ifndef APPLICATION_EXT1_HPP
#define APPLICATION_EXT1_HPP

#include "../CoffeeHouse.hpp"
#include "../VisitorGenerator.hpp"
#include "../CashDesk.hpp"
#include "WorkerWithSpeed.hpp"
#include "../Product.hpp"
#include "../Ingredient.hpp"
#include "../KitchenMachine.hpp"
#include "../Recipe.hpp"
#include "../RecipeStep.hpp"

class ApplicationExt1
{
public:
	ApplicationExt1();

	CoffeeHouse *build();
};

#endif