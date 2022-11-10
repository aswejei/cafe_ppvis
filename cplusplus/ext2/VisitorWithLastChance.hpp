#ifndef VISITOR_WITH_LAST_CHANCE_HPP
#define VISITOR_WITH_LAST_CHANCE_HPP

#include "../Visitor.hpp"

class VisitorWithLastChance: public Visitor
{
public:
	VisitorWithLastChance(CoffeeHouse *model);
	
	void failDesiredProduct(long currentTime, Product *product);
};

#endif