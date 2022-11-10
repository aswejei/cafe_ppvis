#ifndef SUPPLY_MANAGER_HPP
#define SUPPLY_MANAGER_HPP

#include "CoffeeHouseWithSupplyManager.hpp"
#include <iostream>
#include <string>

class SupplyManager
{
public:
	SupplyManager(CoffeeHouseWithSupplyManager* model);

	long renewIngredient(Ingredient* ingredient, long& currentTime);

	long renewProduct(Product* product, long& currentTime);

	bool getManagerState();

	void addIngredientInitialAmount(Ingredient* ingredient, int amount);

	void addProductInitialAmount(Product* product, int amount);

	std::string getHashCode();

protected:
	CoffeeHouseWithSupplyManager* model;
	bool state;
	std::map<Ingredient*, int> ingredientInitialAmountMap;
	std::map<Product*, int> productInitialAmountMap;
};
#endif