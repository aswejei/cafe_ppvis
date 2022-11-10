#ifndef PRODUCT_HPP
#define PRODUCT_HPP

#include <string>

class Product
{
public:
	Product(std::string name, bool isNeedPrepare);

	std::string getName();

	bool getIsNeedPrepare();

	std::string toString();

	std::string getHashCode();

private:
	std::string name;
	bool isNeedPrepare;
};

#endif