#ifndef WORKER_EXT3_HPP
#define WORKER_EXT3_HPP

#include "../Worker.hpp"

class WorkerExt3 : public Worker {
public:
	WorkerExt3(CoffeeHouse* model, CashDesk* cashDesk);

protected:
	void prepareProductProcess(long currentTime);
};
#endif