#include <time.h>

int t0 = 0, t1 = 0;

void begin__() { t0 = clock(); }
void end__() { 
	t1 = clock(); 
	double dif = (t1 - t0) / 1000.;
	std::cout << "\nAlgorithm runtime: " << dif << std::endl;
}

#define START begin__();
#define STOP end__();