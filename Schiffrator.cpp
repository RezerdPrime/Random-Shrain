#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
using namespace std;

int schiff;

int main()
{
    cin >> schiff;
    if (schiff) {

        ifstream fin("a.txt");
        ofstream fout("b.txt");

        srand(time(NULL));

        auto text = (char*)malloc(sizeof(char));
        char sym = 1; int index = 0, inversible_bit;
        string key = "";

        while (!fin.eof()) {
            inversible_bit = rand() % 8; key += to_string(inversible_bit);

            sym = fin.get(); //cout << (int)sym << " ";
            sym ^= 1 << inversible_bit; //cout << (int)sym << endl;

            text[index] = sym;
            index++;
            text = (char*)realloc(text, sizeof(char) * (index + 1));
        }

        for (int i = 0; i < index - 1; i++) {
            fout << (char)text[i];
        }

        cout << key << endl;
    }


    else {

        ifstream fin("b.txt");
        ofstream fout("c.txt");

        int number; cin >> number;
        auto key = (char*)malloc(sizeof(char) * number);

        for (int i = 0; i < number; i++) {
            cin >> key[i];
        }

        auto text = (char*)malloc(sizeof(char));
        char sym = 1; int index = 0, inversible_bit;

        for (int i = 0; i < number; i++) {
            inversible_bit = (int)key[i] - 48;

            sym = fin.get(); //cout << (int)sym << " ";
            sym ^= 1 << inversible_bit; //cout << (int)sym << endl;

            text[index] = sym;
            index++;
            text = (char*)realloc(text, sizeof(char) * (index + 1));
        }

        for (int i = 0; i < index - 1; i++) {
            fout << (char)text[i];
        }
    }
}
