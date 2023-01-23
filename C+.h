#ifndef C_PLUS
#define C_PLUS

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//=======================================================================//
//			Comfortable stuff

#define elif else if
#define and &&
#define or ||

#define CH char
#define UCH unsigned char
#define SH short
#define USH unsigned short
#define IN int
#define UIN unsigned int
#define LL long long
#define ULL unsigned long long
#define FL float
#define DB double
#define LD long double

#define D106 1000000
#define D109 1000000000
#define D231 2147483647
#define D263 9223372036854775807
#define Fpi 3.1415926535897932384626433832795
#define Fe 2.7182818284590452353602874713527

typedef int bool;
#define false 0
#define true 1
#define FALSE 0
#define TRUE 1
#define False 0
#define True 1


//=======================================================================//
//			type function

enum types
{
    t_CHAR = 1, t_UCHAR,
    t_SHORT, t_USHORT,
    t_INT, t_UINT,
    t_LL, t_ULL,

    t_FLOAT,
    t_DOUBLE,
    t_LDOUBLE,

    t_VOID = 0,
};

typedef int type_var;

type_var type_ch(CH var) { return t_CHAR; }
type_var type_uch(UCH var) { return t_UCHAR; }

type_var type_sh(SH var) { return t_SHORT; }
type_var type_ush(USH var) { return t_USHORT; }

type_var type_in(IN var) { return t_INT; }
type_var type_uin(UIN var) { return t_UINT; }

type_var type_ll(LL var) { return t_LL; }
type_var type_ull(ULL val) { return t_ULL; }

type_var type_fl(FL var) { return t_FLOAT; }
type_var type_dbl(DB var) { return t_DOUBLE; }
type_var type_ldbl(LD var) { return t_LDOUBLE; }

type_var type_void(void) { return t_VOID; }

#define type(x)                 \
        _Generic((x),           \
        CH: type_ch,            \
        UCH: type_uch,          \
        SH: type_sh,            \
        USH: type_ush,          \
        IN: type_in,            \
        UIN: type_uin,          \
        LL: type_ll,            \
        ULL: type_ull,          \
        FL: type_fl,            \
        DB: type_dbl,           \
        LD: type_ldbl,          \
        default: type_void      \
)(x)

//=======================================================================//
//			printf

void cout_st(CH* t) { printf("%s", t); }

void cout_ch(CH var) { printf("%c", var); }
void cout_uch(UCH var) { printf("%c", var); }

void cout_sh(SH var) { printf("%d", var); }
void cout_ush(USH var) { printf("%d", var); }

void cout_in(IN var) { printf("%d", var); }
void cout_uin(UIN var) { printf("%d", var); }

void cout_ll(LL var) { printf("%lld", var); }
void cout_ull(ULL var) { printf("%llu", var); }

void cout_fl(FL var) { printf("%f", var); }
void cout_dbl(DB var) { printf("%g", var); }
void cout_ldbl(LD var) { printf("%lg", var); }

#define cout_(x)            \
        _Generic((x),       \
        CH*: cout_st,       \
        CH: cout_ch,        \
        UCH: cout_uch,      \
        SH: cout_sh,        \
        USH: cout_ush,      \
        IN: cout_in,        \
        UIN: cout_uin,      \
        LL: cout_ll,        \
        ULL: cout_ull,      \
        FL: cout_fl,        \
        DB: cout_dbl,       \
        LD: cout_ldbl,      \
        default: cout_in    \
)(x)

#define cout_1(a) cout_(a);
#define cout_2(a, b) cout_1(a); cout_(b);
#define cout_3(a, b, c) cout_2(a, b); cout_(c);
#define cout_4(a, b, c, d) cout_3(a, b, c); cout_(d);
#define cout_5(a, b, c, d, e) cout_4(a, b, c, d); cout_(e);
#define cout_6(a, b, c, d, e, f) cout_5(a, b, c, d, e); cout_(f);
#define cout_7(a, b, c, d, e, f, g) cout_6(a, b, c, d, e, f); cout_(g);
#define cout_8(a, b, c, d, e, f, g, h) cout_7(a, b, c, d, e, f, g); cout_(h);
#define cout_9(a, b, c, d, e, f, g, h, i) cout_8(a, b, c, d, e, f, g, h); cout_(i);
#define cout_10(a, b, c, d, e, f, g, h, i, j) cout_9(a, b, c, d, e, f, g, h, i); cout_(j);

#define CAT1(x,y) CAT1_(x,y)
#define CAT1_(x,y) x##y
#define VA_COUNT(...) VA_COUNT_(__VA_ARGS__,10,9,8,7,6,5,4,3,2,1,0)
#define VA_COUNT_(x10,x9,x8,x7,x6,x5,x4,x3,x2,x1,x0,...) x0
#define cout(...) CAT1(cout_,VA_COUNT(__VA_ARGS__))(__VA_ARGS__)

#define __ ," ",
#define n_ ,"\n",
#define t_ ,"\t",


//=======================================================================//
//			scanf

void cin_ch(CH* var) { CH buf = getchar(); *var = *(&buf); }
void cin_uch(UCH* var) { UCH buf = getchar(); *var = *(&buf); }

void cin_sh(SH* var) { SH buf; scanf("%hi", &buf); *var = *(&buf); }
void cin_ush(USH* var) { USH buf; scanf("%hu", &buf); *var = *(&buf); }

void cin_in(IN* var) { IN buf; scanf("%d", &buf); *var = *(&buf); }
void cin_uin(UIN* var) { UIN buf; scanf("%u", &buf); *var = *(&buf); }

void cin_ll(LL* var) { LL buf; scanf("%lli", &buf); *var = *(&buf); }
void cin_ull(ULL* var) { ULL buf; scanf("%llu", &buf); *var = *(&buf); }

void cin_fl(FL* var) { FL buf; scanf("%f", &buf); *var = *(&buf); }

void cin_dbl(DB* var) { DB buf; scanf("%g", &buf); *var = *(&buf); }

void cin_ldbl(LD* var) { LD buf; scanf("%lg", &buf); *var = *(&buf); }

#define cin__(x)                \
        _Generic((x),           \
        CH*: cin_ch,            \
        UCH*: cin_uch,          \
        SH*: cin_sh,            \
        USH*: cin_ush,          \
        IN*: cin_in,            \
        UIN*: cin_uin,          \
        LL*: cin_ll,            \
        ULL*: cin_ull,          \
        FL*: cin_fl,            \
        DB*: cin_dbl,           \
        LD*: cin_ldbl,          \
        default: cin_in         \
)(x)

#define cin_(x) cin__(&x)
#define cin_1(a) cin_(a);
#define cin_2(a, b) cin_1(a) cin_(b);
#define cin_3(a, b, c) cin_2(a, b) cin_(c);
#define cin_4(a, b, c, d) cin_3(a, b, c) cin_(d);
#define cin_5(a, b, c, d, e) cin_4(a, b, c, d) cin_(e);
#define cin_6(a, b, c, d, e, f) cin_5(a, b, c, d, e) cin_(f);
#define cin_7(a, b, c, d, e, f, g) cin_6(a, b, c, d, e, f) cin_(g);
#define cin_8(a, b, c, d, e, f, g, h) cin_7(a, b, c, d, e, f, g) cin_(h);
#define cin_9(a, b, c, d, e, f, g, h, i) cin_8(a, b, c, d, e, f, g, h) cin_(i);
#define cin_10(a, b, c, d, e, f, g, h, i, j) cin_9(a, b, c, d, e, f, g, h, i) cin_(j);

#define CAT2(x,y) CAT2_(x,y)
#define CAT2_(x,y) x##y
#define VA_COUNT(...) VA_COUNT_(__VA_ARGS__,10,9,8,7,6,5,4,3,2,1,0)
#define VA_COUNT_(x10,x9,x8,x7,x6,x5,x4,x3,x2,x1,x0,...) x0
#define cin(...) CAT2(cin_,VA_COUNT(__VA_ARGS__))(__VA_ARGS__)


//=======================================================================//
//			file shit

#define ofstream(file, path) FILE* file = fopen(path, "w")
#define ifstream(file, path) FILE* file = fopen(path, "r")

void fout_st(FILE* file, CH* text) { fprintf(file, "%s", text); }

void fout_ch(FILE* file, CH var) { fprintf(file, "%c", var); }
void fout_uch(FILE* file, UCH var) { fprintf(file, "%c", var); }

void fout_sh(FILE* file, SH var) { fprintf(file, "%hi", var); }
void fout_ush(FILE* file, USH var) { fprintf(file, "%hi", var); }

void fout_in(FILE* file, IN var) { fprintf(file, "%d", var); }
void fout_uin(FILE* file, UIN var) { fprintf(file, "%u", var); }

void fout_ll(FILE* file, LL var) { fprintf(file, "%lld", var); }
void fout_ull(FILE* file, ULL var) { fprintf(file, "%llu", var); }

void fout_fl(FILE* file, FL var) { fprintf(file, "%f", var); }

void fout_dbl(FILE* file, DB var) { fprintf(file, "%g", var); }

void fout_ldbl(FILE* file, LD var) { fprintf(file, "%lg", var); }

#define fout_(file, x)          \
        _Generic((file, x),     \
        CH*: fout_st,           \
        CH: fout_ch,            \
        UCH: fout_uch,          \
        SH: fout_sh,            \
        USH: fout_ush,          \
        IN: fout_in,            \
        UIN: fout_uin,          \
        LL: fout_ll,            \
        ULL: fout_ull,          \
        FL: fout_fl,            \
        DB: fout_dbl,           \
        LD: fout_ldbl,          \
        default: fout_in        \
)(file, x)

#define fout_1(file, a) fout_(file, a);
#define fout_2(file, a, b) fout_1(file, a); fout_(file, b);
#define fout_3(file, a, b, c) fout_2(file, a, b); fout_(file, c);
#define fout_4(file, a, b, c, d) fout_3(file, a, b, c); fout_(file, d);
#define fout_5(file, a, b, c, d, e) fout_4(file, a, b, c, d); fout_(file, e);
#define fout_6(file, a, b, c, d, e, f) fout_5(file, a, b, c, d, e); fout_(file, f);
#define fout_7(file, a, b, c, d, e, f, g) fout_6(file, a, b, c, d, e, f); fout_(file, g);
#define fout_8(file, a, b, c, d, e, f, g, h) fout_7(file, a, b, c, d, e, f, g); fout_(file, h);
#define fout_9(file, a, b, c, d, e, f, g, h, i) fout_8(file, a, b, c, d, e, f, g, h); fout_(file, i);
#define fout_10(file, a, b, c, d, e, f, g, h, i, j) fout_9(file, a, b, c, d, e, f, g, h, i) fout_(file, j);

//#define FCAT1(x,y) FCAT1_(x,y)
//#define FCAT1_(x,y) x##y
//#define VA_COUNT(...) VA_COUNT_(__VA_ARGS__,10,9,8,7,6,5,4,3,2,1,0)
//#define VA_COUNT_(x10,x9,x8,x7,x6,x5,x4,x3,x2,x1,x0,...) x0
//#define fout(...) FCAT1(fout_,VA_COUNT(__VA_ARGS__))(__VA_ARGS__)

// как передавать обязательный аргумент блять


#define fin_(file, x) fin__(file, &x) // fin() типа для общей функции с перегрузкой по количеству аргументов

void fin_ch(FILE* file, CH* var) { CH buf = getc(file); *var = *(&buf); }
void fin_uch(FILE* file, UCH* var) { UCH buf = getc(file); *var = *(&buf); }

void fin_sh(FILE* file, SH* var) { SH buf; fscanf(file, "%hi", &buf); *var = *(&buf); }
void fin_ush(FILE* file, USH* var) { USH buf; fscanf(file, "%hu", &buf); *var = *(&buf); }

void fin_in(FILE* file, IN* var) { IN buf; fscanf(file, "%d", &buf); *var = *(&buf); }
void fin_uin(FILE* file, UIN* var) { UIN buf; fscanf(file, "%u", &buf); *var = *(&buf); }

void fin_ll(FILE* file, LL* var) { LL buf; fscanf(file, "%lld", &buf); *var = *(&buf); }
void fin_ull(FILE* file, ULL* var) { ULL buf; fscanf(file, "%llu", &buf); *var = *(&buf); }

void fin_fl(FILE* file, FL* var) { FL buf; fscanf(file, "%f", &buf); *var = *(&buf); }

void fin_dbl(FILE* file, DB* var) { DB buf; fscanf(file, "%g", &buf); *var = *(&buf); }

void fin_ldbl(FILE* file, LD* var) { LD buf; fscanf(file, "%lg", &buf); *var = *(&buf); }

#define fin__(file, x)          \
        _Generic((file, x),     \
        CH*: fin_ch,            \
        UCH*: fin_uch,          \
        SH*: fin_sh,            \
        USH*: fin_ush,          \
        IN*: fin_in,            \
        UIN*: fin_uin,          \
        LL*: fin_ll,            \
        ULL*: fin_ull,          \
        FL*: fin_fl,            \
        DB*: fin_dbl,           \
        LD*: fin_ldbl,          \
        default: fin_in         \
)(file, x)

#define fin_1(file, a) fin_(file, a);
#define fin_2(file, a, b) fin_1(file, a) fin_(file, b);
#define fin_3(file, a, b, c) fin_2(file, a, b) fin_(file, c);
#define fin_4(file, a, b, c, d) fin_3(file, a, b, c) fin_(file, d);
#define fin_5(file, a, b, c, d, e) fin_4(file, a, b, c, d) fin_(file, e);
#define fin_6(file, a, b, c, d, e, f) fin_5(file, a, b, c, d, e) fin_(file, f);
#define fin_7(file, a, b, c, d, e, f, g) fin_6(file, a, b, c, d, e, f) fin_(file, g);
#define fin_8(file, a, b, c, d, e, f, g, h) fin_7(file, a, b, c, d, e, f, g) fin_(file, h);
#define fin_9(file, a, b, c, d, e, f, g, h, i) fin_8(file, a, b, c, d, e, f, g, h) fin_(file, i);
#define fin_10(file, a, b, c, d, e, f, g, h, i, j) fin_9(file, a, b, c, d, e, f, g, h, i) fin_(file, j);

// тут должна быть реализация перегрузки по кол-ву аргументов

#endif //C_PLUS

//=======================================================================//
//			ChangeLog

/*
15.01.2023 - Первый релиз
23.01.2023 - Осознание того, что я долбаёб и пишу сишную библиотеку в файле с расширением .cpp
             Реализация перегрузки для функций type(), cout(), cin()
*/
