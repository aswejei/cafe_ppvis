#ifndef WORKER_HPP
#define WORKER_HPP

#include <iostream>
#include <string>
#include <assert.h>
#include "CoffeeHouse.hpp"
#include "CashDesk.hpp"
#include "Recipe.hpp"
#include "Product.hpp"
#include "RecipeStep.hpp"

class CoffeeHouse;
class CashDesk;

class Worker
{

public:
	Worker(CoffeeHouse *model, CashDesk *cashDesk);

	void process(long currentTime);

protected:
	void prepareProductProcess(long currentTime);

	void prepareProductFinished(long currentTime);

	void processStepTime(RecipeStep *step);

	std::string getHashCode();

private:
	RecipeStep *getRecipeStep(int index);

protected:
	CashDesk *cashDesk;
	CoffeeHouse *model;

	Product *currentProduct = nullptr;
	Recipe *currentRecipe = nullptr;
	int recipeStepIndex = 0;

	long nextActionTime = 0;
};

#endif