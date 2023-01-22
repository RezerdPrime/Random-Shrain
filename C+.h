#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

 //=======================================================================//
//			type function

enum types 
{
	t_CHAR = 1,		 t_UCHAR,
	t_SHORT,		 t_USHORT,
	t_INT,			 t_UINT,
	t_LL,			 t_ULL,

	t_FLOAT,
	t_DOUBLE,
	t_LDOUBLE,
	t_VOID = 0,
};

typedef int type_var;

type_var type(char var) { return t_CHAR; }
type_var type(unsigned char var) { return t_UCHAR; }

type_var type(short var) { return t_SHORT; }
type_var type(unsigned short var) { return t_USHORT; }

type_var type(int var) { return t_INT; }
type_var type(unsigned int var) { return t_UINT; }

type_var type(long long var) { return t_LL; }
type_var type(unsigned long long val) { return t_ULL; }

type_var type(float var) { return t_FLOAT; }
type_var type(double var) { return t_DOUBLE; }
type_var type(long double var) { return t_LDOUBLE; }

type_var type(void) { return t_VOID; }

 //=======================================================================//
//			Comfortable stuff

#define elif else if
#define ULL unsigned long long
#define LL long long
#define UN unsigned
#define LD long double
#define D106 1000000
#define D109 1000000000
#define D231 2147483647
#define D263 9223372036854775807
#define Fpi 3.1415926535897932384626433832795
#define Fe 2,7182818284590452353602874713527

typedef int bul;
#define false 0
#define true 1
#define FALSE 0
#define TRUE 1
#define False 0
#define True 1


 //=======================================================================//
//			printf

#define ___ ;cout(" ");
#define _n_ ;cout("\n");
#define _t_ ;cout("\t");

#define __ ___;
#define n_ _n_;
#define t_ _t_;

void cout(const char t[]) { printf("%s", t); } 

void cout(char var) { printf("%c", var); }
void cout(UN char var) { printf("%c", var); }

void cout(short var) { printf("%d", var); }
void cout(UN short var) { printf("%d", var); }

void cout(int var) { printf("%d", var); }
void cout(UN int var) { printf("%d", var); }

void cout(LL var) { printf("%lld", var); }
void cout(ULL var) { printf("%llu", var); }

void cout(float var) { printf("%f", var); }
void cout(double var) { printf("%g", var); }
void cout(LD var) { printf("%lg", var); }

#define cout1(a) cout(a);
#define cout2(a, b) cout1(a) cout(b);
#define cout3(a, b, c) cout2(a, b) cout(c);
#define cout4(a, b, c, d) cout3(a, b, c) cout(d);
#define cout5(a, b, c, d, e) cout4(a, b, c, d) cout(e);
#define cout6(a, b, c, d, e, f) cout5(a, b, c, d, e) cout(f);
#define cout7(a, b, c, d, e, f, g) cout6(a, b, c, d, e, f) cout(g);
#define cout8(a, b, c, d, e, f, g, h) cout7(a, b, c, d, e, f, g) cout(h);
#define cout9(a, b, c, d, e, f, g, h, i) cout8(a, b, c, d, e, f, g, h) cout(i);
#define cout0(a, b, c, d, e, f, g, h, i, j) cout9(a, b, c, d, e, f, g, h, i) cout(j);

/*

And yes, u should to set number of agruments. 
It's underscores why the library is named "C+.h".

*/


 //=======================================================================//
//			scanf

#define cin(x) cin_(&x) 

void cin_(char* var) { char buf = getchar(); *var = *(&buf); }
void cin_(UN char* var) { UN char buf = getchar(); *var = *(&buf); }

void cin_(short* var) { short buf; scanf("%hi", &buf); *var = *(&buf); }
void cin_(UN short* var) { UN short buf; scanf("%hu", &buf); *var = *(&buf); }

void cin_(int* var) { int buf; scanf("%d", &buf); *var = *(&buf); }
void cin_(UN int* var) { UN int buf; scanf("%u", &buf); *var = *(&buf); }

void cin_(LL* var) { LL buf; scanf("%lli", &buf); *var = *(&buf); }
void cin_(ULL* var) { ULL buf; scanf("%llu", &buf); *var = *(&buf); }

void cin_(float* var) { float buf; scanf("%f", &buf); *var = *(&buf); }

void cin_(double* var) { double buf; scanf("%g", &buf); *var = *(&buf); }

void cin_(LD* var) { LD buf; scanf("%lg", &buf); *var = *(&buf); }

#define cin1(a) cin(a);
#define cin2(a, b) cin1(a) cin(b);
#define cin3(a, b, c) cin2(a, b) cin(c);
#define cin4(a, b, c, d) cin3(a, b, c) cin(d);
#define cin5(a, b, c, d, e) cin4(a, b, c, d) cin(e);
#define cin6(a, b, c, d, e, f) cin5(a, b, c, d, e) cin(f);
#define cin7(a, b, c, d, e, f, g) cin6(a, b, c, d, e, f) cin(g);
#define cin8(a, b, c, d, e, f, g, h) cin7(a, b, c, d, e, f, g) cin(h);
#define cin9(a, b, c, d, e, f, g, h, i) cin8(a, b, c, d, e, f, g, h) cin(i);
#define cin0(a, b, c, d, e, f, g, h, i, j) cin9(a, b, c, d, e, f, g, h, i) cin(j);


 //=======================================================================//
//			file shit

#define ofstream(file, path) FILE* file = fopen(path, "w")
#define ifstream(file, path) FILE* file = fopen(path, "r")

//void fout(FILE* file, const char text[]) { for (int i = 0; text[i] != '\0'; i++) { fprintf(file, "%c", text[i]); } }
void fout(FILE* file, const char text[]) { fprintf(file, "%s", text); }

void fout(FILE* file, char var) { fprintf(file, "%c", var); }
void fout(FILE* file, UN char var) { fprintf(file, "%c", var); }

void fout(FILE* file, short var) { fprintf(file, "%hi", var); }
void fout(FILE* file, UN short var) { fprintf(file, "%hi", var); }

void fout(FILE* file, int var) { fprintf(file, "%d", var); }
void fout(FILE* file, UN int var) { fprintf(file, "%u", var); }

void fout(FILE* file, LL var) { fprintf(file, "%lld", var); }
void fout(FILE* file, ULL var) { fprintf(file, "%llu", var); }

void fout(FILE* file, float var) { fprintf(file, "%f", var); }

void fout(FILE* file, double var) { fprintf(file, "%g", var); }

void fout(FILE* file, LD var) { fprintf(file, "%lg", var); }

#define fout1(file, a) fout(file, a);
#define fout2(file, a, b) fout1(file, a) fout(file, b);
#define fout3(file, a, b, c) fout2(file, a, b) fout(file, c);
#define fout4(file, a, b, c, d) fout3(file, a, b, c) fout(file, d);
#define fout5(file, a, b, c, d, e) fout4(file, a, b, c, d) fout(file, e);
#define fout6(file, a, b, c, d, e, f) fout5(file, a, b, c, d, e) fout(file, f);
#define fout7(file, a, b, c, d, e, f, g) fout6(file, a, b, c, d, e, f) fout(file, g);
#define fout8(file, a, b, c, d, e, f, g, h) fout7(file, a, b, c, d, e, f, g) fout(file, h);
#define fout9(file, a, b, c, d, e, f, g, h, i) fout8(file, a, b, c, d, e, f, g, h) fout(file, i);
#define fout0(file, a, b, c, d, e, f, g, h, i, j) fout9(file, a, b, c, d, e, f, g, h, i) fout(file, j);

//

#define fin(file, x) fin_(file, &x)

void fin_(FILE* file, char* var) { char buf = getc(file); *var = *(&buf); }
void fin_(FILE* file, UN char* var) { UN char buf = getc(file); *var = *(&buf); }

void fin_(FILE* file, short* var) { short buf; fscanf(file, "%hi", &buf); *var = *(&buf); }
void fin_(FILE* file, UN short* var) { UN short buf; fscanf(file, "%hu", &buf); *var = *(&buf); }

void fin_(FILE* file, int* var) { int buf; fscanf(file, "%d", &buf); *var = *(&buf); }
void fin_(FILE* file, UN int* var) { UN int buf; fscanf(file, "%u", &buf); *var = *(&buf); }

void fin_(FILE* file, LL* var) { LL buf; fscanf(file, "%lld", &buf); *var = *(&buf); }
void fin_(FILE* file, ULL int* var) { ULL buf; fscanf(file, "%llu", &buf); *var = *(&buf); }

void fin_(FILE* file, float* var) { float buf; fscanf(file, "%f", &buf); *var = *(&buf); }

void fin_(FILE* file, double* var) { double buf; fscanf(file, "%g", &buf); *var = *(&buf); }

void fin_(FILE* file, LD* var) { LD buf; fscanf(file, "%lg", &buf); *var = *(&buf); }

#define fin1(file, a) fin(file, a);
#define fin2(file, a, b) fin1(file, a) fin(file, b);
#define fin3(file, a, b, c) fin2(file, a, b) fin(file, c);
#define fin4(file, a, b, c, d) fin3(file, a, b, c) fin(file, d);
#define fin5(file, a, b, c, d, e) fin4(file, a, b, c, d) fin(file, e);
#define fin6(file, a, b, c, d, e, f) fin5(file, a, b, c, d, e) fin(file, f);
#define fin7(file, a, b, c, d, e, f, g) fin6(file, a, b, c, d, e, f) fin(file, g);
#define fin8(file, a, b, c, d, e, f, g, h) fin7(file, a, b, c, d, e, f, g) fin(file, h);
#define fin9(file, a, b, c, d, e, f, g, h, i) fin8(file, a, b, c, d, e, f, g, h) fin(file, i);
#define fin0(file, a, b, c, d, e, f, g, h, i, j) fin9(file, a, b, c, d, e, f, g, h, i) fin(file, j);


 //=======================================================================//
//			Dynamic arrays

#include <windows.h>

#define arr_init0(arr, size, type)				type* arr = (type*)calloc(size, sizeof(type));
#define arr2D_init0(arr, size1, size2, type)	type** arr = (type**)calloc(size1, sizeof(type*)); for (int i = 0; i < size1; i++) { arr[i] = (type*)calloc(size2, sizeof(type)); }

#define arr_init(arr, size, type)				type* arr = new type[size];
#define arr2D_init(arr, size1, size2, type)		type** arr = new type*[size1]; for (int i = 0; i < size1; i++) { arr[i] = new type[size2]; }

#define mout(arr, size) for (int i = 0; i < size; i++) { cout(arr[i]) __ }
#define mout2D(arr, size1, size2) for (int i = 0; i < size1; i++) { mout(arr[i], size2) n_ }


 //=======================================================================//
//		ChangeLog

/*
15.01.2023 - First release
16.01.2023 - Dynamic arrays macros and functions added
22.01.2023 - Added macros for one millon, billion, max of int, max of LL, Pi, Euler constant,
	     Added extended macros for "cout" and "cin", "fout" and "fin". 
	     Added macros for array's outputing
-
*/
