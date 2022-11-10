#ifndef APPLICATION_EXT4_HPP
#define APPLICATION_EXT4_HPP

#include "CoffeeHouseWithMoreStatistics.hpp"
#include "../VisitorGenerator.hpp"
#include "../CashDesk.hpp"
#include "../Worker.hpp"
#include "../Product.hpp"
#include "../Ingredient.hpp"
#include "../KitchenMachine.hpp"
#include "../Recipe.hpp"
#include "../RecipeStep.hpp"

class ApplicationExt4 {
public:
	ApplicationExt4();

	CoffeeHouseWithMoreStatistics* build();
};

#endif