#ifndef KITCHEN_MACHINE_HPP
#define KITCHEN_MACHINE_HPP

#include <string>

class KitchenMachine
{
public:
	KitchenMachine(std::string name);

	std::string getName();

private:
	std::string name;
};

#endif