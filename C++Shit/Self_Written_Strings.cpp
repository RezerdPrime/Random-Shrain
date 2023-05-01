#include <iostream>
using namespace	std;

struct str {


    // Convertation the char in the array of chars
    char* convert(char c) {
        char* a = new char[2];
        a[0] = c; a[1] = '\0';
        return a;
    }


    // Struct constructors
    str(char* s) : self(s) {}
    str(char c) : self(convert(c)) {}
    str(const char* s) : self((char*)s) {}


    // Lol
    int size() {

        int i;
        for (i = 0; self[i] != '\0'; i++);
        return i;
    }


    // Indexed element
    char operator[](int a) { 
        int sz = size();

        if (a > 0 and sz) return (char)self[a % sz];
        if (a < 0) return (char)self[a + sz];

        return (char)self[0];
    }


    // String concatenation
    str operator+(str s) {
  
        int s1 = size();
        int s2 = (s).size();

        char* nw = new char[s1 + s2 + 1];

        for (int i = 0; i < s1; i++) { nw[i] = self[i]; }
        for (int i = 0; i < s2; i++) { nw[i + s1] = s[i]; }

        nw[s1 + s2] = '\0'; return str(nw);
    }


    str operator+(const char* s) { return operator+((str)s); }
    str operator+(char* s) { return operator+((str)s); }


    // String reversing
    str operator-() {
        int siz = size();
        char* nw = new char[siz];

        for (int i = siz - 1; i > -1; i--) { nw[i] = self[siz - i - 1]; }
        nw[siz] = '\0';
        return str(nw);
    }


    // String duplication
    str operator*(int a) {

        char* nw = self;
        str b = nw;
        for (int i = 0; i < a - 1; i++) b = b + nw;
        return b;
    }


    // String cutting
    str operator/(int sh) {
        int sz = size();

        if (!sh or !sz) return (str)"";

        if (sh > sz or sh < -sz) return (str)self;

        char* nw = new char[((sh > 0) ? 1 : -1) * sh + 1];
        for (int i = 0; i < ((sh > 0) ? 1 : -1) * sh; i++) nw[i] = self[((sh > 0) ? i : sz - i - 1)];
        nw[((sh > 0) ? 1 : -1) * sh] = '\0';

        if (sh > 0) return (str)nw;
        else return -(str)nw;
    }


    // Substring finding
    int find(str substr) {
        int self_sz = size();
        int sub_sz = substr.size();

        if (sub_sz > self_sz or !self_sz or !sub_sz) return -1;

        bool flg = true;

        for (int i = 0; i <= self_sz - sub_sz; i++) {
            for (int j = 0; (j < sub_sz) and flg; j++) {
                flg = flg and (substr[j] == self[i + j]);
            }

            if (flg) return i;
            flg = true;
        }

        return -1;
    }


    // Type "str" convertation to array of the chars
    char* convert() { return self; }

#define cout(s) cout << (s).convert();


    // The fucking replace
    str replace(str old, str nw) {

        int self_sz = size(),
            new_sz = nw.size(),
            old_sz = old.size();

        if (old_sz > self_sz or !old_sz or !self_sz) return str(self);

        int index = find(old);

        if (index == -1) return str(self);

        return (str(self) / index) + nw + (str(self) / -(self_sz - index - old_sz));
    }

private:
    char* self;
};


//int main() {
//    str a = "foo";
//    str b = "bar";
//    cout << (a + b).convert();
//}
// оап сасать
