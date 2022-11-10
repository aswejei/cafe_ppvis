#ifndef VISITOR_GENERATOR_EXT3_HPP
#define VISITOR_GENERATOR_EXT3_HPP

#include "../VisitorGenerator.hpp"
#include "VisitorExt3.hpp"

class VisitorGeneratorExt3 : public VisitorGenerator
{
public:
	VisitorGeneratorExt3(CoffeeHouse* model);
protected:
	Visitor* generateVisitor();
};
#endif
