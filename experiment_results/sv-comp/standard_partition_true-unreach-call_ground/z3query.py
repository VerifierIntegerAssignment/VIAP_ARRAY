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
	d1array10=Function('d1array10',arraySort,IntSort(),IntSort(),IntSort())
	b4=Function('b4',IntSort(),IntSort())
	b1=Int('b1')
	_x1=Const('_x1',arraySort)
	_x2=Int('_x2')
	A1=Const('A1',arraySort)
	d1array=Function('d1array',arraySort,IntSort(),IntSort())
	C1=Const('C1',arraySort)
	main=Int('main')
	A=Const('A',arraySort)
	C=Const('C',arraySort)
	B=Const('B',arraySort)
	_N2=Const('_N2',IntSort())
	_N3=Const('_N3',IntSort())
	_N1=Const('_N1',IntSort())
	a1=Int('a1')
	c8=Function('c8',IntSort(),IntSort())
	d1array8=Function('d1array8',arraySort,IntSort(),IntSort(),IntSort())
	d1array4=Function('d1array4',arraySort,IntSort(),IntSort(),IntSort())
	c1=Int('c1')
	x1=Int('x1')
	d1array1=Function('d1array1',arraySort,IntSort(),IntSort())
	_n2=Int('_n2')
	_n3=Int('_n3')
	_n1=Int('_n1')
	B1=Const('B1',arraySort)
	_k3=Int('_k3')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(A1 == A)
	_s.add(C1 == C)
	_s.add(B1 == B)
	_s.add(a1 == _N2)
	_s.add(c1 == c8(_N2))
	_s.add(b1 == b4(_N1))
	_s.add(ForAll([_x2,_x1],Implies(_x2>=0,d1array1(_x1,_x2) == d1array10(_x1,_x2,_N3))))
	_s.add(main == 0)
	_s.add(x1 == _N3)
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array4(B,b4(_n1),_n1 + 1) == If(((d1array(A,_n1))>=(0)),d1array(A,_n1),d1array4(B,b4(_n1),_n1)))))
	_s.add(ForAll([_n1],Implies(_n1>=0,b4(_n1 + 1) == If(((d1array(A,_n1))>=(0)),b4(_n1) + 1,b4(_n1)))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(B,_x2,0) == d1array(B,_x2))))
	_s.add(b4(0) == 0)
	_s.add(_N1 >= 100000)
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),_f(_n1) < 100000)))
	_s.add(Or(_N1==0,_N1 - 1 < 100000))
	_s.add(ForAll([_n2],Implies(_n2>=0,c8(_n2 + 1) == If(((d1array(A,_n2))<(0)),c8(_n2) + 1,c8(_n2)))))
	_s.add(ForAll([_n2],Implies(_n2>=0,d1array8(C,c8(_n2),_n2 + 1) == If(((d1array(A,_n2))<(0)),d1array(A,_n2),d1array8(C,c8(_n2),_n2)))))
	_s.add(c8(0) == 0)
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array8(C,_x2,0) == d1array(C,_x2))))
	_s.add(_N2 >= 100000)
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),_f(_n2) < 100000)))
	_s.add(Or(_N2==0,_N2 - 1 < 100000))
	_s.add(_N3 >= b4(_N1))
	_s.add(ForAll([_n3],Implies(And(_n3 < _N3,_n3>=0),_f(_n3) < b4(_N1))))
	_s.add(Or(_N3==0,_N3 - 1 < b4(_N1)))
	_s.add(A1 == A)
	_s.add(C1 == C)
	_s.add(B1 == B)
	_s.add(b4(_N1)>=0)
	_s.add((_N1==(-(0)+100000)))
	_s.add((_N2==(-(0)+100000)))
	_s.add((_N3==(b4(_N1)-0)))
	_s.add(_k3>=0)
	_s.add(Not(Implies(((d1array(A,((0)+(0))))>=(0)),((d1array4(B,b4(((0)+(0))),((0)+(1))))>=(0)))))

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
