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
	__VERIFIER_nondet_int3=Int('__VERIFIER_nondet_int3')
	__VERIFIER_nondet_int2=Int('__VERIFIER_nondet_int2')
	i1=Int('i1')
	_N1=Const('_N1',IntSort())
	marker1=Int('marker1')
	d1array1=Function('d1array1',arraySort,IntSort(),IntSort())
	a1=Const('a1',arraySort)
	i=Int('i')
	d1array=Function('d1array',arraySort,IntSort(),IntSort())
	_n1=Int('_n1')
	main=Int('main')
	_x1=Const('_x1',arraySort)
	_x2=Int('_x2')
	pos1=Int('pos1')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(a1 == a)
	_s.add(i1 == If(And(((__VERIFIER_nondet_int3)>=(0)),((__VERIFIER_nondet_int3)<(100000))),_N1,i))
	_s.add(marker1 == __VERIFIER_nondet_int2)
	_s.add(ForAll([_x2,_x1],Implies(_x2>=0,d1array1(_x1,_x2) == If(And(((__VERIFIER_nondet_int3)>=(0)),((__VERIFIER_nondet_int3)<(100000))),If(And(((_x1)==(a)),((_x2)==(__VERIFIER_nondet_int3))),__VERIFIER_nondet_int2,d1array(_x1,_x2)),d1array(_x1,_x2)))))
	_s.add(pos1 == __VERIFIER_nondet_int3)
	_s.add(main == 0)
	_s.add(((If(And(((a)==(a)),((_N1)==(__VERIFIER_nondet_int3))),__VERIFIER_nondet_int2,d1array(a,_N1)))==(__VERIFIER_nondet_int2)))
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),((If(And(((a)==(a)),((_f(_n1))==(__VERIFIER_nondet_int3))),__VERIFIER_nondet_int2,d1array(a,_f(_n1))))!=(__VERIFIER_nondet_int2)))))
	_s.add(Or(_N1==0,((If(And(((a)==(a)),(((_N1-1))==(__VERIFIER_nondet_int3))),__VERIFIER_nondet_int2,d1array(a,(_N1-1))))!=(__VERIFIER_nondet_int2))))
	_s.add(_N1>=0)
	_s.add(Not(Implies(And(((__VERIFIER_nondet_int3)>=(0)),((__VERIFIER_nondet_int3)<(100000))),((_N1)<=(__VERIFIER_nondet_int3)))))

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
