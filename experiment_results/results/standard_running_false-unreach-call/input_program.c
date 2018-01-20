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
  int _1_PROVE = 0;
  int a[10];
  int b[10];
  int i = 0;
  while (i < 10)
  {
    if (a[i] >= 0)
    {
      b[i] = 1;
    }
    else
    {
      b[i] = 0;
    }

    i = i + 1;
  }

  int f = 1;
  i = 0;
  while (i < 10)
  {
    if ((a[i] >= 0) && (! b[i]))
    {
      f = 0;
    }

    if ((a[i] < 0) && (! b[i]))
    {
      f = 0;
    }

    i = i + 1;
  }

  _1_PROVE = f > 0;
  printf("_1_PROVE:%d\n", _1_PROVE);
  printf("f:%d\n", f);
  printf("i:%d\n", i);
  printf("--------\n");
  return 0;
}
