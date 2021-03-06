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
	_n1=Int('_n1')
	ret2_var1=Int('ret2_var1')
	temp1=Int('temp1')
	f1_3_RET1=Int('f1_3_RET1')
	_x1=Const('_x1',arraySort)
	_x2=Int('_x2')
	x1=Const('x1',arraySort)
	f1_2_RET1=Int('f1_2_RET1')
	f1_3_ret10=Function('f1_3_ret10',IntSort(),IntSort())
	i1=Int('i1')
	f1_1_ret1=Int('f1_1_ret1')
	ret5_var1=Int('ret5_var1')
	f1_2_i1=Int('f1_2_i1')
	main=Int('main')
	d1array=Function('d1array',arraySort,IntSort(),IntSort())
	f1_1_i1=Int('f1_1_i1')
	_N2=Const('_N2',IntSort())
	_N3=Const('_N3',IntSort())
	_N1=Const('_N1',IntSort())
	f1_1_ret4=Function('f1_1_ret4',IntSort(),IntSort())
	_N4=Const('_N4',IntSort())
	_N5=Const('_N5',IntSort())
	f1_3_i1=Int('f1_3_i1')
	__VERIFIER_nondet_int2=Function('__VERIFIER_nondet_int2',IntSort(),IntSort())
	d1array8=Function('d1array8',arraySort,IntSort(),IntSort(),IntSort())
	_1_FAILED1=Int('_1_FAILED1')
	d1array1=Function('d1array1',arraySort,IntSort(),IntSort())
	d1array2=Function('d1array2',arraySort,IntSort(),IntSort(),IntSort())
	f1_3_ret1=Int('f1_3_ret1')
	_n2=Int('_n2')
	f1_1_RET1=Int('f1_1_RET1')
	f1_2_ret6=Function('f1_2_ret6',IntSort(),IntSort())
	f1_2_ret1=Int('f1_2_ret1')
	_n4=Int('_n4')
	_n5=Int('_n5')
	ret1=Int('ret1')
	_n3=Int('_n3')
	x=Const('x',arraySort)
	avg=Function('avg',IntSort(),IntSort())
	_k1=Int('_k1')
	_k4=Int('_k4')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(x1 == x)
	_s.add(f1_2_i1 == _N3)
	_s.add(f1_1_ret1 == f1_1_ret4(_N2))
	_s.add(temp1 == If(And(((x)==(x)),((0)==(1))),d1array2(x,0,_N1),If(And(((x)==(x)),((0)==(0))),d1array2(x,1,_N1),d1array2(x,0,_N1))))
	_s.add(ret5_var1 == ((f1_3_ret10(_N5))/(20)))
	_s.add(_1_FAILED1 == If(Or(((((f1_1_ret4(_N2))/(20)))!=(((f1_2_ret6(_N3))/(20)))),((((f1_1_ret4(_N2))/(20)))!=(((f1_3_ret10(_N5))/(20))))),1,0))
	_s.add(f1_3_i1 == _N5)
	_s.add(f1_3_RET1 == ((f1_3_ret10(_N5))/(20)))
	_s.add(ret1 == ((f1_1_ret4(_N2))/(20)))
	_s.add(i1 == _N4)
	_s.add(ret2_var1 == ((f1_2_ret6(_N3))/(20)))
	_s.add(f1_2_ret1 == f1_2_ret6(_N3))
	_s.add(main == 1)
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array1(x,_x2) == If(And(((x)==(x)),((_x2)==(19))),If(And(((x)==(x)),((0)==(1))),d1array2(x,0,_N1),If(And(((x)==(x)),((0)==(0))),d1array2(x,1,_N1),d1array2(x,0,_N1))),d1array8(x,_x2,_N4)))))
	_s.add(f1_2_RET1 == ((f1_2_ret6(_N3))/(20)))
	_s.add(f1_1_i1 == _N2)
	_s.add(f1_3_ret1 == f1_3_ret10(_N5))
	_s.add(f1_1_RET1 == ((f1_1_ret4(_N2))/(20)))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array2(x,_n1,_n1 + 1) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(x,_x2,0) == d1array(x,_x2))))
	_s.add(_N1 >= 20)
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),_f(_n1) < 20)))
	_s.add(Or(_N1==0,_N1 - 1 < 20))
	_s.add(ForAll([_n2],Implies(_n2>=0,f1_1_ret4(_n2 + 1) == ((f1_1_ret4(_n2))+(d1array2(x,_n2,_N1))))))
	_s.add(f1_1_ret4(0) == 0)
	_s.add(_N2 >= 20)
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),_f(_n2) < 20)))
	_s.add(Or(_N2==0,_N2 - 1 < 20))
	_s.add(ForAll([_n3],Implies(_n3>=0,f1_2_ret6(_n3 + 1) == ((f1_2_ret6(_n3))+(If(And(((x)==(x)),((_n3)==(1))),d1array2(x,0,_N1),If(And(((x)==(x)),((_n3)==(0))),d1array2(x,1,_N1),d1array2(x,_n3,_N1))))))))
	_s.add(f1_2_ret6(0) == 0)
	_s.add(_N3 >= 20)
	_s.add(ForAll([_n3],Implies(And(_n3 < _N3,_n3>=0),_f(_n3) < 20)))
	_s.add(Or(_N3==0,_N3 - 1 < 20))
	_s.add(ForAll([_n4],Implies(_n4>=0,d1array8(x,_n4,_n4 + 1) == d1array8(x,_n4 + 1,_n4))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array8(x,_x2,0) == If(((_x2)==(1)),d1array2(x,0,_N1),If(((_x2)==(0)),d1array2(x,1,_N1),d1array2(x,_x2,_N1))))))
	_s.add(_N4 >= 19)
	_s.add(ForAll([_n4],Implies(And(_n4 < _N4,_n4>=0),_f(_n4) < 19)))
	_s.add(Or(_N4==0,_N4 - 1 < 19))
	_s.add(ForAll([_n5],Implies(_n5>=0,f1_3_ret10(_n5 + 1) == ((f1_3_ret10(_n5))+(If(And(((x)==(x)),((_n5)==(19))),If(And(((x)==(x)),((0)==(1))),d1array2(x,0,_N1),If(And(((x)==(x)),((0)==(0))),d1array2(x,1,_N1),d1array2(x,0,_N1))),d1array8(x,_n5,_N4)))))))
	_s.add(f1_3_ret10(0) == 0)
	_s.add(_N5 >= 20)
	_s.add(ForAll([_n5],Implies(And(_n5 < _N5,_n5>=0),_f(_n5) < 20)))
	_s.add(Or(_N5==0,_N5 - 1 < 20))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array2(x,_n1,_N1) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n4,_n1],Implies(And(_n4>=0,_n1>=0),d1array8(x,_n4,_N4) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array2(x,_n1,_N1) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array2(x,_n1,_N1) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n4,_n1],Implies(And(_n4>=0,_n1>=0),d1array8(x,_n4,_N4) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n4,_n1],Implies(And(_n4>=0,_n1>=0),d1array8(x,_n4,_N4) == __VERIFIER_nondet_int2(_n1))))
	_s.add(x1 == x)
	_s.add(_k1>=0)
	_s.add(_k4>=0)
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(_N3>=0)
	_s.add(_N4>=0)
	_s.add(_N5>=0)
	_s.add(Not(((_1_FAILED1)==(0))))

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
