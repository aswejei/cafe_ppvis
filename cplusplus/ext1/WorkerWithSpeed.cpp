#include "WorkerWithSpeed.hpp"

WorkerWithSpeed::WorkerWithSpeed(CoffeeHouse *model, CashDesk *cashDesk) : Worker(model, cashDesk)
{
	this->speed = rand() % 11;
}

void WorkerWithSpeed::processStepTime(RecipeStep *step)
{
	nextActionTime += step->getTime() / this->speed;
}