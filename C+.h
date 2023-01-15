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

typedef int boolean;
#define false 0
#define true 1
#define FALSE 0
#define TRUE 1
#define False 0
#define True 1


 //=======================================================================//
//			printf

void cout(const char t[]) { for (int i = 0; t[i] != '\0'; i++) { printf("%c", t[i]); } }

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


 //=======================================================================//
//			file shit

#define ofstream(file, path) FILE* file = fopen(path, "w")
#define ifstream(file, path) FILE* file = fopen(path, "r")

void fout(FILE* file, const char text[]) { for (int i = 0; text[i] != '\0'; i++) { fprintf(file, "%c", text[i]); } }

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


 //=======================================================================//
//			MAX nd MIN



