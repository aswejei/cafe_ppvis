#ifndef APPLICATION_EXT1_HPP
#define APPLICATION_EXT1_HPP

#include "../CoffeeHouse.hpp"
#include "VisitorGeneratorExt2.hpp"
#include "../CashDesk.hpp"
#include "../Worker.hpp"
#include "../Product.hpp"
#include "../Ingredient.hpp"
#include "../KitchenMachine.hpp"
#include "../Recipe.hpp"
#include "../RecipeStep.hpp"

class ApplicationExt2
{
public:
	ApplicationExt2();

	CoffeeHouse *build();
};

#endif