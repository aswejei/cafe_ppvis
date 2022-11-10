#include "Visitor.hpp"

Visitor::Visitor(CoffeeHouse *model)
{
	this->model = model;

	auto menu = model->getMenu();

	desiredProduct = menu[rand() % menu.size()];

	auto cashDeskVector = model->getCashDeskVector();
	cashDesk = cashDeskVector[rand() % cashDeskVector.size()];
	cashDesk->addVisitorToQueue(this);
}

void Visitor::process(long currentTime)
{
	if (nextActionTime == 0)
	{
		nextActionTime = currentTime + Settings::VISITOR_WAITING_TIME;
	}
	if (currentTime >= nextActionTime)
	{
		model->addRating(0);
		model->visitorLeave(this);
		std::cout << "Time=" + std::to_string(currentTime) + " Visitor leave by timeout " << this << std::endl;
	}
}

void Visitor::askDesiredProduct(long currentTime)
{
	auto requestStatus = model->requestProduct(desiredProduct);
	if (requestStatus == VisitorRequestStatus::SUCCESS)
	{
		model->takeProduct(desiredProduct);
		model->addRating(successRating);
		model->visitorLeave(this);
		std::cout << "Time=" + std::to_string(currentTime) + " Visitor(" + getHashCode() + ") leave with product " << desiredProduct->toString() << std::endl;
	}
	else if (requestStatus == VisitorRequestStatus::PRODUCT_MISSING)
	{
		failDesiredProduct(currentTime, desiredProduct);
	}
}

void Visitor::givePreparedProduct(long currentTime, Product *product)
{
	model->addRating(successRating);
	model->visitorLeave(this);
	std::cout << "Time=" + std::to_string(currentTime) + " Visitor(" + getHashCode() + ") leave with product " << product->toString() << std::endl;
}

void Visitor::failDesiredProduct(long currentTime, Product *product)
{
	model->addRating(1);
	model->visitorLeave(this);
	std::cout << "Time=" + std::to_string(currentTime) + " Visitor(" + getHashCode() + ") leave without product " << product->toString() << std::endl;
}

Product *Visitor::getDesiredProduct()
{
	return desiredProduct;
}

CashDesk *Visitor::getCashDesk()
{
	return cashDesk;
}

std::string Visitor::toString()
{
	std::vector<Visitor *> visitorVector = cashDesk->getVisitorVector();
	auto it = std::find(visitorVector.begin(), visitorVector.end(), this);
	return "Visitor(" + getHashCode() + ") desiredProduct=[" + desiredProduct->toString() + "] queuePos=" + std::to_string(it - visitorVector.begin());
}

std::string Visitor::getHashCode()
{
	std::string thisAddress = std::to_string(reinterpret_cast<int>(this));
	std::string hashCode = std::to_string(std::hash<std::string>()(thisAddress));

	return hashCode;
}
