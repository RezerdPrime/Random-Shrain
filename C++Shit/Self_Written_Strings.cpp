#include <iostream>
using namespace std;

class str {
    friend ostream& operator<<(ostream&, const str&);
    friend istream& operator>>(istream&, str&);

public:

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

    str() = default;


    // Lol
    int size() {

        int i;
        for (i = 0; self[i] != '\0'; i++);
        return i;
    }


    // Indexed element
    char& operator[](int a) {
        int sz = size();

        if (a > 0 and sz) return self[a % sz];
        if (a < 0) return self[a + sz];

        return *(a + self);
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

        if (!a) return (str)"";

        if (a > 0) {
            char* nw = self;
            str b = nw;
            for (int i = 0; i < a - 1; i++) b = b + nw;
            return b;
        }

        if (a == -1) return -((str)self);

        if (a < 0) return -((str)self) * -a;
    }


    // String cutting
    str operator/(int sh) {
        int sz = size();

        if (!sh or !sz) return (str)"";

        if (sh > sz or sh < -sz) return (str)self;

        int cond = (sh > 0) ? 1 : -1;

        char* nw = new char[cond * sh + 1];
        for (int i = 0; i < cond * sh; i++) nw[i] = self[((sh > 0) ? i : sz - i - 1)];
        nw[cond * sh] = '\0';

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

    int count(char c) {
        int sz = size(), count = 0;

        for (int i = 0; i < sz; i++) {
            if (self[i] == c) count++;
        }
        return count;
    }

private:
    char* self = (char*)"";
};

std::ostream& operator<<(ostream& out, const str& s) {
    out << s.self;
    return out;
}

std::istream& operator>>(istream& in, str& s) {
    char* a = (char*)malloc(sizeof(char)); int i = 0;

    for (i;; i++) {
        a[i] = cin.get();

        if (a[i] == '\n') {
            a[i] = '\0';
            s = str(a); 
            return in;
        }

        a = (char*)realloc(a, sizeof(char) * (i + 2));
    }
}
