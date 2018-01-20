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
	j6=Function('j6',IntSort(),IntSort())
	j1=Int('j1')
	_x1=Const('_x1',arraySort)
	_x2=Int('_x2')
	_x3=Int('_x3')
	d2array1=Function('d2array1',arraySort,IntSort(),IntSort(),IntSort())
	d2array8=Function('d2array8',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	A1=Const('A1',arraySort)
	_N2=Const('_N2',IntSort())
	m6=Function('m6',IntSort(),IntSort())
	m1=Int('m1')
	m3=Function('m3',IntSort(),IntSort(),IntSort())
	A=Const('A',arraySort)
	d2array11=Function('d2array11',arraySort,IntSort(),IntSort(),IntSort(),IntSort())
	i1=Int('i1')
	_N3=Function('_N3',IntSort(),IntSort())
	_N1=Function('_N1',IntSort(),IntSort())
	_N4=Const('_N4',IntSort())
	d2array=Function('d2array',arraySort,IntSort(),IntSort(),IntSort())
	j11=Function('j11',IntSort(),IntSort())
	p1=Int('p1')
	_n2=Int('_n2')
	_n3=Int('_n3')
	_n1=Int('_n1')
	_n4=Int('_n4')
	n=Int('n')
	p=Int('p')
	n1=Int('n1')
	main=Int('main')
	_L4=Int('_L4')
	_L3=Int('_L3')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(A1 == A)
	_s.add(p1 == p)
	_s.add(n1 == n)
	_s.add(i1 == _N4)
	_s.add(j1 == j11(_N4))
	_s.add(m1 == m6(_N2))
	_s.add(ForAll([_x3,_x2,_x1],Implies(And(_x3>=0,_x2>=0),d2array1(_x1,_x2,_x3) == d2array11(_x1,_x2,_x3,_N4))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),m3(_n1 + 1, _n2) == If(((d2array(A,_n2,_n1))>(m3(_n1, _n2))),d2array(A,_n2,_n1),m3(_n1, _n2)))))
	_s.add(ForAll([_n2],m3(0, _n2) == m6(_n2)))
	_s.add(ForAll([_n2],Implies(_n2>=0,_N1(_n2) >= n)))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1 < _N1(_n2),And(_n1>=0,_n2>=0)),_f(_n1) < n)))
	_s.add(ForAll([_n2],Implies(_n2>=0,Or(_N1(_n2)==0,_N1(_n2) - 1 < n))))
	_s.add(ForAll([_n2],Implies(_n2>=0,j6(_n2 + 1) == _N1(_n2))))
	_s.add(ForAll([_n2],Implies(_n2>=0,m6(_n2 + 1) == m3(_N1(_n2), _n2))))
	_s.add(j6(0) == 0)
	_s.add(m6(0) == d2array(A,0,0))
	_s.add(_N2 >= m6(_N2))
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),_f(_n2) < m6(_f(_n2)))))
	_s.add(Or(_N2==0,_N2 - 1 < m6(_N2 - 1)))
	_s.add(ForAll([_x3,_x2,_n4,_n3],Implies(And(_x3>=0,And(_x2>=0,And(_n4>=0,_n3>=0))),d2array8(A,_x2,_x3,_n3 + 1,_n4) == d2array8(A,_x2,_x3,_n3,_n4))))
	_s.add(ForAll([_x3,_x2,_n4],Implies(And(_x3>=0,And(_x2>=0,_n4>=0)),d2array8(A,_x2,_x3,0,_n4) == d2array11(A,_x2,_x3,_n4))))
	_s.add(ForAll([_n4],Implies(_n4>=0,_N3(_n4) >= n)))
	_s.add(ForAll([_n4,_n3],Implies(And(_n3 < _N3(_n4),And(_n4>=0,_n3>=0)),_f(_n3) < n)))
	_s.add(ForAll([_n4],Implies(_n4>=0,Or(_N3(_n4)==0,_N3(_n4) - 1 < n))))
	_s.add(ForAll([_n4],Implies(_n4>=0,j11(_n4 + 1) == _N3(_n4))))
	_s.add(ForAll([_x3,_x2,_n4],Implies(And(_x3>=0,And(_x2>=0,_n4>=0)),d2array11(A,_x2,_x3,_n4 + 1) == d2array8(A,_x2,_x3,_N3(_n4),_n4))))
	_s.add(j11(0) == 0)
	_s.add(ForAll([_x3,_x2],Implies(And(_x3>=0,_x2>=0),d2array11(A,_x2,_x3,0) == d2array(A,_x2,_x3))))
	_s.add(_N4 >= m6(_N2))
	_s.add(ForAll([_n4],Implies(And(_n4 < _N4,_n4>=0),_f(_n4) < m6(_N2))))
	_s.add(Or(_N4==0,_N4 - 1 < m6(_N2)))
	_s.add(ForAll([_x3,_x2],Implies(And(_x3>=0,_x2>=0),d2array11(A,_x2,_x3,_N4) == d2array(A,_x2,_x3))))
	_s.add(ForAll([_n4,_n3],Implies(And(_n4>=0,_n3>=0),((d2array(A,_n4,_n3))<=(m6(_L4))))))
	_s.add(_L4 >= 0)
	_s.add(A1 == A)
	_s.add(p1 == p)
	_s.add(n1 == n)
	_s.add(i1 == _N4)
	_s.add(j1 == j11(_N4))
	_s.add(m1 == m6(_N2))
	_s.add(ForAll([_x3,_x2,_x1],Implies(And(_x3>=0,_x2>=0),d2array1(_x1,_x2,_x3) == d2array11(_x1,_x2,_x3,_N4))))
	_s.add(Not(Implies(ForAll([_n4,_n3],Implies(And(And(And(_n4>=0,_n3>=0),_n3<_L3),_L3>0),((d2array(A,_n4,_n3))<=(m3(_L3, _L4))))),ForAll([_n4,_n3],Implies(And(And(And(And(And(_n4>=0,_n3>=0),_n3<_L3),_L3>0),_n3<_L3+1),_L3>0),((d2array(A,_n4,_n3))<=(m3(_L3 + 1, _L4))))))))

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
