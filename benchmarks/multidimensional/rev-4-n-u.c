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
	int m,n,p,q;
	int A [m][n][p][q];
	int B [m][n][p][q];

	i=0;
	j=0;
	k=0;
        l=0;
	while(i < m){
		j=0;
		k=0;
                l=0;
		while(j < n){
			k=0;
                        l=0;
			while(k < p){
                            l=0;
                            while(l < q){
					A[i][j][k][l]=B[m-i-1][n-j-1][p-k-1][q-l-1];
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
	while(i < m){
		j=0;
		k=0;
                l=0;
		while(j < n){
			k=0;
                        l=0;
			while(k < p){
                            l=0;
                            while(l < q){
					__VERIFIER_assert(A[i][j][k][l]==B[m-i-1][n-j-1][p-k-1][q-l-1]);
                                        l=l+1;
					
                                }
                                k=k+1;
			}
			j=j+1;
		}
		i=i+1;
    }

}
