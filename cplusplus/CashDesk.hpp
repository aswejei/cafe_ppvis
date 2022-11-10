#ifndef CASH_DESK_HPP
#define CASH_DESK_HPP

#include <vector>
#include <algorithm>
#include "Worker.hpp"
#include "Visitor.hpp"

class Visitor;
class Worker;

class CashDesk
{
public:
	CashDesk();

	Worker *getWorker();

	void setWorker(Worker *worker);

	void addVisitorToQueue(Visitor *visitor);

	Visitor *getFirstVisitor();

	std::vector<Visitor *> getVisitorVector();

	void removeVisitor(Visitor *visitor);

private:
	Worker *worker = nullptr;
	std::vector<Visitor *> visitorVector;
};

#endif