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

	int i,j,k,l,m,t;
	int Size;
	int A [Size][Size][Size][Size][Size];
        int C;
	i=0;
	j=0;
	k=0;
        l=0;
        m=0;
        
        
       
       
   
	while(i < Size){
	j=0;
	k=0;
        l=0;
        m=0;
        
       
        
       
      
		while(j < Size){

	k=0;
        l=0;
        m=0;
        
      
        
        
       
			while(k < Size){

        l=0;
        m=0;
        
        
       
        
       
                                while(l < Size){

        m=0;
        
        
       
        
        
					while(m < Size){



 




										A[i][j][k][l][m]=C;



					

						m=m+1;
					}

					
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
        m=0;
        
       
        
       
       
	while(i < Size){
	j=0;
	k=0;
        l=0;
        m=0;
       
        
       
       
       
		while(j < Size){

	k=0;
        l=0;
        m=0;
        
       
      
      
        
			while(k < Size){

        l=0;
        m=0;
        
       
       
        
        
                                while(l < Size){

        m=0;
        
        
       
       
        
					while(m < Size){







										__VERIFIER_assert(A[i][j][k][l][m]==C);


					

						m=m+1;
					}

					
					l=l+1;
                                    }
                            k=k+1;
			}
			j=j+1;
		}
		i=i+1;
    }


}
