#ifndef RECIPE_HPP
#define RECIPE_HPP

#include <vector>
#include "RecipeStep.hpp"

class Recipe
{
public:
	Recipe();

	Recipe *addStep(RecipeStep *step);

	std::vector<RecipeStep *> getStepVector();

private:
	std::vector<RecipeStep *> stepVector;
};

#endif