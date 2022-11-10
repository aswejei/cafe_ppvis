#ifndef SETTINGS_HPP
#define SETTINGS_HPP

class Settings
{
public:
    const static long TICK_TIME = 300;      // 5 minutes
    const static long CLOSING_TIME = 21600; // 6 hours

    const static long VISITOR_GENERATE_TIME_PERIOD = 900; // 15 minutes
    const static long VISITOR_WAITING_TIME = 300;         // 5 minutes
};

#endif