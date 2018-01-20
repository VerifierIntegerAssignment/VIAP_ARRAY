#include <time.h>
#include <stdlib.h>
#include <stdio.h>
char _count_char='\0';
unsigned int _count=0;
int _count_int=0;
double _count_double=0.0;
float _count_float=0.0f;
int __VERIFIER_nondet_bool()
{
int value;
_count++;
srand(_count+(unsigned int)time(NULL));
srand(rand());
value=rand()%2;
if(value<0) value=-value;
return value;
}
char __VERIFIER_nondet_char()
{
char value;
_count_char++;
srand(_count_int+(char)time(NULL));
srand(rand());
value=rand()%1000;
if(value<0) value=-value;
return value;
}
int __VERIFIER_nondet_int()
{
int value;
 _count_int++;
srand(_count_int+(int)time(NULL));
 srand(rand());
value=rand()%1000;
if(value<0) value=-value;
return value;
}

unsigned int __VERIFIER_nondet_uint()
{
unsigned int value;
 _count++;
srand(_count+(unsigned int)time(NULL));
 srand(rand());
value=rand()%1000;
if(value<0) value=-value;
return value;
}

double __VERIFIER_nondet_double()
{
double value;
 _count++;
srand(_count_double+(double)time(NULL));
 srand(rand());
 value=rand()%1000;
if(value<0) value=-value;
return value;
}

float __VERIFIER_nondet_float()
{
float value;
 _count++;
srand(_count_float+(float)time(NULL));
 srand(rand());
 
 value=rand()%1000;
if(value<0) value=-value;
return value;
}
int main(){
  int _1_PROVE[1000000];
  int a1_var[100000];
  int a2_var[100000];
  int a3_var[100000];
  int a4_var[100000];
  int a5_var[100000];
  int a6_var[100000];
  int a7_var[100000];
  int a8_var[100000];
  int a9_var[100000];
  int a0_var[100000];
  int a;
  a = 0;
  while (a < 100000)
  {
    a1_var[a] = __VERIFIER_nondet_int();
    a9_var[a] = __VERIFIER_nondet_int();
    a = a + 1;
  }

  int i;
  i = 0;
  while (i < 100000)
  {
    a2_var[i] = a1_var[i];
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    a3_var[i] = a2_var[i];
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    a4_var[i] = a3_var[i];
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    a5_var[i] = a4_var[i];
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    a6_var[i] = a5_var[i];
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    a7_var[i] = a6_var[i];
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    a8_var[i] = a7_var[i];
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    a0_var[i] = a8_var[i];
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    a0_var[i] = a9_var[i];
    i = i + 1;
  }

  int x;
  x = 0;
  while (x < 100000)
  {
    _1_PROVE[x] = a1_var[x] == a0_var[x];
    printf("_1_PROVE[x]:%d\n", _1_PROVE[x]);
    printf("a1_var[x]:%d\n", a1_var[x]);
    printf("a:%d\n", a);
    printf("i:%d\n", i);
    printf("x:%d\n", x);
    printf("--------\n");
    x = x + 1;
  }

  return 0;
}
