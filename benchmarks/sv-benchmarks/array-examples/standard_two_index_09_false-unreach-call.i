extern void __VERIFIER_error() __attribute__ ((__noreturn__));
void __VERIFIER_assert(int cond) { if(!(cond)) { ERROR: __VERIFIER_error(); } }
int main( )
{
  int a[100000];
  int b[100000];
  int i;
  int j;
  i = 1;
  j = 0;
  while( i < 100000 )
  {
 a[j] = b[i];
        i = i+9;
        j = j+1;
  }
  i = 1;
  j = 0;
  while( i < 100000 )
  {
 __VERIFIER_assert( a[j] != b[9*j+1] );
        i = i+9;
        j = j+1;
  }
  return 0;
}
