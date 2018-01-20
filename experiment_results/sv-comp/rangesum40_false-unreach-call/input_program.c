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
int rangesum(int x[40]);
void init_nondet(int x[40]);
void init_nondet(int x[40]){
  int i;
  i = 0;
  while (i < 40)
  {
    x[i] = __VERIFIER_nondet_int();
    i = i + 1;
  }

}
int main(){
  int _1_FAILED = 0;
  int x[40];
  init_nondet(x);
  int temp;
  int ret;
  int ret2_var;
  int ret5_var;
  ret = rangesum(x);
  temp = x[0];
  x[0] = x[1];
  x[1] = temp;
  ret2_var = rangesum(x);
  temp = x[0];
  int i = 0;
  while (i < (40 - 1))
  {
    x[i] = x[i + 1];
    i = i + 1;
  }

  x[40 - 1] = temp;
  ret5_var = rangesum(x);
  if ((ret != ret2_var) || (ret != ret5_var))
  {
    _1_FAILED = 1;
    printf("_1_FAILED:%d\n", _1_FAILED);
    printf("temp:%d\n", temp);
    printf("ret5_var:%d\n", ret5_var);
    printf("ret:%d\n", ret);
    printf("i:%d\n", i);
    printf("ret2_var:%d\n", ret2_var);
    printf("--------\n");
  }

  return 1;
}
int rangesum(int x[40]){
  int i;
  long long ret;
  ret = 0;
  int cnt = 0;
  i = 0;
  while (i < 40)
  {
    if (i > (40 / 2))
    {
      ret = ret + x[i];
      cnt = cnt + 1;
    }

    i = i + 1;
  }

  if (cnt != 0)
  {
    return ret / cnt;
  }
  else
  {
    return 0;
  }

}
