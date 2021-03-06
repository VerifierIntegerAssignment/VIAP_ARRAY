# VIAP
<img src="VIAP_logo.jpg" width=400 alt="SMACK Logo" align="right">

Verifier Integer Assignment Program(VIAP) translates a program to first-order logic with
quantifiers on natural numbers following the method proposed recently by [Professor Fangzhen Lin](http://www.cs.ust.hk/~flin/). Once translated to a first-order theory, properties of the program can then be proved using induction (because of the quantifiers on natural numbers) and other methods.

### Awards & Achievements
1. [VIAP was second in the ReachSafety-Arrays sub-category of ReachSafety category](https://sv-comp.sosy-lab.org/2018/results/results-verified/)

Many more to come..

## Publications

1. [A Formalization of Programs in First-Order Logic with a Discrete Linear Order](http://www.sciencedirect.com/science/article/pii/S000437021630011X?via%3Dihub),Fangzhen Lin,Artificial Intelligence(2016)

1. [VIAP - automated system for verifying integer assignment programs with loops](https://github.com/VerifierIntegerAssignment/sv-comp/blob/master/viap-automated-system.pdf),Pritom Rajkhowa, Fangzhen Lin, 19th International Symposium on Symbolic and Numeric Algorithms for Scientific Computing,SYNASC 2017, Timisoara, Romania, September 21-24, 2017

1. [VIAP-Automated System for Verifying Integer Assignment Programs with Loops(Competition Contribution)](https://github.com/VerifierIntegerAssignment/sv-comp-1/blob/master/viap-automated-system.pdf), Pritom Rajkhowa, Fangzhen Lin, 7th International Competition on Software Verification (2018)(not part of TACAS proceeding)


# See below for system requirements, installation, usage, and everything else.

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

#### Output contains the string:
```
-Result TRUE when the program is safe
```
```
-Result FALSE when a counterexample is found and a file named errorWitness.graphml that contains the witness of error-path is generated in the VIAP root folder
```
```
-Result UNKNOWN otherwise.
```






### Using The VIAP Verifier

Next, we illustrate how to verify the following simple C program using the VIAP
verifier:

```C
// benchmarks/multidimensional/transpose.c
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

```python
Program Body
{
  int _1_PROVE[100000][100000];
  int i;
  int k;
  int j;
  int n;
  int m;
  int A[n][m];
  int C[m][n];
  i = 0;
  j = 0;
  while (i < n)
  {
    j = 0;
    while (j < m)
    {
      C[j][i] = A[i][j];
      j = j + 1;
    }

    i = i + 1;
  }

  i = 0;
  while (i < m)
  {
    j = 0;
    while (j < n)
    {
      _1_PROVE[i][j] = C[i][j] == A[i][j];
      j = j + 1;
    }

    i = i + 1;
  }

}

Function Name:
main
Return Type:
int
Input Variables:
{}
Local Variables:
{ A:array C:array j:int i:int k:int _1_PROVE:array m:int n:int}


Output in normal notation:
1. Frame axioms:
A1 = A
C1 = C
m1 = m
k1 = k
n1 = n

2. Output equations:
i1 = (_N4+0)
j1 = j10(_N4)
d2array1(_x1,_x2,_x3) = d2array10(_x1,_x2,_x3,_N4)

3. Other axioms:
d2array2(_x1,_x2,_x3,(_n1+1),_n2) = ite(((_x1=C) and (_x2=(_n1+0)) and (_x3=(_n2+0))),d2array2(A,(_n2+0),(_n1+0),_n1,_n2),d2array2(_x1,_x2,_x3,_n1,_n2))
d2array2(_x1,_x2,_x3,0,_n2) = d2array5(_x1,_x2,_x3,_n2)
(_N1(_n2)>=(-(0)+m))
(_n1<_N1(_n2)) -> ((_n1+0)<m)
j5((_n2+1)) = (_N1(_n2)+0)
d2array5(_x1,_x2,_x3,(_n2+1)) = d2array2(_x1,_x2,_x3,_N1(_n2),_n2)
j5(0) = 0
d2array5(_x1,_x2,_x3,0) = d2array(_x1,_x2,_x3)
(_N2>=(-(0)+n))
(_n2<_N2) -> ((_n2+0)<n)
d2array7(_x1,_x2,_x3,(_n3+1),_n4) = d2array7(_x1,_x2,_x3,_n3,_n4)
d2array7(_x1,_x2,_x3,0,_n4) = d2array10(_x1,_x2,_x3,_n4)
(_N3(_n4)>=(-(0)+n))
(_n3<_N3(_n4)) -> ((_n3+0)<n)
j10((_n4+1)) = (_N3(_n4)+0)
d2array10(_x1,_x2,_x3,(_n4+1)) = d2array7(_x1,_x2,_x3,_N3(_n4),_n4)
j10(0) = j5(_N2)
d2array10(_x1,_x2,_x3,0) = d2array5(_x1,_x2,_x3,_N2)
(_N4>=(-(0)+m))
(_n4<_N4) -> ((_n4+0)<m)

4. Assumption :

5. Assertion :
(d2array10(C,(_n4+0),(_n3+0),_N4)==d2array10(A,(_n4+0),(_n3+0),_N4))

Axiomes Added

d2array7(A,_x2,_x3,_N3(_n4),_n4) = d2array(A,_x2,_x3)
d2array2(A,_x2,_x3,_N1(_n2),_n2) = d2array(A,_x2,_x3)
d2array7(C,(_n1+0),(_n2+0),_N3(_n4),_n4) = d2array7(A,(_n2+0),(_n1+0),_N3(_n4),_n4)
d2array10(C,(_n1+0),(_n2+0),_N4) = d2array10(C,(_n2+0),(_n1+0),(_n4+1))
d2array7(A,_x2,_x3,_N3(_n4),_n4) = d2array7(A,_x2,_x3,_N3(_n4),_n4)
d2array2(C,(_n1+0),(_n2+0),_N1(_n2),_n2) = d2array(A,(_n2+0),(_n1+0))
d2array10(A,_x2,_x3,_N4) = d2array10(A,_x2,_x3,(_n4+1))
d2array10(A,_x2,_x3,_N4) = d2array(A,_x2,_x3)
d2array5(C,(_n1+0),(_n2+0),_N2) = d2array5(C,(_n2+0),(_n1+0),(_n2+1))
d2array2(A,_x2,_x3,_N1(_n2),_n2) = d2array2(A,_x2,_x3,_N1(_n2),_n2)
d2array2(C,(_n1+0),(_n2+0),_N1(_n2),_n2) = d2array2(A,(_n2+0),(_n1+0),_N1(_n2),_n2)
d2array5(A,_x2,_x3,_N2) = d2array5(A,_x2,_x3,(_n2+1))
d2array10(C,(_n1+0),(_n2+0),_N4) = d2array(A,(_n2+0),(_n1+0))
d2array7(C,(_n1+0),(_n2+0),_N3(_n4),_n4) = d2array(A,(_n2+0),(_n1+0))
d2array5(C,(_n1+0),(_n2+0),_N2) = d2array(A,(_n2+0),(_n1+0))
d2array5(A,_x2,_x3,_N2) = d2array(A,_x2,_x3)


VIAP_STANDARD_OUTPUT_True
```



