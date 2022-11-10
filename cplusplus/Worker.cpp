#include "Worker.hpp"

Worker::Worker(CoffeeHouse *model, CashDesk *cashDesk) : model(model), cashDesk(cashDesk)
{
	this->cashDesk = cashDesk;
	this->model = model;
}

void Worker::process(long currentTime)
{
	if (currentRecipe == nullptr)
	{
		Visitor *visitor = cashDesk->getFirstVisitor();
		if (visitor == nullptr)
		{
			return;
		}

		currentProduct = visitor->getDesiredProduct();
		if (currentProduct->getIsNeedPrepare())
		{
			currentRecipe = model->getRecipe(currentProduct);
			std::cout << "Time=" + std::to_string(currentTime) + " Worker(" + getHashCode() + ") start prepare product " << currentProduct->toString() << std::endl;
		}
		else
		{
			visitor->askDesiredProduct(currentTime);
		}
	}

	if (currentRecipe != nullptr)
	{
		prepareProductProcess(currentTime);
	}
}

void Worker::prepareProductProcess(long currentTime)
{
	if (nextActionTime == 0)
	{
		recipeStepIndex = 0;
		auto step = getRecipeStep(recipeStepIndex);
		assert(step != nullptr);

		nextActionTime = currentTime;
		processStepTime(step);
	}
	else if (nextActionTime <= currentTime)
	{
		auto step = getRecipeStep(recipeStepIndex);
		assert(step != nullptr);

		auto result = model->takeIngredient(step->getIngredient(), step->getAmount());
		if (!result)
		{
			cashDesk->getFirstVisitor()->failDesiredProduct(currentTime, currentProduct);
			prepareProductFinished(currentTime);
		}
		recipeStepIndex += 1;
		auto nextStep = getRecipeStep(recipeStepIndex);
		if (nextStep == nullptr)
		{
			// finish prepare
			model->takeProduct(currentProduct);
			cashDesk->getFirstVisitor()->givePreparedProduct(currentTime, currentProduct);
			prepareProductFinished(currentTime);
		}
		else
		{
			processStepTime(nextStep);
			prepareProductProcess(currentTime);
		}
	}
}

void Worker::prepareProductFinished(long currentTime)
{
	std::cout << "Time=" + std::to_string(currentTime) + " Worker(" + getHashCode() + ") finish prepare " << currentProduct->toString() << std::endl;
	nextActionTime = 0;
	recipeStepIndex = 0;
	currentProduct = nullptr;
	currentRecipe = nullptr;
}

void Worker::processStepTime(RecipeStep *step)
{
	nextActionTime += step->getTime();
}

std::string Worker::getHashCode()
{
	std::string thisAddress = std::to_string(reinterpret_cast<int>(this));
	std::string hashCode = std::to_string(std::hash<std::string>()(thisAddress));
	
	return hashCode;
}

RecipeStep *Worker::getRecipeStep(int index)
{
	assert(currentRecipe != nullptr);
	auto stepVector = currentRecipe->getStepVector();
	return stepVector.size() > recipeStepIndex ? stepVector[recipeStepIndex] : nullptr;
}