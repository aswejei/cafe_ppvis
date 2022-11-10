#ifndef COFFEE_HOUSE_WITH_MORE_STATISTICS_HPP
#define COFFEE_HOUSE_WITH_MORE_STATISTICS_HPP

#include "../CoffeeHouse.hpp"
#include <iostream>

class CoffeeHouseWithMoreStatistics: public CoffeeHouse {

public:
	CoffeeHouseWithMoreStatistics();

	void printMoreStatistics();

	void visitorLeave(Visitor* visitor);

	void takeProduct(Product* product);

private:
	int visitorCounter = 0;
	int dessertCounter = 0;
	int drinkCounter = 0;
};
#endif