#ifndef COFFEE_HOUSE_WITH_SUPPLY_MANAGER_HPP
#define COFFEE_HOUSE_WITH_SUPPLY_MANAGER_HPP

#include "../CoffeeHouse.hpp"
#include "SupplyManager.hpp"

class CoffeeHouseWithSupplyManager : public CoffeeHouse {

public:
	CoffeeHouseWithSupplyManager();

	void addIngredient(Ingredient *ingredient, int amount);

	void addDessert(Product *dessert, int amount);

	void addSupplyManager(SupplyManager* supplyManager);

	void takeProduct(Product *product);

	bool takeIngredient(Ingredient *ingredient, int amount);
protected:
	SupplyManager* supplyManager;
};
#endif