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
	a=Const('a',arraySort)
	_n2=Int('_n2')
	max1=Int('max1')
	i1=Int('i1')
	max3=Function('max3',IntSort(),IntSort())
	x1=Int('x1')
	_N1=Const('_N1',IntSort())
	d1array1=Function('d1array1',arraySort,IntSort(),IntSort())
	a1=Const('a1',arraySort)
	_N2=Const('_N2',IntSort())
	d1array=Function('d1array',arraySort,IntSort(),IntSort())
	_n1=Int('_n1')
	d1array5=Function('d1array5',arraySort,IntSort(),IntSort(),IntSort())
	main=Int('main')
	_x1=Const('_x1',arraySort)
	_x2=Int('_x2')
	_L2=Int('_L2')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(a1 == a)
	_s.add(i1 == _N1)
	_s.add(max1 == max3(_N1))
	_s.add(ForAll([_x2,_x1],Implies(_x2>=0,d1array1(_x1,_x2) == d1array5(_x1,_x2,_N2))))
	_s.add(main == 0)
	_s.add(x1 == _N2)
	_s.add(ForAll([_n1],Implies(_n1>=0,max3(_n1 + 1) == If(((d1array(a,_n1))>(max3(_n1))),d1array(a,_n1),max3(_n1)))))
	_s.add(max3(0) == 0)
	_s.add(_N1 >= 100000)
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),_f(_n1) < 100000)))
	_s.add(Or(_N1==0,_N1 - 1 < 100000))
	_s.add(ForAll([_x2,_n2],Implies(And(_x2>=0,_n2>=0),d1array5(a,_x2,_n2 + 1) == d1array5(a,_x2,_n2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array5(a,_x2,0) == d1array(a,_x2))))
	_s.add(_N2 >= 100000)
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),_f(_n2) < 100000)))
	_s.add(Or(_N2==0,_N2 - 1 < 100000))
	_s.add(a1 == a)
	_s.add(i1 == _N1)
	_s.add(max1 == max3(_N1))
	_s.add(ForAll([_x2,_x1],Implies(_x2>=0,d1array1(_x1,_x2) == d1array5(_x1,_x2,_N2))))
	_s.add(main == 0)
	_s.add(x1 == _N2)
	_s.add(Not(Implies(ForAll([_n2],Implies(And(And(_n2>=0,_n2<_L2),_L2>0),((d1array5(a,_n2,_n2))<=(max3(_L2))))),ForAll([_n2],Implies(And(And(And(And(_n2>=0,_n2<_L2),_L2>0),_n2<_L2+1),_L2>0),((d1array5(a,_n2,_n2))<=(max3(_L2 + 1))))))))

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
