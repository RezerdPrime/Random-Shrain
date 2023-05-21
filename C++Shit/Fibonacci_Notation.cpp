#include <iostream>
using namespace std;

int cond = 1;

int main() {

    cin >> cond;

    if (cond) {

        cout << "Set the decimal number: \n";

        int fib1 = 1, fib2 = 2, ind = 0;
        unsigned long long number; cin >> number;
        unsigned long long* arr = (unsigned long long*)malloc(sizeof(unsigned long long) * (ind + 1));

        do {

            //cout << number % fib2 << " ";
            arr[ind] = number % fib2; //cout << arr[ind] << " ";
            ind++; arr = (unsigned long long*)realloc(arr, (ind + 1) * sizeof(unsigned long long));
            number /= fib2;

            fib2 += fib1;
            fib1 = fib2 - fib1;

        } while (number);

        for (int i = ind - 1; i >= 0; i--) { cout << arr[i] << ' '; }
        //((unsigned long long)1 << 64 - 1) 9223372036854775807
    }

    else {

        cout << "Set the number in Fibonacci notation: \n";

        int cur = 0, ind = 0;
        unsigned long long* arr = (unsigned long long*)malloc(sizeof(unsigned long long) * (ind + 1));
        int fib1 = 0, fib2 = 1;

        do {
            if (cur >= 0) {
                cin >> cur;
                arr[ind] = cur;
                ind++; arr = (unsigned long long*)realloc(arr, (ind + 1) * sizeof(unsigned long long));

                fib2 += fib1;
                fib1 = fib2 - fib1;
            }

        } while (cur >= 0);

        unsigned long long res = arr[0] * fib1;

        for (int i = 1; i < ind - 1; i++) {

            fib1 = fib2 - fib1;
            fib2 -= fib1;

            res += arr[i];
            res *= fib1;
        }

        cout << res;
    }
}
