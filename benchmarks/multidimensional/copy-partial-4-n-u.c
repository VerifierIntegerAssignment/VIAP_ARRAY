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
	int m,n,p,v;
	int q,s,t,u;
	int A [m][n][p][v];
        int B [m][n][p][v];

	i=0;
	j=0;
	k=0;
        l=0;
	__VERIFIER_assume(q<m);
	__VERIFIER_assume(s<n);
	__VERIFIER_assume(t<p);
        __VERIFIER_assume(u<v);

	while(i < q){
		j=0;
		k=0;
                l=0;
		while(j < s){
			k=0;
                        l=0;
			while(k < t){
                            l=0;
                                        while(l < u){
                                                A[i][j][k][l]=B[i][j][k][l];
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
	while(i < q){
		j=0;
		k=0;
                l=0;
		while(j < s){
			k=0;
                        l=0;
			while(k < t){
                            l=0;
                                        while(l < u){
					__VERIFIER_assert(A[i][j][k][l]==B[i][j][k][l]);
                                        l=l+1;
                                        }
					k=k+1;
			}
			j=j+1;
		}
		i=i+1;
    }

}