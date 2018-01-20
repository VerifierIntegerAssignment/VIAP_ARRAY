import sys
import os
currentdirectory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdirectory+"/packages/setuptools/")
currentdirectory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdirectory+"/packages/z3/python/")
from z3 import *
init(currentdirectory+"/packages/z3")
set_param(proof=True)

try:
	_p1=Int('_p1')
	_p2=Int('_p2')
	_n=Int('_n')
	_bool=Int('_bool')
	arraySort = DeclareSort('arraySort')
	_f=Function('_f',IntSort(),IntSort())
	_ToReal=Function('_ToReal',RealSort(),IntSort())
	_ToInt=Function('_ToInt',IntSort(),RealSort())
	d1array16=Function('d1array16',arraySort,IntSort(),IntSort(),IntSort())
	_n2=Int('_n2')
	volArray1=Const('volArray1',arraySort)
	d1array14=Function('d1array14',arraySort,IntSort(),IntSort(),IntSort())
	CCCELVOL2_var1=Int('CCCELVOL2_var1')
	CCCELVOL3_var=Int('CCCELVOL3_var')
	_x1=Const('_x1',arraySort)
	_x2=Int('_x2')
	__VERIFIER_nondet_int2=Int('__VERIFIER_nondet_int2')
	i1=Int('i1')
	volArray=Const('volArray',arraySort)
	main=Int('main')
	CCCELVOL2_var=Int('CCCELVOL2_var')
	_N1=Const('_N1',IntSort())
	_N2=Const('_N2',IntSort())
	d1array=Function('d1array',arraySort,IntSort(),IntSort())
	MINVAL1=Int('MINVAL1')
	CCCELVOL1_var1=Int('CCCELVOL1_var1')
	CELLCOUNT1=Int('CELLCOUNT1')
	CCCELVOL4_var1=Int('CCCELVOL4_var1')
	d1array1=Function('d1array1',arraySort,IntSort(),IntSort())
	MINVAL=Int('MINVAL')
	i=Int('i')
	_n1=Int('_n1')
	CCCELVOL4_var=Int('CCCELVOL4_var')
	CCCELVOL3_var1=Int('CCCELVOL3_var1')
	CCCELVOL1_var=Int('CCCELVOL1_var')
	_k1=Int('_k1')
	_k2=Int('_k2')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(volArray1 == volArray)
	_s.add(MINVAL1 == MINVAL)
	_s.add(CCCELVOL2_var1 == If(((__VERIFIER_nondet_int2)>(1)),3,CCCELVOL2_var))
	_s.add(CELLCOUNT1 == __VERIFIER_nondet_int2)
	_s.add(ForAll([_x2],Implies(And(_x2>=0,_x2<CELLCOUNT1),d1array1(volArray,_x2) == If(((__VERIFIER_nondet_int2)>(1)),If(((((__VERIFIER_nondet_int2)%(4)))==(0)),d1array16(volArray,_x2,_N2),d1array(volArray,_x2)),d1array(volArray,_x2)))))
	_s.add(CCCELVOL4_var1 == If(((__VERIFIER_nondet_int2)>(1)),5,CCCELVOL4_var))
	_s.add(main == If(Or(((((__VERIFIER_nondet_int2)%(4)))==(0)),((__VERIFIER_nondet_int2)<=(1))),1,If(((__VERIFIER_nondet_int2)>(1)),If(((((__VERIFIER_nondet_int2)%(4)))!=(0)),1,0),0)))
	_s.add(i1 == If(((__VERIFIER_nondet_int2)>(1)),If(((((__VERIFIER_nondet_int2)%(4)))==(0)),_N2,i),i))
	_s.add(CCCELVOL1_var1 == If(((__VERIFIER_nondet_int2)>(1)),1,CCCELVOL1_var))
	_s.add(CCCELVOL3_var1 == If(((__VERIFIER_nondet_int2)>(1)),7,CCCELVOL3_var))
	_s.add(ForAll([_n1],Implies(And(_n1<_N1,_n1>=0),d1array14(volArray,((((((_n1)+(1)))*(4)))-(1)),((_n1)+(1))) == 1)))
	_s.add(ForAll([_n1],Implies(And(_n1<_N1,_n1>=0),d1array14(volArray,((((((_n1)+(1)))*(4)))-(4)),((_n1)+(1))) == 5)))
	_s.add(ForAll([_n1],Implies(And(_n1<_N1,_n1>=0),d1array14(volArray,((((((_n1)+(1)))*(4)))-(2)),((_n1)+(1))) == 3)))
	_s.add(ForAll([_n1],Implies(And(_n1<_N1,_n1>=0),d1array14(volArray,((((((_n1)+(1)))*(4)))-(3)),((_n1)+(1))) == 7)))
	_s.add(ForAll([_x2],Implies(And(_x2>=0,_x2<CELLCOUNT1),d1array14(volArray,_x2,0) == d1array(volArray,_x2))))
	_s.add(((((_N1)+(1)))>(((__VERIFIER_nondet_int2)/(4)))))
	_s.add(ForAll([_n1],Implies(And(((_n1)<(_N1)),_n1>=0),((((_f(_n1))+(1)))<=(((__VERIFIER_nondet_int2)/(4)))))))
	_s.add(Or(_N1==0,_N1 <= __VERIFIER_nondet_int2/4))
	_s.add(ForAll([_x2,_n2],Implies(And(_n2<_N2,And(And(_x2>=0,_n2>=0),_x2<CELLCOUNT1)),d1array16(volArray,_x2,((_n2)+(1))) == d1array16(volArray,_x2,_n2))))
	_s.add(ForAll([_x2],Implies(And(_x2>=0,_x2<CELLCOUNT1),d1array16(volArray,_x2,0) == d1array14(volArray,_x2,_N1))))
	_s.add(((_N2)>=(((__VERIFIER_nondet_int2)-(0)))))
	_s.add(ForAll([_n2],Implies(And(((_n2)<(_N2)),_n2>=0),((((_f(_n2))+(0)))<(__VERIFIER_nondet_int2)))))
	_s.add(Or(_N2==0,(((_N2-1))<(__VERIFIER_nondet_int2))))
	_s.add(ForAll([_x2,_n1],Implies(And(_n1<_N1,And(And(_x2>=0,_n1>=0),_x2<CELLCOUNT1)),d1array14(volArray,_x2,_N1) == If(((1)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(1)))),1,If(((3)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(2)))),3,If(((7)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),7,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL))),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),0,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL))))),If(((_x2)==(((((((_n1)+(1)))*(4)))-(2)))),0,If(((7)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),7,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL))),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),0,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL))))))),If(((_x2)==(((((((_n1)+(1)))*(4)))-(1)))),0,If(((3)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(2)))),3,If(((7)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),7,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL))),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),0,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL))))),If(((_x2)==(((((((_n1)+(1)))*(4)))-(2)))),0,If(((7)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),7,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL))),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),0,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL)))))))))))
	_s.add(ForAll([_x2,_n1],Implies(And(_n1<_N1,And(And(_x2>=0,_n1>=0),_x2<CELLCOUNT1)),d1array16(volArray,_x2,_N2) == If(((1)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(1)))),1,If(((3)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(2)))),3,If(((7)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),7,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL))),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),0,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL))))),If(((_x2)==(((((((_n1)+(1)))*(4)))-(2)))),0,If(((7)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),7,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL))),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),0,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL))))))),If(((_x2)==(((((((_n1)+(1)))*(4)))-(1)))),0,If(((3)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(2)))),3,If(((7)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),7,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL))),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),0,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL))))),If(((_x2)==(((((((_n1)+(1)))*(4)))-(2)))),0,If(((7)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),7,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL))),If(((_x2)==(((((((_n1)+(1)))*(4)))-(3)))),0,If(((5)>=(MINVAL)),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),5,MINVAL),If(((_x2)==(((((((_n1)+(1)))*(4)))-(4)))),0,MINVAL)))))))))))
	_s.add(volArray1 == volArray)
	_s.add(MINVAL1 == MINVAL)
	_s.add((_N2==(__VERIFIER_nondet_int2-0)))
	_s.add(_k1>=0)
	_s.add(_k2>=0)
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(((__VERIFIER_nondet_int2%4)==0))
	_s.add((__VERIFIER_nondet_int2>1))
	_s.add(Not(ForAll([_n2],Implies(And(_n2<_N2,_n2>=0),Implies(((((__VERIFIER_nondet_int2)%(4)))==(0)),Or(((d1array16(volArray,_n2,_N2))>=(MINVAL)),((d1array16(volArray,_n2,_N2))==(0))))))))

except Exception as e:
	print "Error(Z3Query)"
	file = open('j2llogs.logs', 'a')

	file.write(str(e))

	file.close()

	sys.exit(1)

try:
	result=_s.check()
	if sat==result:
		print "Counter Example"
		print _s.model()
	elif unsat==result:
		result
		try:
			if os.path.isfile('j2llogs.logs'):
				file = open('j2llogs.logs', 'a')
				file.write("\n**************\nProof Details\n**************\n"+str(_s.proof().children())+"\n")
				file.close()
			else:
				file = open('j2llogs.logs', 'w')
				file.write("\n**************\nProof Details\n**************\n"+str(_s.proof().children())+"\n")
				file.close()
		except Exception as e:
			file = open('j2llogs.logs', 'a')
			file.write("\n**************\nProof Details\n**************\n"+"Error"+"\n")
			file.close()
		print "Successfully Proved"
	else:
		print "Failed To Prove"
except Exception as e:
	print "Error(Z3Query)"
	file = open('j2llogs.logs', 'a')

	file.write(str(e))

	file.close()
