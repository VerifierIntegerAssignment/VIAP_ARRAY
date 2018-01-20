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

	int i,j,k,l;
	int n;
	int A [n][n][n][n];
	int B [n][n][n][n];
        int C [n][n][n][n];

	i=0;
	j=0;
	k=0;
        l=0;
	while(i < n){
		j=0;
		k=0;
                l=0;
		while(j < n){
			k=0;
                        l=0;
			while(k < n){
                                l=0;
                                    while(l < n){
                                            C[i][j][k][l]=A[i][j][k][l]-B[i][j][k][l];
                                            l=l+1;
                                        }
					k=k+1;
			}
			j=j+1;
		}
		i=i+1;
    }


	i=0;
	j=0;
	k=0;
        l=0;
	while(i < n){
		j=0;
		k=0;
                l=0;
		while(j < n){
			k=0;
                        l=0;
			while(k < n){
                                l=0;
                                    while(l < n){
                                            __VERIFIER_assert(C[i][j][k][l]==A[i][j][k][l]-B[i][j][k][l]);
                                            l=l+1;
                                        }
					k=k+1;
			}
			j=j+1;
		}
		i=i+1;
    }




}