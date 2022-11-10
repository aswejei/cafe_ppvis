#include "Recipe.hpp"

Recipe::Recipe()
{
}
Recipe *Recipe::addStep(RecipeStep *step)
{
	stepVector.push_back(step);
	return this;
}

std::vector<RecipeStep *> Recipe::getStepVector()
{
	return stepVector;
}
