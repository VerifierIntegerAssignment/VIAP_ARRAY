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
	FIXEDVAL=Int('FIXEDVAL')
	_x1=Const('_x1',arraySort)
	_x2=Int('_x2')
	__VERIFIER_nondet_int2=Int('__VERIFIER_nondet_int2')
	DEFAULTVAL1=Int('DEFAULTVAL1')
	_N2=Const('_N2',IntSort())
	value1=Int('value1')
	d1array22=Function('d1array22',arraySort,IntSort(),IntSort(),IntSort())
	main=Int('main')
	d1array24=Function('d1array24',arraySort,IntSort(),IntSort(),IntSort())
	ReadFromPort=Int('ReadFromPort')
	_N1=Const('_N1',IntSort())
	i1=Int('i1')
	d1array=Function('d1array',arraySort,IntSort(),IntSort())
	a1=Const('a1',arraySort)
	FIXEDVAL1=Int('FIXEDVAL1')
	ReadFromPort_4=Int('ReadFromPort_4')
	ReadFromPort_2=Int('ReadFromPort_2')
	ReadFromPort_3=Int('ReadFromPort_3')
	DEFAULTVAL=Int('DEFAULTVAL')
	ReadFromPort_1=Int('ReadFromPort_1')
	d1array1=Function('d1array1',arraySort,IntSort(),IntSort())
	a=Const('a',arraySort)
	SIZE1=Int('SIZE1')
	i=Int('i')
	_n1=Int('_n1')
	value=Int('value')
	_n2=Int('_n2')
	_k1=Int('_k1')
	_k2=Int('_k2')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(a1 == a)
	_s.add(i1 == If(((__VERIFIER_nondet_int2)>(1)),If(((((__VERIFIER_nondet_int2)%(5)))==(0)),_N2,i),i))
	_s.add(ForAll([_x2],Implies(And(_x2>=0,_x2<SIZE1),d1array1(a,_x2) == If(((__VERIFIER_nondet_int2)>(1)),If(((((__VERIFIER_nondet_int2)%(5)))==(0)),d1array24(a,_x2,_N2),d1array(a,_x2)),d1array(a,_x2)))))
	_s.add(FIXEDVAL1 == If(((__VERIFIER_nondet_int2)>(1)),10,FIXEDVAL))
	_s.add(value1 == If(((__VERIFIER_nondet_int2)>(1)),If(((((__VERIFIER_nondet_int2)%(5)))==(0)),ReadFromPort_4,value),value))
	_s.add(main == If(Or(((((__VERIFIER_nondet_int2)%(5)))==(0)),((__VERIFIER_nondet_int2)<=(1))),1,If(((__VERIFIER_nondet_int2)>(1)),If(((((__VERIFIER_nondet_int2)%(5)))!=(0)),1,0),0)))
	_s.add(DEFAULTVAL1 == If(((__VERIFIER_nondet_int2)>(1)),0,DEFAULTVAL))
	_s.add(SIZE1 == __VERIFIER_nondet_int2)
	_s.add(ForAll([_n1],Implies(And(_n1<_N1,_n1>=0),d1array22(a,((((((_n1)+(1)))*(5)))-(1)),((_n1)+(1))) == ReadFromPort_4)))
	_s.add(ForAll([_n1],Implies(And(_n1<_N1,_n1>=0),d1array22(a,((((((_n1)+(1)))*(5)))-(3)),((_n1)+(1))) == ReadFromPort_2)))
	_s.add(ForAll([_n1],Implies(And(_n1<_N1,_n1>=0),d1array22(a,((((((_n1)+(1)))*(5)))-(2)),((_n1)+(1))) == ReadFromPort_3)))
	_s.add(ForAll([_n1],Implies(And(_n1<_N1,_n1>=0),d1array22(a,((((((_n1)+(1)))*(5)))-(5)),((_n1)+(1))) == ReadFromPort)))
	_s.add(ForAll([_n1],Implies(And(_n1<_N1,_n1>=0),d1array22(a,((((((_n1)+(1)))*(5)))-(4)),((_n1)+(1))) == ReadFromPort_1)))
	_s.add(ForAll([_x2],Implies(And(_x2>=0,_x2<SIZE1),d1array22(a,_x2,0) == d1array(a,_x2))))
	_s.add(((((_N1)+(1)))>(((__VERIFIER_nondet_int2)/(5)))))
	_s.add(ForAll([_n1],Implies(And(((_n1)<(_N1)),_n1>=0),((((_f(_n1))+(1)))<=(((__VERIFIER_nondet_int2)/(5)))))))
	_s.add(Or(_N1==0,_N1 <= __VERIFIER_nondet_int2/5))
	_s.add(ForAll([_x2,_n2],Implies(And(_n2<_N2,And(And(_x2>=0,_n2>=0),_x2<SIZE1)),d1array24(a,_x2,((_n2)+(1))) == d1array24(a,_x2,_n2))))
	_s.add(ForAll([_x2],Implies(And(_x2>=0,_x2<SIZE1),d1array24(a,_x2,0) == d1array22(a,_x2,_N1))))
	_s.add(((_N2)>=(((__VERIFIER_nondet_int2)-(0)))))
	_s.add(ForAll([_n2],Implies(And(((_n2)<(_N2)),_n2>=0),((((_f(_n2))+(0)))<(__VERIFIER_nondet_int2)))))
	_s.add(Or(_N2==0,(((_N2-1))<(__VERIFIER_nondet_int2))))
	_s.add(ForAll([_x2,_n1],Implies(And(_n1<_N1,And(And(_x2>=0,_n1>=0),_x2<SIZE1)),d1array22(a,_x2,_N1) == If(((ReadFromPort_4)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(1)))),ReadFromPort_4,If(((ReadFromPort_3)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(2)))),ReadFromPort_3,If(((ReadFromPort_2)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),ReadFromPort_2,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),10,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))))))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(2)))),10,If(((ReadFromPort_2)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),ReadFromPort_2,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),10,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))))))))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(1)))),10,If(((ReadFromPort_3)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(2)))),ReadFromPort_3,If(((ReadFromPort_2)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),ReadFromPort_2,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),10,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))))))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(2)))),10,If(((ReadFromPort_2)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),ReadFromPort_2,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),10,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10)))))))))))))
	_s.add(ForAll([_x2,_n1],Implies(And(_n1<_N1,And(And(_x2>=0,_n1>=0),_x2<SIZE1)),d1array24(a,_x2,_N2) == If(((ReadFromPort_4)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(1)))),ReadFromPort_4,If(((ReadFromPort_3)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(2)))),ReadFromPort_3,If(((ReadFromPort_2)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),ReadFromPort_2,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),10,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))))))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(2)))),10,If(((ReadFromPort_2)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),ReadFromPort_2,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),10,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))))))))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(1)))),10,If(((ReadFromPort_3)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(2)))),ReadFromPort_3,If(((ReadFromPort_2)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),ReadFromPort_2,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),10,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))))))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(2)))),10,If(((ReadFromPort_2)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),ReadFromPort_2,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(3)))),10,If(((ReadFromPort_1)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),ReadFromPort_1,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10))),If(((_x2)==(((((((_n1)+(1)))*(5)))-(4)))),10,If(((ReadFromPort)!=(0)),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),ReadFromPort,10),If(((_x2)==(((((((_n1)+(1)))*(5)))-(5)))),10,10)))))))))))))
	_s.add(a1 == a)
	_s.add((_N2==(__VERIFIER_nondet_int2-0)))
	_s.add(_k1>=0)
	_s.add(_k2>=0)
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(((__VERIFIER_nondet_int2%5)==0))
	_s.add((__VERIFIER_nondet_int2>1))
	_s.add(Not(ForAll([_n2],Implies(And(_n2<_N2,_n2>=0),Implies(((((__VERIFIER_nondet_int2)%(5)))==(0)),((d1array24(a,_n2,_N2))!=(0)))))))

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
