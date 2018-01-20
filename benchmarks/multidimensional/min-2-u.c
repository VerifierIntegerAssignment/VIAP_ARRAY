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
	int m,n;
	int A [n][n];
	int min;

	i=0;
	j=0;
        min=A [0][0];
	while(i < n){
		j=0;
		while(j < n){
			if(A[i][j]<min){
                            min=A[i][j];
                        }
			j=j+1;
		}
		i=i+1;
    }




	i=0;
	j=0;
	while(i < n){
		j=0;
		while(j < n){
                    
			__VERIFIER_assert(A[i][j]>=min);
			j=j+1;
		}
		i=i+1;
    }

}