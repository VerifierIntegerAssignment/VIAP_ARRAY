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
	largest2_var9=Function('largest2_var9',IntSort(),IntSort())
	d1array13=Function('d1array13',arraySort,IntSort(),IntSort(),IntSort())
	d1array11=Function('d1array11',arraySort,IntSort(),IntSort(),IntSort())
	largest2_var1=Int('largest2_var1')
	temp1=Int('temp1')
	array=Const('array',arraySort)
	_x1=Const('_x1',arraySort)
	_x2=Int('_x2')
	array1=Const('array1',arraySort)
	_N2=Const('_N2',IntSort())
	main=Int('main')
	_N1=Const('_N1',IntSort())
	i1=Int('i1')
	_N3=Const('_N3',IntSort())
	d1array=Function('d1array',arraySort,IntSort(),IntSort())
	x1=Int('x1')
	d1array1=Function('d1array1',arraySort,IntSort(),IntSort())
	largest1_var9=Function('largest1_var9',IntSort(),IntSort())
	temp=Int('temp')
	_n2=Int('_n2')
	largest1_var1=Int('largest1_var1')
	_n1=Int('_n1')
	_n3=Int('_n3')
	_k2=Int('_k2')
	_k3=Int('_k3')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(array1 == array)
	_s.add(temp1 == If(((d1array(array,0))<(d1array(array,1))),d1array(array,0),temp))
	_s.add(i1 == _N1 + 2)
	_s.add(ForAll([_x2],Implies(And(_x2>=0,_x2<100000),d1array1(array,_x2) == d1array13(array,_x2,_N3))))
	_s.add(largest1_var1 == largest1_var9(_N1))
	_s.add(main == 0)
	_s.add(x1 == _N3)
	_s.add(largest2_var1 == largest2_var9(_N1))
	_s.add(ForAll([_n1],Implies(And(_n1<_N1,_n1>=0),largest1_var9(((_n1)+(1))) == If(((d1array(array,((_n1)+(2))))>=(largest1_var9(_n1))),d1array(array,((_n1)+(2))),largest1_var9(_n1)))))
	_s.add(ForAll([_n1],Implies(And(_n1<_N1,_n1>=0),largest2_var9(((_n1)+(1))) == If(((d1array(array,((_n1)+(2))))>=(largest1_var9(_n1))),largest1_var9(_n1),If(((d1array(array,((_n1)+(2))))>(largest2_var9(_n1))),d1array(array,((_n1)+(2))),largest2_var9(_n1))))))
	_s.add(largest1_var9(0) == If(((d1array(array,0))<(d1array(array,1))),d1array(array,1),d1array(array,0)))
	_s.add(largest2_var9(0) == If(((d1array(array,0))<(d1array(array,1))),d1array(array,0),d1array(array,1)))
	_s.add(_N1 >= 99998)
	_s.add(ForAll([_n1],Implies(And(((_n1)<(_N1)),_n1>=0),((((_f(_n1))+(2)))<(100000)))))
	_s.add(Or(_N1==0,_N1 + 1 < 100000))
	_s.add(ForAll([_x2,_n2],Implies(And(_n2<_N2,And(And(_x2>=0,_n2>=0),_x2<100000)),d1array11(array,_x2,((_n2)+(1))) == d1array11(array,_x2,_n2))))
	_s.add(ForAll([_x2],Implies(And(_x2>=0,_x2<100000),d1array11(array,_x2,0) == d1array(array,_x2))))
	_s.add(_N2 >= 100000)
	_s.add(ForAll([_n2],Implies(And(((_n2)<(_N2)),_n2>=0),((((_f(_n2))+(0)))<(100000)))))
	_s.add(Or(_N2==0,_N2 - 1 < 100000))
	_s.add(ForAll([_x2,_n3],Implies(And(_n3<_N3,And(And(_x2>=0,_n3>=0),_x2<100000)),d1array13(array,_x2,((_n3)+(1))) == d1array13(array,_x2,_n3))))
	_s.add(ForAll([_x2],Implies(And(_x2>=0,_x2<100000),d1array13(array,_x2,0) == d1array11(array,_x2,_N2))))
	_s.add(_N3 >= 100000)
	_s.add(ForAll([_n3],Implies(And(((_n3)<(_N3)),_n3>=0),((((_f(_n3))+(0)))<(100000)))))
	_s.add(Or(_N3==0,_N3 - 1 < 100000))
	_s.add(ForAll([_x2],Implies(And(_x2>=0,_x2<100000),d1array11(array,_x2,_N2) == d1array11(array,_x2,_N2))))
	_s.add(ForAll([_x2],Implies(And(_x2>=0,_x2<100000),d1array13(array,_x2,_N3) == d1array13(array,_x2,_N3))))
	_s.add(array1 == array)
	_s.add((_N1==(-(2)+100000)))
	_s.add((_N2==(-(0)+100000)))
	_s.add((_N3==(-(0)+100000)))
	_s.add(_k2>=0)
	_s.add(_k3>=0)
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(_N3>=0)
	_s.add(Not(ForAll([_n3],Implies(And(_n3<_N3,_n3>=0),Or(((d1array13(array,_n3,_N3))<=(largest2_var9(_N1))),((d1array13(array,_n3,_N3))==(largest1_var9(_N1))))))))

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
