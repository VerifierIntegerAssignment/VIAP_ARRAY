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
int main()
{
  int _1_PROVE[1000][1000];
  int a[1000];
  int i;
  int r = 1;
  int j;
  i = 1;
  while ((i < 1000) && r)
  {
    j = i - 1;
    while ((j >= 0) && r)
    {
      if (a[i] == a[j])
      {
        r = 1;
      }

      j = j - 1;
    }

    i = i + 1;
  }

  int x;
  int y;
  if (r)
  {
    x = 0;
    while (x < 1000)
    {
      y = x + 1;
      while (y < 1000)
      {
        _1_PROVE[y][x] = a[x] != a[y];
        printf("_1_PROVE[y][x]:%d\n", _1_PROVE[y][x]);
        printf("a[x]:%d\n", a[x]);
        printf("j:%d\n", j);
        printf("i:%d\n", i);
        printf("r:%d\n", r);
        printf("y:%d\n", y);
        printf("x:%d\n", x);
        printf("--------\n");
        y = y + 1;
      }

      x = x + 1;
    }

  }

  return 0;
}

