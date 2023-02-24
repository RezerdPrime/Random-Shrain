#include <iostream>
#include <fstream>
using namespace std;

int RDVALUE_ = 1, sh, mov;

int RD(void) {
    int A;
    RDVALUE_ = (RDVALUE_ + (int)(&A)) * 1103515245 + 12345;
    return RDVALUE_ / 31;
}

int main()
{
    cin >> sh;

    if (sh) {
        ifstream fin("a.txt");
        ofstream fout("b.txt");

        char sym;
        int leng = 0; auto key = (int*)malloc(sizeof(int));

        while (!fin.eof()) {
            sym = fin.get(); //cout << (int)sym << " ";
            if (!fin.eof() or sym != -1) {
                mov = RD();
                sym += mov;
                fout << sym;

                leng++; key = (int*)realloc(key, (leng + 1) * sizeof(int));
                key[leng - 1] = mov;
            }
        }

        fin.close(); fout.close();
        ofstream keyout("a.txt");
        for (int i = 0; i < leng; i++) { keyout << key[i] << " "; }
    }

    else {
        ifstream fin("b.txt");
        ofstream fout("c.txt");

        char sym;

        while (!fin.eof()) {
            sym = fin.get();
            if (!fin.eof()) {
                cin >> mov;
                sym -= mov;
                fout << sym;
            }
        }
    }
}
