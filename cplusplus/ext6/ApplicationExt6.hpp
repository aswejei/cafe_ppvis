#ifndef APPLICATION_EXT6_HPP
#define APPLICATION_EXT6_HPP

#include "CoffeeHouseWithSupplyManager.hpp"
#include "SupplyManager.hpp"
#include "../VisitorGenerator.hpp"
#include "../CashDesk.hpp"
#include "../Worker.hpp"
#include "../Product.hpp"
#include "../Ingredient.hpp"
#include "../KitchenMachine.hpp"
#include "../Recipe.hpp"
#include "../RecipeStep.hpp"

class ApplicationExt6 {
public:
	ApplicationExt6();

	CoffeeHouseWithSupplyManager* build();
};

#endif