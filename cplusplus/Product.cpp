#include "Product.hpp"

Product::Product(std::string name, bool isNeedPrepare) : name(name), isNeedPrepare(isNeedPrepare)
{
}

std::string Product::getName()
{
	return name;
}
bool Product::getIsNeedPrepare()
{
	return isNeedPrepare;
}

std::string Product::toString()
{
	return "Product(" + getHashCode() + ")" + " name=" + name;
}

std::string Product::getHashCode()
{
	std::string thisAddress = std::to_string(reinterpret_cast<int>(this));
	std::string hashCode = std::to_string(std::hash<std::string>()(thisAddress));

	return hashCode;
}