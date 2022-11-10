#ifndef VISITOR_WITH_MOOD_GENERATOR_HPP
#define VISITOR_WITH_MOOD_GENERATOR_HPP

#include "../VisitorGenerator.hpp"
#include "VisitorWithMood.hpp"

class VisitorWithMoodGenerator : public VisitorGenerator
{
public:
	VisitorWithMoodGenerator(CoffeeHouse* model);
protected:
	Visitor* generateVisitor();
};
#endif
