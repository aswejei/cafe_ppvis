#ifndef WORKER_WITH_SPEED_HPP
#define WORKER_WITH_SPEED_HPP

#include "../Worker.hpp"

class WorkerWithSpeed: public Worker
{
public:
	WorkerWithSpeed(CoffeeHouse *model, CashDesk *cashDesk);
	
protected:
	void processStepTime(RecipeStep *step);

protected:
	int speed;
};

#endif