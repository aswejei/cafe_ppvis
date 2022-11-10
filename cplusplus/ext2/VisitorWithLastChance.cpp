#include "VisitorWithLastChance.hpp"

VisitorWithLastChance::VisitorWithLastChance(CoffeeHouse *model): Visitor(model)
{
}

void VisitorWithLastChance::failDesiredProduct(long currentTime, Product *product)
{
	if (this->successRating == 5)
	{
		this->successRating = 4;
		auto menu = this->model->getMenu();
		this->desiredProduct = menu[rand() % menu.size()];
	}
	else
	{
		Visitor::failDesiredProduct(currentTime, product);
	}
}