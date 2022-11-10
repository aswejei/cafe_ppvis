#ifndef VISITOR_GENERATOR_EXT2_HPP
#define VISITOR_GENERATOR_EXT2_HPP

#include "../VisitorGenerator.hpp"
#include "VisitorWithLastChance.hpp"

class VisitorGeneratorExt2: public VisitorGenerator
{
public:
	VisitorGeneratorExt2(CoffeeHouse *model);
	
	Visitor *generateVisitor();
};

#endif