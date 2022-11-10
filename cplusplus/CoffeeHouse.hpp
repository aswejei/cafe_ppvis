#ifndef COFFEE_HOUSE_HPP
#define COFFEE_HOUSE_HPP

#include <assert.h>
#include <algorithm>
#include <vector>
#include <map>
#include "Settings.hpp"
#include "Visitor.hpp"
#include "Product.hpp"
#include "CashDesk.hpp"
#include "VisitorRequestStatus.hpp"
#include "VisitorGenerator.hpp"
#include "Worker.hpp"
#include "Recipe.hpp"

class CashDesk;
class VisitorGenerator;

class CoffeeHouse
{
public:
	CoffeeHouse();

	void run();

	VisitorRequestStatus requestProduct(Product *product);

	void setVisitorGenerator(VisitorGenerator *visitorGenerator);

	void addRating(int rating);

	float getAvgRating();

	void visitorLeave(Visitor *visitor);

	void createMenu();

	std::vector<Product *> getMenu();

	void addDessert(Product *dessert, int amount);

	void takeProduct(Product *product);

	void addRecipe(Product *product, Recipe *recipe);

	Recipe *getRecipe(Product *product);

	void addIngredient(Ingredient *ingredient, int amount);

	bool takeIngredient(Ingredient *ingredient, int amount);

	void addCashDesk(CashDesk *cashDesk);

	std::vector<CashDesk*> getCashDeskVector();

private:
	VisitorGenerator *visitorGenerator = nullptr;
	std::map<Product *, int> dessertMap;
	std::map<Product *, Recipe *> recipeMap;
	std::vector<CashDesk *> cashDeskVector;
	std::vector<Product *> menuVector;
	std::vector<Visitor *> outgoingVisitorVector;
	std::map<Ingredient *, int> ingredientMap;

	long currentTime = 0;
	long ratingSum = 0;
	long ratingAmount = 0;
};

#endif