#ifndef VISITOR_GENERATOR_HPP
#define VISITOR_GENERATOR_HPP

#include <iostream>
#include <string>
#include "CoffeeHouse.hpp"
#include "Settings.hpp"
#include "Visitor.hpp"

class VisitorGenerator
{
public:
	VisitorGenerator(CoffeeHouse *model);

	void process(long currentTime);

	Visitor *generateVisitor();

protected:
	CoffeeHouse *model;

private:
	long nextActionTime = 0;
};

#endif