#ifndef VISITOR_HPP
#define VISITOR_HPP

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include "VisitorRequestStatus.hpp"
#include "CoffeeHouse.hpp"
#include "CashDesk.hpp"
#include "Settings.hpp"

class CoffeeHouse;
class Product;
class CashDesk;

class Visitor
{
public:
	Visitor(CoffeeHouse *model);

	void process(long currentTime);

	void askDesiredProduct(long currentTime);

	void givePreparedProduct(long currentTime, Product *product);

	void failDesiredProduct(long currentTime, Product *product);

	Product *getDesiredProduct();

	CashDesk *getCashDesk();

	std::string toString();

	std::string getHashCode();

protected:
	CoffeeHouse *model = nullptr;
	CashDesk *cashDesk = nullptr;
	Product *desiredProduct = nullptr;
	long nextActionTime = 0;
	int successRating = 5;
};

#endif