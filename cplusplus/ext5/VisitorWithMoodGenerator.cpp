#include "VisitorWithMoodGenerator.hpp"

VisitorWithMoodGenerator::VisitorWithMoodGenerator(CoffeeHouse* model) : VisitorGenerator(model) {
}

Visitor* VisitorWithMoodGenerator::generateVisitor() {
	return new VisitorWithMood(model);
}
