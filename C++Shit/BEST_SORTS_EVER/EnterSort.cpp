    /*  
   //  Реализация лучшей сортировки из всех
  //   Она заставляет пользователя вводить массив до тех пор
 //    Пока не будет введён отсортированный массив
*/ 

#include <iostream>
using namespace std;

int main() {
    
    int N; cin >> N; int* arr = new int[N];
    bool nonstop = true;
    
    if (N <= 1) {
        int el; cin >> el; 
        cout << el; return 0;
    }

    while (nonstop) {

        int prev, cur; cin >> prev >> cur;
        short flag = 0;
        arr[0] = prev;
        arr[1] = cur;

        if (prev < cur) flag = 1;
        if (prev > cur) flag = 2;

        for (int i = 2; i < N; i++) {
            prev = cur; cin >> cur;

            if (prev > cur and flag == 1) {
                flag = -1; cout << "\nIDI NAHUY\n\n";
            }

            if (prev < cur and flag == 2) {
                flag = -1; cout << "\nIDI NAHUY\n\n";
            }

            if (prev < cur and !flag) {
                arr[i] = cur;
                flag = 1;
            }

            if (prev > cur and !flag) {
                arr[i] = cur;
                flag = 2;
            }

            if ((prev > cur and flag == 2) or (prev < cur and flag == 1) or (prev == cur)) {
                arr[i] = cur;
            }
        }

        if (flag == -1) continue;

        nonstop = false;
    }

    for (int i = 0; i < N; i++) {
        cout << arr[i] << " ";
    }
}
