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
return value;
}
char __VERIFIER_nondet_char()
{
char value;
_count_char++;
srand(_count_int+(char)time(NULL));
srand(rand());
value=rand()%1000;
return value;
}
int __VERIFIER_nondet_int()
{
int value;
 _count_int++;
srand(_count_int+(int)time(NULL));
 srand(rand());
value=rand()%1000;
value=2;
return value;
}

unsigned int __VERIFIER_nondet_uint()
{
unsigned int value;
 _count++;
srand(_count+(unsigned int)time(NULL));
 srand(rand());
value=rand()%1000;
return value;
}

double __VERIFIER_nondet_double()
{
double value;
 _count++;
srand(_count_double+(double)time(NULL));
 srand(rand());
 value=rand()%1000;
return value;
}

float __VERIFIER_nondet_float()
{
float value;
 _count++;
srand(_count_float+(float)time(NULL));
 srand(rand());
 
 value=rand()%1000;
return value;
}
int main(){
  int _con_flag1 = 0;
  int _con_flag2 = 0;
  int _con_flag3 = 0;
  int _1_PROVE[1000000];
  int a[100000];
  int max = 0;
  int i = 0;
  _con_flag1 = i < 100000;
  printf("WhileCondition:i < 100000:7:%d\n", _con_flag1);
  while (_con_flag1)
  {
    _con_flag2 = a[i] > max;
    printf("IfCondition1:a[i] > max:8:%d\n", _con_flag2);
    if (_con_flag2)
    {
      printf("IfCondition2:a[i] > max:8:%d\n", _con_flag2);
      max = a[i];
      printf("assumption:max==%d;a[i]==%d;\n", max, a[i]);
      printf("Assignment:max = a[i]:max = a[i]:9\n");
    }

    i = i + 1;
    printf("assumption:i==%d;max==%d;a[i]==%d;\n", i, max, a[i]);
    printf("Assignment:i = i + 1:i = i + 1:11\n");
    _con_flag1 = i < 100000;
    printf("WhileCondition:i < 100000:7:%d\n", _con_flag1);
  }

  int x;
  x = 0;
  printf("assumption:i==%d;max==%d;a[i]==%d;x==%d;\n", i, max, a[i], x);
  printf("Assignment:x = 0:int max = 0:5\n");
  _con_flag3 = x < 100000;
  printf("WhileCondition:x < 100000:14:%d\n", _con_flag3);
  while (_con_flag3)
  {
    _1_PROVE[x] = a[x] > max;
    printf("assumption:i==%d;max==%d;a[i]==%d;a[x]==%d;x==%d;\n", i, max, a[i], a[x], x);
    printf("__VERIFIER_assert(a[x] > max):%d\n", _1_PROVE[x]);
    x = x + 1;
    printf("assumption:i==%d;max==%d;a[i]==%d;a[x]==%d;x==%d;\n", i, max, a[i], a[x], x);
    printf("Assignment:x = x + 1:x = x + 1:14\n");
    _con_flag3 = x < 100000;
    printf("WhileCondition:x < 100000:14:%d\n", _con_flag3);
  }

  printf("assumption:i==%d;max==%d;a[i]==%d;a[x]==%d;x==%d;\n", i, max, a[i], a[x], x);
  printf("Return:0:main:%d:17\n", 0);
  return 0;
}
