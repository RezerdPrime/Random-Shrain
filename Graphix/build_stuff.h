#define _USE_MATH_DEFINES
#include "graphics.h"
#include <math.h>

int X0 = 400, 
    Y0 = 400, 
    kaunt = 0; //X0 = 525, Y0 = 520;

float k = 10, 
      solutions[3], 
      dstep = 0.01;

char s[16] = {};
  

// Sets the discretization step
void buildspeed(float x) { dstep *= x; }


// Sets the scale
void setzoom(float x) { k *= x; }


// Sets the correspondence between the value and the screen
int ScreenX(float x) { return X0 + k * x; } int ScreenY(float y) { return Y0 - k * y; }


// Sets the correspondence between the value and the graph
int graphX(float x) { return X0 + k * x * 10; } int graphY(float y) { return Y0 - k * y * 10; }


// Draws the axis lol
void Axes(int color = WHITE) {
    int xe, ye; setcolor(color);

    sprintf(s, "Zoom: %.2f", k / 10);
    outtextxy(10, 10, s);
    sprintf(s, "Speed: %.2f", dstep * 100);
    outtextxy(10, 32, s);

    sprintf(s, ">"); outtextxy(ScreenX(X0 / k - 20 / k) + 3, ScreenY(0) - 8, s); // the arrows of the axis
    sprintf(s, "/\\"); outtextxy(ScreenX(0) - 3, ScreenY(Y0 / k - 20 / k) - 23, s);

    line(X0, 0, X0, 800); // the axis
    line(0, Y0, 800, Y0);

    sprintf(s, "0");
    outtextxy(ScreenX(0) - 14, ScreenY(0) + 4, s);

    for (int i = -X0 / k; i <= (800 - X0) / k; i++) { // value and hatch setting (X axis) // 1050 - X0

        xe = ScreenX(i);

        if (i and i % 2 == 0) {
            line(xe, Y0 - 2 - 3 * (i % 10 == 0), xe, Y0 + 2 + 3 * (i % 10 == 0));
        } xe = ScreenX(10 * i);

        if (i and xe < 800 and xe > -10) sprintf(s, "%d", i), outtextxy(xe - 3 - 4 * (i < 0), Y0 + 7, s);
    }

    for (int i = -Y0 / k; i <= (800 - Y0) / k; i++) { // value and hatch setting (Y axis)

        ye = ScreenY(i);

        if (i and i % 2 == 0) {
            line(X0 - 2 - 3 * (i % 10 == 0), ye, X0 + 2 + 3 * (i % 10 == 0), ye);
        } ye = ScreenY(10 * i);

        if (i and ye < 800 and ye > -10) sprintf(s, "%d", i), outtextxy(X0 - 16 - 3 * (i < 0), ye - 6, s);
    } setcolor(WHITE);
}


// Draws the function whose name is used as an argument
void Plot(float func(float), int color = WHITE) {

    setcolor(color);

    for (float i = -(800 - X0) / k / 10; i < (800 - X0) / k / 10; i += dstep) {

        if (ScreenY(func(i)) >= 350 and ScreenY(func(i)) <= 450) {
            line(graphX(i), graphY(func(i)), graphX(i + dstep), graphY(func(i + dstep)));
        }
    } setcolor(WHITE);
}


// Draws the point
void Point(float x, float y, int color = WHITE) {
    int xe, ye;
    xe = graphX(x);
    ye = graphY(y);
    if (xe >= 0 and xe < 800 and ye >= 0 and ye < 800) { putpixel(xe, ye, color); }
}


// Makes the solutions
void Cross(float func1(float), float func2(float), float left_, float right_) {

    float eps = 0.001, delta = 2 * eps, mid, sol,
          left = left_,
          right = right_;
    bool  cond = 0;

    if ((right - left) / 2 > delta) {

        while (right - left > delta) {
            mid = (right + left - eps / 5) / 2;

            if ((func1(right) - func2(right)) * (func1(mid) - func2(mid)) <= 0) left = mid, cond = 0;
            else right = mid, cond = 1;
        }

        if ((func1(right) - func2(right)) * (func1(left) - func2(left)) <= 0) {

            sol = (left + right + eps) / 2; 
            solutions[kaunt++] = sol;

            if (!cond) Cross(func1, func2, left + eps, 5);
            else Cross(func1, func2, -5, right - eps);
        }
    }
}


// Builds the hatch in the bounded space
void Hatch(float func1(float), float func2(float)) {
    setcolor(DARKGRAY);

    for (float i = solutions[2]; i < solutions[0]; i += 0.3) {
        line(graphX(i), graphY(func1(i)), graphX(i), graphY(func2(i)));
    }

    setcolor(LIGHTBLUE);
    for (int i = 0; i < 3; i++) {

        sprintf(s, "x = %.3f", solutions[i]);
        outtextxy(graphX(solutions[i]) + 7, graphY(func1(solutions[i])) - 20, s);

        sprintf(s, "y = %.3f", func1(solutions[i]));
        outtextxy(graphX(solutions[i]) + 7, graphY(func1(solutions[i])), s);

        fillellipse(graphX(solutions[i]), graphY(func1(solutions[i])), 5, 5);
    }
    setcolor(WHITE);
}


// The right rectangle method to find the area
void Area_RRM(float func1(float), float func2(float), int cond) {

    float x = solutions[(cond) ? 2 : 1], S = 0;

    while (func2(x) > func1(x)) {
        S += func2(x) * dstep - func1(x) * dstep;
        x += dstep;
    }
    sprintf(s, "RRM"), outtextxy(10, 68, s); // 32 + 22 = 54 + 12
    if (cond) sprintf(s, "Area 1: %.3f", S), outtextxy(10, 90, s);
    else sprintf(s, "Area 2: %.3f", S), outtextxy(10, 112, s);
}


unsigned int RDVALUE_ = 1;

float RD(void) { // For Monte-Carlo method
    int A;
    RDVALUE_ = (RDVALUE_ + (unsigned int)(&A)) * 1103515245 + 12345;
    return RDVALUE_ / 4294967295.;
}


// The Monte-Carlo method for finding the area
void Area_MCM(float func1(float), float func2(float), int cond, int number) {
    float a = solutions[(cond) ? 2 : 1],
          b = solutions[(cond) ? 1 : 0],
          xi, S = 0;

    for (int i = 1; i < number; i++) { 
        xi = a + RD() * (b - a);
        S += func2(xi) - func1(xi); 
    }

    S *= (b - a) / number;

    sprintf(s, "MCM"), outtextxy(10, 148, s);
    if (cond) sprintf(s, "Area 1: %.3f", S), outtextxy(10, 170, s);
    else sprintf(s, "Area 2: %.3f", S), outtextxy(10, 192, s);
}


void Axes_() { // cringe
    int xe, ye;

    sprintf(s, ">"); outtextxy(ScreenX(50) + 8, ScreenY(0) - 8, s); // the arrows of the axis
    sprintf(s, "/\\"); outtextxy(ScreenX(0) - 3, ScreenY(50) - 23, s);

    settextstyle(2, 0, 4);

    line(X0, 0, X0, 1100); // the axis
    line(0, Y0, 1100, Y0);

    line(graphX(-5), graphY(-5), graphX(-5), graphY(5)); // the frame
    line(graphX(5), graphY(-5), graphX(5), graphY(5));
    line(graphX(-5), graphY(5), graphX(5), graphY(5));
    line(graphX(-5), graphY(-5), graphX(5), graphY(-5));

    sprintf(s, "0");
    outtextxy(ScreenX(0) - 12, ScreenY(0) + 4, s);

    sprintf(s, "-0.2"); // this value is repeated twice, so there is an overlap, which looks terrible
    outtextxy(ScreenX(0) - 26, ScreenY(0) + 14, s);
    
    for (int i = -50; i <= (1030 - X0) / k; i += 2) { // value and hatch setting (X axis)

        if (i) {
            xe = ScreenX(i);
            line(xe, Y0 - 2 - 3 * (i % 10 == 0), xe, Y0 + 2 + 3 * (i % 10 == 0));

            if (i != -2) {
                if (i > 0) {
                    sprintf(s, "%d.", i / 10); outtextxy(xe - 7, Y0 + 6, s); // this shit sends me the fuck up
                    sprintf(s, "%d", i % 10); outtextxy(xe + 1, Y0 + 6, s); //  cuz it cannot work with float vars
                }

                else {
                    if (i / 10 == 0) {
                        sprintf(s, "-%d.", i / 10); outtextxy(xe - 11, Y0 + 6, s);
                        sprintf(s, "%d", abs(i) % 10); outtextxy(xe, Y0 + 6, s);
                    }
                    else {
                        sprintf(s, "%d.", i / 10); outtextxy(xe - 10, Y0 + 6, s);
                        sprintf(s, "%d", abs(i) % 10); outtextxy(xe, Y0 + 6, s);
                    }
                }
            }
        }
    }

    for (int i = -50; i <= (1030 - Y0) / k; i += 2) { // value and hatch setting (Y axis)
        if (i) {
            ye = ScreenY(i);
            line(X0 - 2 - 3 * (i % 10 == 0), ye, X0 + 2 + 3 * (i % 10 == 0), ye);

            if (i != -2) {
                if (i > 0) {
                    sprintf(s, "%d.", i / 10); outtextxy(X0 - 22, ye - 4, s);
                    sprintf(s, "%d", i % 10); outtextxy(X0 - 14, ye - 4, s);
                }

                else {
                    if (i / 10 == 0) { sprintf(s, "-%d.", i / 10); }
                    else { sprintf(s, "%d.", i / 10); }
                    outtextxy(X0 - 26, ye - 4, s);
                    sprintf(s, "%d", abs(i) % 10); outtextxy(X0 - 14, ye - 4, s);
                }
            }
        }
    }
}