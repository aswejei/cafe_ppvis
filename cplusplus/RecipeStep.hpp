#ifndef RECIPE_STEP_HPP
#define RECIPE_STEP_HPP

#include <string>
#include "Ingredient.hpp"
#include "KitchenMachine.hpp"

class RecipeStep
{
public:
	RecipeStep(Ingredient *ingredient, int amount, KitchenMachine *machine, long time);

	Ingredient *getIngredient();

	int getAmount();

	KitchenMachine *getMachine();

	long getTime();

private:
	Ingredient *ingredient;
	int amount;
	KitchenMachine *machine;
	long time;
};

#endif