#include "CashDesk.hpp"

CashDesk::CashDesk()
{
}

Worker *CashDesk::getWorker()
{
	return worker;
}
void CashDesk::setWorker(Worker *worker)
{
	this->worker = worker;
}

void CashDesk::addVisitorToQueue(Visitor *visitor)
{
	visitorVector.push_back(visitor);
}

Visitor *CashDesk::getFirstVisitor()
{
	return visitorVector.size() == 0 ? nullptr : visitorVector[0];
}

std::vector<Visitor *> CashDesk::getVisitorVector()
{
	return visitorVector;
}

void CashDesk::removeVisitor(Visitor *visitor)
{
	auto it = std::find(visitorVector.begin(), visitorVector.end(), visitor);
	if (it != visitorVector.end())
		visitorVector.erase(it);
}
