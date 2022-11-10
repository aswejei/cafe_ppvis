#include "Ingredient.hpp"

Ingredient::Ingredient(std::string name) : name(name)
{
}

std::string Ingredient::getName()
{
	return name;
};
