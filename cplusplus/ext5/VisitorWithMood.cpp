#include "VisitorWithMood.hpp"

VisitorWithMood::VisitorWithMood(CoffeeHouse* model) : Visitor(model) {
	if (this->ifWantsToLeave())
		this->leaveQueue();
}

void VisitorWithMood::process(long currentTime)
{
	if (this->ifWantsToLeave())
		this->leaveQueue();
	else
		Visitor::process(currentTime);
}

bool VisitorWithMood::ifWantsToLeave()
{
	int mood = rand() % 10;
	if (mood < 3)
		return true;
	return false;
}

void VisitorWithMood::leaveQueue()
{
	this->model->addRating(3);
	this->cashDesk->removeVisitor(this);
}