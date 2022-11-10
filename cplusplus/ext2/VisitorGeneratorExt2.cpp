
#include "VisitorGeneratorExt2.hpp"

VisitorGeneratorExt2::VisitorGeneratorExt2(CoffeeHouse *model) : VisitorGenerator(model)
{
}

Visitor *VisitorGeneratorExt2::generateVisitor()
{
	return new VisitorWithLastChance(model);
}
