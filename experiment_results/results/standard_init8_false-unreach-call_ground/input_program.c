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
  int a[100000];
  int i = 0;
  while (i < 100000)
  {
    a[i] = 42;
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    a[i] = 43;
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    a[i] = 44;
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    a[i] = 45;
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    a[i] = 46;
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    a[i] = 47;
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    a[i] = 48;
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    a[i] = 49;
    i = i + 1;
  }

  int x;
  x = 0;
  while (x < 100000)
  {
    _1_PROVE[x] = a[x] == 48;
    printf("_1_PROVE[x]:%d\n", _1_PROVE[x]);
    printf("a[x]:%d\n", a[x]);
    printf("i:%d\n", i);
    printf("x:%d\n", x);
    printf("--------\n");
    x = x + 1;
  }

  return 0;
}
