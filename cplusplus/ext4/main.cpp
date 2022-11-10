#include <iostream>
#include "CoffeeHouseWithMoreStatistics.hpp"
#include "ApplicationExt4.hpp"
#include <time.h>

	int main()
	{
		setlocale(0, "");
		srand(time(0));
		ApplicationExt4 app;
		CoffeeHouseWithMoreStatistics *model = app.build();
		std::cout << "Start modeling" << std::endl;
		model->run();
		std::cout << "Finish rating: " << model->getAvgRating() << std::endl;
		model->printMoreStatistics();
		return 0;
	}