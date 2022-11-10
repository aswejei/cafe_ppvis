#include "RecipeStep.hpp"

RecipeStep::RecipeStep(Ingredient *ingredient, int amount, KitchenMachine *machine, long time) : ingredient(ingredient), amount(amount), machine(machine), time(time)
{
}

Ingredient *RecipeStep::getIngredient()
{
	return ingredient;
}
int RecipeStep::getAmount()
{
	return amount;
}
KitchenMachine *RecipeStep::getMachine()
{
	return machine;
}
long RecipeStep::getTime()
{
	return time;
}
