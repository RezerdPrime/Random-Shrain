#include <iostream>
#include <timecheck.cpp>
using namespace std;

int RDVALUE_ = 1;
#define RAND RD()

unsigned int RD(void) {
    unsigned int A;
    RDVALUE_ = (RDVALUE_ + (int)(&A)) * 1103515245 + 12345;
    return RDVALUE_ / 31;
}

int main() {

    int N; cin >> N;
    int* arr = new int[N];
    bool fliegen = true;

    for (int i = 0; i < N; i++) { 
        cin >> arr[i];
        cout << arr[i] << " ";
    }

    START

    while (fliegen) {

        bool flag = true;
        swap(arr[RAND % N], arr[RAND % N]);

        for (int i = 0; i < N - 1; i++) {
            flag = flag and (arr[i] <= arr[i + 1]);
        }

        fliegen = fliegen and !flag;
    }

    STOP

    cout << "\n\n";
    for (int i = 0; i < N; i++) cout << arr[i] << " ";
}
