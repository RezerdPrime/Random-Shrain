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
    cout << "  Set mode of Schiffrator:\n"
         << "  0 - random key generation (encryption mode)\n"
         << "  1 - manual key setting (decryption mode)\n\n";

    while ((sh < 48) or (sh > 49)) { cin >> sh; }
    
    if (sh == '0') {

        ifstream fin("orig.txt");
        ofstream fout("encrypted_codes.txt"),
                 thout("encrypted.txt"),
                 kout("key.txt");

        char sym;

        while (!fin.eof()) {
            sym = fin.get();

            if (!fin.eof()) {
                mov = RD() % 256;
                sym += mov;
                fout << (int)sym << " "; thout << sym;
                kout << mov << " ";
            }
        }
    }

    else if (sh == '1') {

        ifstream fin("encrypted_codes.txt"),
                 kin("key.txt");
        ofstream fout("decrypted.txt");

        int sym;

        while (!kin.eof()) {
            kin >> mov;

            if (!kin.eof()) {
                fin >> sym;
                sym -= mov;
                fout << (char)sym;
            }
        }
    }
}
