#include "CoffeeHouse.hpp"

CoffeeHouse::CoffeeHouse()
{
}

void CoffeeHouse::run()
{
	createMenu();

	while (currentTime < Settings::CLOSING_TIME)
	{
		for (Visitor *visitor : outgoingVisitorVector)
		{
			visitor->getCashDesk()->removeVisitor(visitor);
		}
		outgoingVisitorVector.clear();

		assert(visitorGenerator != nullptr);
		visitorGenerator->process(currentTime);

		for (CashDesk *cash_desk : cashDeskVector)
		{
			cash_desk->getWorker()->process(currentTime);
			for (Visitor *visitor : cash_desk->getVisitorVector())
			{
				auto it = std::find(outgoingVisitorVector.begin(), outgoingVisitorVector.end(), visitor);
				if (it != outgoingVisitorVector.end())
					visitor->process(currentTime);
			}
		}

		currentTime += Settings::TICK_TIME;
	}
}

VisitorRequestStatus CoffeeHouse::requestProduct(Product *product)
{
	if (product->getIsNeedPrepare())
	{
		if (recipeMap.find(product) != recipeMap.end())
		{
			return VisitorRequestStatus::NEED_PREPARE;
		}
	}
	else
	{
		auto it = dessertMap.find(product);
		int currentAmount;
		if (it != dessertMap.end())
			currentAmount = it->second;
		else
			currentAmount = 0;
		if (currentAmount > 0)
		{
			return VisitorRequestStatus::SUCCESS;
		}
	}

	return VisitorRequestStatus::PRODUCT_MISSING;
}

void CoffeeHouse::setVisitorGenerator(VisitorGenerator *visitorGenerator)
{
	this->visitorGenerator = visitorGenerator;
}

void CoffeeHouse::addRating(int rating)
{
	ratingSum += rating;
	ratingAmount += 1;
}

float CoffeeHouse::getAvgRating()
{
	return (float)ratingSum / (float)ratingAmount;
}

void CoffeeHouse::visitorLeave(Visitor *visitor)
{
	outgoingVisitorVector.push_back(visitor);
}

void CoffeeHouse::createMenu()
{
	for (std::map<Product *, int>::iterator it = dessertMap.begin(); it != dessertMap.end(); it++)
		menuVector.push_back(it->first);
	for (std::map<Product *, Recipe *>::iterator it = recipeMap.begin(); it != recipeMap.end(); it++)
		menuVector.push_back(it->first);
}

std::vector<Product *> CoffeeHouse::getMenu()
{
	return menuVector;
}

void CoffeeHouse::addDessert(Product *dessert, int amount)
{
	dessertMap[dessert] += amount;
}

void CoffeeHouse::takeProduct(Product *product)
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
		}
	}
}

void CoffeeHouse::addRecipe(Product *product, Recipe *recipe)
{
	recipeMap[product] = recipe;
}

Recipe *CoffeeHouse::getRecipe(Product *product)
{
	auto it = recipeMap.find(product);
	if (it != recipeMap.end())
		return it->second;
	return nullptr;
}

void CoffeeHouse::addIngredient(Ingredient *ingredient, int amount)
{
	ingredientMap[ingredient] = amount;
}

bool CoffeeHouse::takeIngredient(Ingredient *ingredient, int amount)
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
		return true;
	}
	return false;
}

void CoffeeHouse::addCashDesk(CashDesk *cashDesk)
{
	cashDeskVector.push_back(cashDesk);
}

std::vector<CashDesk *> CoffeeHouse::getCashDeskVector()
{
	return cashDeskVector;
}
