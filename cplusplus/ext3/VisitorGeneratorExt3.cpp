#include "VisitorGeneratorExt3.hpp"

VisitorGeneratorExt3::VisitorGeneratorExt3(CoffeeHouse* model) : VisitorGenerator(model) {
}

Visitor* VisitorGeneratorExt3::generateVisitor() {
	return new VisitorExt3(model);
}
