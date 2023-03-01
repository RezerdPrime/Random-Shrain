#include <iostream>
#include <fstream>
using namespace std;

int RDVALUE_ = 1, mov; char sh;

int RD(void) {
    int A;
    RDVALUE_ = (RDVALUE_ + (int)(&A)) * 1103515245 + 12345;
    return RDVALUE_ / 31;
}

int main()
{
    cout << "Set mode of Schiffrator:\n"
         << "0 - random key generation\n"
         << "1 - manual key setting (decryption mode)\n"
         << "2 - manual key setting (encryption mode)\n\n";

    while ((sh != '0') and (sh != '1') and (sh != '2')) { cin >> sh; }
    if (sh == '0') {

        ifstream fin("a.txt");
        ofstream fout("b.txt");

        char sym;
        int leng = 0; auto key = (int*)malloc(sizeof(int));

        while (!fin.eof()) {
            sym = fin.get();
            if (!fin.eof() or sym != -1) {
                mov = RD() % 256;
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

    else if ((sh == '1') or (sh == '2')) {
        ifstream fin("b.txt");
        ofstream fout("c.txt");

        char sym; int len;
        cout << "Set the length of key:\n\n";
        cin >> len;

        while (len) {
            sym = fin.get();
            if (len) {
                cin >> mov;

                if (sh == '1') sym -= mov;
                if (sh == '2') sym += mov;
                
                fout << sym; len--;
            }
        }
    }
}
