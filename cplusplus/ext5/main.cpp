#include <iostream>
#include "../CoffeeHouse.hpp"
#include "ApplicationExt5.hpp"
#include <time.h>

int main()
{
	setlocale(0, "");
	srand(time(0));
	ApplicationExt5 app;
	CoffeeHouse *model = app.build();
	std::cout << "Start modeling" << std::endl;
	model->run();
	std::cout << "Finish rating: " << model->getAvgRating() << std::endl;
	return 0;
}