#include "VisitorGenerator.hpp"

VisitorGenerator::VisitorGenerator(CoffeeHouse *model) : model(model)
{
	this->model = model;
}

void VisitorGenerator::process(long currentTime)
{
	if (nextActionTime <= currentTime)
	{
		auto visitor = generateVisitor();
		nextActionTime += Settings::VISITOR_GENERATE_TIME_PERIOD;
		std::cout << "Time=" + std::to_string(currentTime) + " Generate visitor " << visitor->toString() << std::endl;
	}
}

Visitor *VisitorGenerator::generateVisitor()
{
	return new Visitor(model);
}
