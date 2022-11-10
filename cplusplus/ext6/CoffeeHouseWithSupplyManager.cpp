#include "CoffeeHouseWithSupplyManager.hpp"

CoffeeHouseWithSupplyManager::CoffeeHouseWithSupplyManager() : CoffeeHouse()
{
}

void CoffeeHouseWithSupplyManager::addIngredient(Ingredient *ingredient, int amount)
{
	CoffeeHouse::addIngredient(ingredient, amount);
	this->supplyManager->addIngredientInitialAmount(ingredient, amount);
}

void CoffeeHouseWithSupplyManager::addDessert(Product *dessert, int amount)
{
	CoffeeHouse::addDessert(dessert, amount);
	this->supplyManager->addProductInitialAmount(dessert, amount);
}

void CoffeeHouseWithSupplyManager::addSupplyManager(SupplyManager* supplyManager)
{
	if (this->supplyManager == nullptr)
		this->supplyManager = supplyManager;
}

void CoffeeHouseWithSupplyManager::takeProduct(Product *product)
{
	if (!product->getIsNeedPrepare())
	{
		auto it = dessertMap.find(product);
		int currentAmount;
		if (it != dessertMap.end())
			currentAmount = it->second;
		else
			currentAmount = 0;
		if (currentAmount > 0)
		{
			dessertMap[product]--;
			if (this->dessertMap[product] < 1)
				if (this->supplyManager->getManagerState())
				{
					long time = this->supplyManager->renewProduct(product, this->currentTime);
					this->currentTime += time;
				}
		}
	}
}

bool CoffeeHouseWithSupplyManager::takeIngredient(Ingredient *ingredient, int amount)
{
	auto it = ingredientMap.find(ingredient);
	int currentAmount;
	if (it != ingredientMap.end())
		currentAmount = it->second;
	else
		currentAmount = 0;
	if (currentAmount - amount >= 0)
	{
		ingredientMap[ingredient] -= amount;
		if (this->ingredientMap[ingredient] < 0)
			if (this->supplyManager->getManagerState())
			{
				long time = this->supplyManager->renewIngredient(ingredient, this->currentTime);
				this->currentTime += time;
			}
		return true;
	}
	return false;
}

