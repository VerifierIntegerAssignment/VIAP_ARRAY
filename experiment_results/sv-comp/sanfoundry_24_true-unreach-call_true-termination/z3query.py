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
	_1DUMMY1=Int('_1DUMMY1')
	__VERIFIER_nondet_int2=Int('__VERIFIER_nondet_int2')
	num1=Int('num1')
	_n1=Int('_n1')
	i1=Int('i1')
	array1=Const('array1',arraySort)
	d1array=Function('d1array',arraySort,IntSort(),IntSort())
	_x1=Const('_x1',arraySort)
	_2DUMMY1=Int('_2DUMMY1')
	_N2=Const('_N2',IntSort())
	_2DUMMY8=Function('_2DUMMY8',IntSort(),IntSort())
	_n2=Int('_n2')
	_N1=Const('_N1',IntSort())
	array=Const('array',arraySort)
	main=Int('main')
	d1array1=Function('d1array1',arraySort,IntSort(),IntSort())
	_x2=Int('_x2')
	_1DUMMY5=Function('_1DUMMY5',IntSort(),IntSort())
	printEven=Function('printEven',RealSort(),IntSort())
	printOdd=Function('printOdd',RealSort(),IntSort())
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(array1 == array)
	_s.add(ForAll([_x2,_x1],Implies(_x2>=0,d1array1(_x1,_x2) == d1array(_x1,_x2))))
	_s.add(i1 == _N2)
	_s.add(num1 == __VERIFIER_nondet_int2)
	_s.add(_2DUMMY1 == _2DUMMY8(_N2))
	_s.add(main == 0)
	_s.add(_1DUMMY1 == _1DUMMY5(_N1))
	_s.add(_1DUMMY5(0) == 0)
	_s.add(((_N1)>=(((-(0))+(__VERIFIER_nondet_int2)))))
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),((_f(_n1))<(__VERIFIER_nondet_int2)))))
	_s.add(Or(_N1==0,(((_N1-1))<(__VERIFIER_nondet_int2))))
	_s.add(_2DUMMY8(0) == 0)
	_s.add(((_N2)>=(((-(0))+(__VERIFIER_nondet_int2)))))
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),((_f(_n2))<(__VERIFIER_nondet_int2)))))
	_s.add(Or(_N2==0,(((_N2-1))<(__VERIFIER_nondet_int2))))
	_s.add(array1 == array)
	_s.add(ForAll([_x2,_x1],Implies(_x2>=0,d1array1(_x1,_x2) == d1array(_x1,_x2))))
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(Not(ForAll([_n2],Implies(And(_n2<_N2,_n2>=0),Implies(((((d1array(array,_n2))%(2)))!=(0)),((((d1array(array,_n2))%(2)))!=(0)))))))

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
