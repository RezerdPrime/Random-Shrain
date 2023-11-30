// ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki ryadiki

#include <iostream>
#define ull unsigned long long
using namespace std;

ull power;

double f1(ull n) {
    return double(n - 1) / (power + n);
}

double f2(ull n) {
    return double(n) / power * ((n % 2 == 0) ? 1 : -1);
}

double SeriesSum(double func(ull), ull pwr, double eps, int begin) {
    power = pow(pwr, begin);
    double Sum = func(begin), 
           prevSum = 0;


    for (ull i = begin + 1; (abs(Sum - prevSum) > eps) or (Sum == 0 and prevSum == 0); i++) {
        prevSum = Sum;
        power *= pwr;
        Sum += func(i);
    }

    return Sum;
}

int main() {
    cout << "Sum: " << SeriesSum(f1, 3, 0.0000001, 1) << endl;
}
