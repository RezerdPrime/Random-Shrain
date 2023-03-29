#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include "build_stuff.h"
using namespace std;

float f1(float x) {
    return (x * x * x + 2 * x * x - 8 * x + 1);
}

float f2(float x) {
    return (5 * sin(x) + 12 * cos(x));
}


int main()
{
    setzoom(0.25);
    buildspeed(1);

    initwindow(800, 800);

    Axes();
    Plot(f1, LIGHTRED); Plot(f2, LIGHTGREEN);
    Cross(f1, f2, -5, 5); 
    Hatch(f1, f2);

    Area_RRM(f1, f2, 0);
    Area_RRM(f2, f1, 1);

    Area_MCM(f1, f2, 0, 25000);
    Area_MCM(f2, f1, 1, 25000);
    
    getch();
    closegraph();

    // -  https://www.desmos.com/calculator/pgojdlm9op?lang=ru - мои графики в десмосе
}
