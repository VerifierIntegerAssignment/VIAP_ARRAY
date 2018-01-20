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
	j1=Int('j1')
	dst1=Const('dst1',arraySort)
	src1=Const('src1',arraySort)
	_x1=Const('_x1',arraySort)
	_x2=Int('_x2')
	__VERIFIER_nondet_int2=Function('__VERIFIER_nondet_int2',IntSort(),IntSort())
	dst=Const('dst',arraySort)
	_N2=Const('_N2',IntSort())
	main=Int('main')
	d1array=Function('d1array',arraySort,IntSort(),IntSort())
	i1=Int('i1')
	_N3=Const('_N3',IntSort())
	_N1=Const('_N1',IntSort())
	d1array4=Function('d1array4',arraySort,IntSort(),IntSort(),IntSort())
	d1array6=Function('d1array6',arraySort,IntSort(),IntSort(),IntSort())
	x1=Int('x1')
	d1array1=Function('d1array1',arraySort,IntSort(),IntSort())
	d1array2=Function('d1array2',arraySort,IntSort(),IntSort(),IntSort())
	src=Const('src',arraySort)
	_n2=Int('_n2')
	_n3=Int('_n3')
	_n1=Int('_n1')
	_k1=Int('_k1')
	_k2=Int('_k2')
	_k3=Int('_k3')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(src1 == src)
	_s.add(dst1 == dst)
	_s.add(i1 == _N2)
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array1(dst,_x2) == d1array6(dst,_x2,_N3))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array1(src,_x2) == d1array6(src,_x2,_N3))))
	_s.add(j1 == _N1)
	_s.add(main == 0)
	_s.add(x1 == _N3)
	_s.add(ForAll([_x2,_n1],Implies(And(_x2>=0,_n1>=0),d1array2(dst,_x2,_n1 + 1) == d1array2(dst,_x2,_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array2(src,_n1,_n1 + 1) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(dst,_x2,0) == d1array(dst,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(src,_x2,0) == d1array(src,_x2))))
	_s.add(_N1 >= 100000)
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),_f(_n1) < 100000)))
	_s.add(Or(_N1==0,_N1 - 1 < 100000))
	_s.add(ForAll([_n2],Implies(_n2>=0,d1array4(dst,_n2,_n2 + 1) == d1array4(src,_n2,_n2))))
	_s.add(ForAll([_x2,_n2],Implies(And(_x2>=0,_n2>=0),d1array4(src,_x2,_n2 + 1) == d1array4(src,_x2,_n2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(dst,_x2,0) == d1array2(dst,_x2,_N1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(src,_x2,0) == d1array2(src,_x2,_N1))))
	_s.add(Or(_N2 >= 100000,((d1array4(src,_N2,_N2))==(0))))
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),And(_f(_n2) < 100000,((d1array4(src,_f(_n2),_f(_n2)))!=(0))))))
	_s.add(Or(_N2==0,And((_N2-1) < 100000,((d1array4(src,(_N2-1),(_N2-1)))!=(0)))))
	_s.add(ForAll([_x2,_n3],Implies(And(_x2>=0,_n3>=0),d1array6(dst,_x2,_n3 + 1) == d1array6(dst,_x2,_n3))))
	_s.add(ForAll([_x2,_n3],Implies(And(_x2>=0,_n3>=0),d1array6(src,_x2,_n3 + 1) == d1array6(src,_x2,_n3))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(dst,_x2,0) == d1array4(dst,_x2,_N2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(src,_x2,0) == d1array4(src,_x2,_N2))))
	_s.add(_N3 >= _N2)
	_s.add(ForAll([_n3],Implies(And(_n3 < _N3,_n3>=0),_f(_n3) < _N2)))
	_s.add(Or(_N3==0,_N3 - 1 < _N2))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(dst,_x2,_N1) == d1array(dst,_x2))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array2(src,_n1,_N1) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array4(dst,_n2,_N2) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array4(src,_n1,_N2) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array6(dst,_n2,_N3) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array6(src,_n1,_N3) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(dst,_x2,_N1) == d1array(dst,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(dst,_x2,_N1) == d1array2(dst,_x2,_N1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array2(src,_n1,_N1) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array2(src,_n1,_N1) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array4(dst,_n2,_N2) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array4(dst,_n2,_N2) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array4(src,_n1,_N2) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array4(src,_n1,_N2) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array6(dst,_n2,_N3) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array6(dst,_n2,_N3) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array6(src,_n1,_N3) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array6(src,_n1,_N3) == __VERIFIER_nondet_int2(_n1))))
	_s.add(src1 == src)
	_s.add(dst1 == dst)
	_s.add(_k1>=0)
	_s.add(_k2>=0)
	_s.add(_k3>=0)
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(_N3>=0)
	_s.add(Not(ForAll([_n3],Implies(And(_n3<_N3,_n3>=0),((d1array6(dst,_n3,_N3))==(d1array6(src,_n3,_N3)))))))

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
