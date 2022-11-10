#ifndef VISITOR_WITH_MOOD_HPP
#define VISITOR_WITH_MOOD_HPP

#include "../Visitor.hpp"

class VisitorWithMood : public Visitor
{
public:
	VisitorWithMood(CoffeeHouse* model);

	void process(long currentTime);

	bool ifWantsToLeave();

	void leaveQueue();
}
#endif