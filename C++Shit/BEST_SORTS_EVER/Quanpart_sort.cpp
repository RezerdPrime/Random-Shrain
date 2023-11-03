#include <iostream>
using namespace std;

int main(){
    bool not_sorted = true,
        inc_order = true,
        dec_order = true;

    int arr_size; cin >> arr_size;

    if (arr_size == 0) {
        cout << "\n";
        return 0;
    }

    if (arr_size == 1) {
        int a; 
        cin >> a; cout << a;
        return 0;
    }

    if (arr_size == 2) {
        int a, b; cin >> a >> b;
        cout << a << " " << b << endl;
        return 0;
    }

    auto arr = new int[arr_size];
    for (int i = 0; i < arr_size; i++) cin >> arr[i];

    while (not_sorted) {
        for (int i = 0; i < arr_size - 1; i++) {
            inc_order &= arr[i] <= arr[i + 1];
            dec_order &= arr[i] >= arr[i + 1];

        }

        not_sorted = !(inc_order or dec_order);
    }

    for (int i = 0; i < arr_size; i++) cout << arr[i] << " ";
}

/*
There is an incredibly low chance that a quantum particle will pass through your computer
and change some bit of memory in it. 

Purely theoretically, there is a non-zero probability
that many such particles will change the bit information in an array so that it becomes sorted.
*/
