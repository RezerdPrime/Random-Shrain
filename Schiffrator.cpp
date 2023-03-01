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
    while ((sh < 48) or (sh > 50)) { cin >> sh; }
    
    if (sh == '0') {

        ifstream fin("a.txt");
        ofstream fout("b.txt"),
                 kout("key.txt");

        char sym;

        while (!fin.eof()) {
            sym = fin.get();

            if (!fin.eof() or sym != -1) {
                mov = RD() % 256;
                sym += mov;
                fout << sym;
                kout << mov << " ";
            }
        }
    }

    else if ((sh == '1') or (sh == '2')) {

        ifstream fin("b.txt"),
                 kin("key.txt");
        ofstream fout("c.txt");

        char sym;

        while (!kin.eof()) {
            kin >> mov;

            if (!kin.eof()) {

                sym = fin.get();
                if (sh == '1') sym -= mov;
                if (sh == '2') sym += mov;

                fout << sym;
            }
        }
    }
}
