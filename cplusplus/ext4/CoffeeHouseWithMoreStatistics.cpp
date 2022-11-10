#include "CoffeeHouseWithMoreStatistics.hpp"

CoffeeHouseWithMoreStatistics::CoffeeHouseWithMoreStatistics() : CoffeeHouse()
{
}

void CoffeeHouseWithMoreStatistics::printMoreStatistics() {
	std::cout << "Visitors: " + visitorCounter;
	std::cout << "Dessert: " + dessertCounter;
	std::cout << "Drink: " + drinkCounter;
}

void CoffeeHouseWithMoreStatistics::visitorLeave(Visitor* visitor) {
	CoffeeHouse::visitorLeave(visitor);
	visitorCounter += 1;
}

void CoffeeHouseWithMoreStatistics::takeProduct(Product* product) {
	CoffeeHouse::takeProduct(product);
	if (product->getIsNeedPrepare()) {
		drinkCounter += 1;
	}
	else {
		dessertCounter += 1;
	}
}

