#ifndef APPLICATION_EXT3_HPP
#define APPLICATION_EXT3_HPP

#include "../CoffeeHouse.hpp"
#include "VisitorGeneratorExt3.hpp"
#include "../CashDesk.hpp"
#include "WorkerExt3.hpp"
#include "../Product.hpp"
#include "../Ingredient.hpp"
#include "../KitchenMachine.hpp"
#include "../Recipe.hpp"
#include "../RecipeStep.hpp"

class ApplicationExt3 {
public:
	ApplicationExt3();

	CoffeeHouse* build();
};

#endif