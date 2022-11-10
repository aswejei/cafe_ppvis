#ifndef VISITOR_EXT3_HPP
#define VISITOR_EXT3_HPP

#include "../Visitor.hpp"

class VisitorExt3: public Visitor
{
public:
	VisitorExt3(CoffeeHouse* model);

	void failDesiredProduct(long currentTime, Product* product);
}
#endif