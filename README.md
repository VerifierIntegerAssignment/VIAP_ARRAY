# VIAP
<img src="VIAP_logo.png" width=400 alt="SMACK Logo" align="right">

Verifier Integer Assignment Program(VIAP) translates a program to first-order logic with
quantifiers on natural numbers following the method proposed recently by [Professor Fangzhen Lin](http://www.cs.ust.hk/~flin/). Once translated to a first-order theory, properties of the program can then be proved using induction (because of the quantifiers on natural numbers) and other methods.


See below for system requirements, installation, usage, and everything else.

### Support

* If something is not working or missing, open an [issue](https://github.com/VerifierIntegerAssignment/VerifierIntegerAssignment.github.io/issues).

* As a last resort, send mail to 
  [Pritom Rajkhowa](mailto:pritom.rajkhowa@gmail.com), [Fangzhen Lin](mailto:flin@cs.ust.hk), or both.

* To stay informed about updates, you can either watch [VIAP](https://verifierintegerassignment.github.io/)'s Github page.

### System Requirements and Installation

In practice we have run VIAP on standard Ubuntu 16.04 LTS distribution. VIAP is provided as a set of binaries and libraries for
Ubuntu 16.04 LTS distribution. 

#### Download 


##### Clone over HTTPS:

 $ git clone https://github.com/VerifierIntegerAssignment/VIAP_ARRAY.git
 
 #### Running VIAP


VIAP software verifier is run using the `viap_tool.py` tool in the viap directory.
For a given input C program, the tool checks for violations of user-provided
assertions. 

#### Running Command

PATH_TO_VIAP/viap_tool.py [OPTIONS] file


### Using The VIAP Verifier

Next, we illustrate how to verify the following simple C program using the VIAP
verifier:

```C
// benchmarks/multidimensional/
extern void __VERIFIER_error() __attribute__ ((__noreturn__));
void __VERIFIER_assert(int cond) { if(!(cond)) { ERROR: __VERIFIER_error(); } }
int main()
{

	int i;
	int k;
	int j;
	int n;
        int m;
	int A[n][m];
	int C[m][n];

	i=0;
	j=0;

	while(i < n){
		  j=0;
           while(j < m){
                C[j][i] = A[i][j];
		  		j=j+1;
          }
	i=i+1;
    }

	for ( i = 0 ; i < m ; i++ ){
          for ( j = 0 ; j < n ; j++ ){
                __VERIFIER_assert(C[i][j] == A[i][j]);
          }
    }

}

```
Note that this example can also be found in the benchmarks/multidimensional
directory. VIAP defines a number of functions (one for each basic type)
for introducing nondeterministic (i.e., unconstrained) values, such as
`__VERIFIER_nondet_int` used in this example.

#### How to run above Example 

$viap/viap_tool.py --spec=propertyfile/ReachSafety.prp benchmarks/multidimensional/transpose.c

#### Output 




