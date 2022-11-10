#include "SupplyManager.hpp"

SupplyManager::SupplyManager(CoffeeHouseWithSupplyManager* model) : model(model), state(true)
{
}

long SupplyManager::renewIngredient(Ingredient* ingredient, long& currentTime)
{
	this->state = false;
	std::cout << "Time= " << currentTime << " Supply manager " << this->getHashCode() << " left to get missing ingredient(Missing ingredient is " << ingredient->getName() << ") " << std::endl;
	currentTime += this->ingredientInitialAmountMap[ingredient] / 10;
	this->model->addIngredient(ingredient, this->ingredientInitialAmountMap[ingredient]);
	std::cout << "Time= " << currentTime << " Supply manager " << this->getHashCode() << " successfully bought missing ingredient(" << ingredient->getName() << ")." << std::endl;
	std::cout << "Missing ingredient is now renewed";
	this->state = true;
	return currentTime;
}

long SupplyManager::renewProduct(Product* product, long& currentTime)
{
	this->state = false;
	std::cout << "Time= " << currentTime << " Supply manager " << this->getHashCode() << " left to get missing product(Missing ingredient is " << product->toString() << ") " << std::endl;
	currentTime += this->productInitialAmountMap[product] / 10;
	this->model->addDessert(product, this->productInitialAmountMap[product]);
	std::cout << "Time= " << currentTime << " Supply manager " << product->getHashCode() << " successfully bought missing product(" << product->toString() << ")." << std::endl;
	std::cout << "Missing product is now renewed";
	this->state = true;
	return currentTime;
}

bool SupplyManager::getManagerState()
{
	return this->state;
}

void SupplyManager::addIngredientInitialAmount(Ingredient* ingredient, int amount)
{
	auto it = this->ingredientInitialAmountMap.find(ingredient);
	if (it == this->ingredientInitialAmountMap.end())
		this->ingredientInitialAmountMap[ingredient] = amount;
}

void SupplyManager::addProductInitialAmount(Product* product, int amount)
{
	auto it = this->productInitialAmountMap.find(product);
	if (it == this->productInitialAmountMap.end())
		this->productInitialAmountMap[product] = amount;
}

std::string SupplyManager::getHashCode()
{
	std::string thisAddress = std::to_string(reinterpret_cast<int>(this));
	std::string hashCode = std::to_string(std::hash<std::string>()(thisAddress));

	return hashCode;
}