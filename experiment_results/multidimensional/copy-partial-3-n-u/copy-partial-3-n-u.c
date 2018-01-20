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

	int i,j,k;
	int m,n,p;
	int q,s,t;
	int A [m][n][p];
        int B [m][n][p];

	i=0;
	j=0;
	k=0;
	__VERIFIER_assume(q<m);
	__VERIFIER_assume(s<n);
	__VERIFIER_assume(t<p);

	while(i < q){
		j=0;
		k=0;
		while(j < s){
			k=0;
			while(k < t){
					A[i][j][k]=B[i][j][k];
					k=k+1;
			}
			j=j+1;
		}
		i=i+1;
    }




	i=0;
	j=0;
	k=0;
	while(i < q){
		j=0;
		k=0;
		while(j < s){
			k=0;
			while(k < t){
					__VERIFIER_assert(A[i][j][k]==B[i][j][k]);
					k=k+1;
			}
			j=j+1;
		}
		i=i+1;
    }

}