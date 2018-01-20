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
  int i;
  int a[100000];
  i = 0;
  while (i < 100000)
  {
    a[i] = 10;
    i = i + 1;
  }

  i = 0;
  while (i < 100000)
  {
    _1_PROVE[i] = a[i] == 10;
    printf("_1_PROVE[i]:%d\n", _1_PROVE[i]);
    printf("a[i]:%d\n", a[i]);
    printf("i:%d\n", i);
    printf("--------\n");
    if ((i + 1) != 15000)
    {
      a[i + 1] = 20;
    }

    i = i + 1;
  }

  return 0;
}
