extern void __VERIFIER_error() __attribute__ ((__noreturn__));
void __VERIFIER_assert(int cond) { if(!(cond)) { ERROR: __VERIFIER_error(); } }
int main( ) {
  int A[100000];
  int a = 0;
  int b = 0;
  int c = 0;
  int B[100000];
  int C[100000];
  while( a < 100000 ) {
    if( A[ a ] >= 0 ) {
      B[ b ] = A[ a ];
      b = b + 1;
    }
    else {
      C[ c ] = A[ a ];
      c = c + 1;
    }
    a = a + 1;
  }
  int x;
  for ( x = 0 ; x < b ; x++ ) {
    __VERIFIER_assert( B[ x ] >= 0 );
  }
  for ( x = 0 ; x < c ; x++ ) {
    __VERIFIER_assert( C[ x ] < 0 );
  }
  return 0;
}
