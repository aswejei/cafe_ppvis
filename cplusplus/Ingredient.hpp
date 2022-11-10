#ifndef INGREDIENT_HPP
#define INGREDIENT_HPP

#include <string>

class Ingredient
{
public:
	Ingredient(std::string name);

	std::string getName();

private:
	std::string name;
};

#endif