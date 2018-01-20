extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();

int main()
{

	int i,j;
	int m,n,p;
	int A [m][n];
	int B [m][n];

	i=0;
	j=0;
	while(i < m){
		j=0;
		while(j < n){
			
                            A[i][j]=B[i][j];
			
			j=j+1;
		}
		i=i+1;
    }




	i=0;
	j=0;
	while(i < m){
		j=0;
		while(j < n){
			
                            __VERIFIER_assert(A[i][j]==B[i][j]);
		
			j=j+1;
		}
		i=i+1;
    }

}