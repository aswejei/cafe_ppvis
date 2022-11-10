#include "KitchenMachine.hpp"

KitchenMachine::KitchenMachine(std::string name) : name(name)
{
}

std::string KitchenMachine::getName()
{
	return name;
}