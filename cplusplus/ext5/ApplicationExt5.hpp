#ifndef APPLICATION_EXT5_HPP
#define APPLICATION_EXT5_HPP

#include "../CoffeeHouse.hpp"
#include "VisitorWithMoodGenerator.hpp"
#include "../CashDesk.hpp"
#include "../Worker.hpp"
#include "../Product.hpp"
#include "../Ingredient.hpp"
#include "../KitchenMachine.hpp"
#include "../Recipe.hpp"
#include "../RecipeStep.hpp"

class ApplicationExt5 {
public:
	ApplicationExt5();

	CoffeeHouse* build();
};

#endif