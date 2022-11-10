#include "VisitorExt3.hpp"
VisitorExt3::VisitorExt3(CoffeeHouse* model) : Visitor(model) {
}

void VisitorExt3::failDesiredProduct(long currentTime, Product* product) {
	if (product->getIsNeedPrepare()) {
		successRating -= 1;
		if (successRating > 1) {
			return;
		}
	}
	Visitor::failDesiredProduct(currentTime, product);
}
