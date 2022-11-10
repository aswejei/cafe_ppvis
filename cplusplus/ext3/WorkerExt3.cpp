#include "WorkerExt3.hpp"

WorkerExt3::WorkerExt3(CoffeeHouse* model, CashDesk* cashDesk) : Worker(model, cashDesk) {
}

void WorkerExt3::prepareProductProcess(long currentTime) {
	if (currentRecipe != nullptr) {
		bool isFail = rand() % 2;
		if (isFail) {
			if (cashDesk->getFirstVisitor() == nullptr) {
				return;
			}
			cashDesk->getFirstVisitor()->failDesiredProduct(currentTime, currentProduct);
			prepareProductFinished(currentTime);
			return;
		}
	}
	Worker::prepareProductProcess(currentTime);
}

