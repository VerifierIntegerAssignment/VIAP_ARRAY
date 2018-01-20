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
	volArray1=Const('volArray1',arraySort)
	_n1=Int('_n1')
	j8=Function('j8',IntSort(),IntSort())
	d1array10=Function('d1array10',arraySort,IntSort(),IntSort(),IntSort())
	j1=Int('j1')
	_x1=Const('_x1',arraySort)
	_x2=Int('_x2')
	__VERIFIER_nondet_int2=Int('__VERIFIER_nondet_int2')
	i1=Int('i1')
	volArray=Const('volArray',arraySort)
	main=Int('main')
	_N1=Function('_N1',IntSort(),IntSort())
	_N2=Const('_N2',IntSort())
	_N3=Const('_N3',IntSort())
	d1array=Function('d1array',arraySort,IntSort(),IntSort())
	d1array8=Function('d1array8',arraySort,IntSort(),IntSort(),IntSort())
	MINVAL1=Int('MINVAL1')
	CELLCOUNT1=Int('CELLCOUNT1')
	d1array5=Function('d1array5',arraySort,IntSort(),IntSort(),IntSort(),IntSort())
	d1array1=Function('d1array1',arraySort,IntSort(),IntSort())
	MINVAL=Int('MINVAL')
	_n2=Int('_n2')
	_n3=Int('_n3')
	j=Int('j')
	i=Int('i')
	_k1=Int('_k1')
	_k2=Int('_k2')
	_k3=Int('_k3')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(volArray1 == volArray)
	_s.add(MINVAL1 == If(((__VERIFIER_nondet_int2)>(1)),2,MINVAL))
	_s.add(CELLCOUNT1 == __VERIFIER_nondet_int2)
	_s.add(ForAll([_x2],Implies(And(_x2>=0,_x2<CELLCOUNT1),d1array1(volArray,_x2) == If(((__VERIFIER_nondet_int2)>(1)),If(((((__VERIFIER_nondet_int2)%(4)))==(0)),d1array10(volArray,_x2,_N3),d1array(volArray,_x2)),d1array(volArray,_x2)))))
	_s.add(j1 == If(((__VERIFIER_nondet_int2)>(1)),If(((((__VERIFIER_nondet_int2)%(4)))==(0)),j8(_N2),j),j))
	_s.add(main == If(Or(((((__VERIFIER_nondet_int2)%(4)))==(0)),((__VERIFIER_nondet_int2)<=(1))),1,If(((__VERIFIER_nondet_int2)>(1)),If(((((__VERIFIER_nondet_int2)%(4)))!=(0)),1,0),0)))
	_s.add(i1 == If(((__VERIFIER_nondet_int2)>(1)),If(((((__VERIFIER_nondet_int2)%(4)))==(0)),_N3,i),i))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1<_N1(_n2),And(_n2<_N2,And(_n1>=0,_n2>=0))),d1array5(volArray,((((((_n2)+(1)))*(4)))-(((-(_n1))+(4)))),((_n1)+(1)),_n2) == -_n1 + 4)))
	_s.add(ForAll([_x2,_n2],Implies(And(_n2<_N2,And(And(_x2>=0,_n2>=0),_x2<CELLCOUNT1)),d1array5(volArray,_x2,0,_n2) == d1array8(volArray,_x2,_n2))))
	_s.add(ForAll([_n2],Implies(And(_n2<_N2,_n2>=0),-_N1(_n2) + 4 < 1)))
	_s.add(ForAll([_n1,_n2],Implies(And(((_n1)<(_N1(_n2))),And(_n1>=0,_n2>=0)),((((-(_f(_n1)))+(4)))>=(1)))))
	_s.add(ForAll([_n2],Implies(_n2>=0,Or(_N1(_n2)==0,-_N1(_n2) + 5 >= 1))))
	_s.add(ForAll([_x2,_n2],Implies(And(_n2<_N2,And(And(_x2>=0,_n2>=0),_x2<CELLCOUNT1)),d1array8(volArray,_x2,((_n2)+(1))) == d1array5(volArray,_x2,_N1(_n2),_n2))))
	_s.add(ForAll([_n2],Implies(And(_n2<_N2,_n2>=0),j8(_n2 + 1) == -_N1(_n2) + 4)))
	_s.add(ForAll([_x2],Implies(And(_x2>=0,_x2<CELLCOUNT1),d1array8(volArray,_x2,0) == d1array(volArray,_x2))))
	_s.add(j8(0) == j)
	_s.add(((((_N2)+(1)))>(((__VERIFIER_nondet_int2)/(4)))))
	_s.add(ForAll([_n2],Implies(And(((_n2)<(_N2)),_n2>=0),((((_f(_n2))+(1)))<=(((__VERIFIER_nondet_int2)/(4)))))))
	_s.add(Or(_N2==0,_N2 <= __VERIFIER_nondet_int2/4))
	_s.add(ForAll([_x2,_n3],Implies(And(_n3<_N3,And(And(_x2>=0,_n3>=0),_x2<CELLCOUNT1)),d1array10(volArray,_x2,((_n3)+(1))) == d1array10(volArray,_x2,_n3))))
	_s.add(ForAll([_x2],Implies(And(_x2>=0,_x2<CELLCOUNT1),d1array10(volArray,_x2,0) == d1array8(volArray,_x2,_N2))))
	_s.add(((_N3)>=(((__VERIFIER_nondet_int2)-(0)))))
	_s.add(ForAll([_n3],Implies(And(((_n3)<(_N3)),_n3>=0),((((_f(_n3))+(0)))<(__VERIFIER_nondet_int2)))))
	_s.add(Or(_N3==0,(((_N3-1))<(__VERIFIER_nondet_int2))))
	_s.add(ForAll([_x2,_n1,_n2],Implies(And(_n1<_N1(_n2),And(_n2<_N2,And(And(_x2>=0,And(_n1>=0,_n2>=0)),_x2<CELLCOUNT1))),d1array8(volArray,_x2,_N2) == If(((((-(_n1))+(4)))>=(2)),If(((_x2)==(((((((_n2)+(1)))*(4)))-(((-(_n1))+(4)))))),((-(_n1))+(4)),d1array(volArray,_x2)),If(((_x2)==(((((((_n2)+(1)))*(4)))-(((-(_n1))+(4)))))),0,d1array(volArray,_x2))))))
	_s.add(ForAll([_x2,_n1,_n2],Implies(And(_n1<_N1(_n2),And(_n2<_N2,And(And(_x2>=0,And(_n1>=0,_n2>=0)),_x2<CELLCOUNT1))),d1array5(volArray,_x2,_N1(_n2),_n2) == If(((((-(_n1))+(4)))>=(2)),If(((_x2)==(((((((_n2)+(1)))*(4)))-(((-(_n1))+(4)))))),((-(_n1))+(4)),d1array5(volArray,_x2,_N1(_n2),_n2)),If(((_x2)==(((((((_n2)+(1)))*(4)))-(((-(_n1))+(4)))))),0,d1array5(volArray,_x2,_N1(_n2),_n2))))))
	_s.add(ForAll([_x2,_n1,_n2],Implies(And(_n1<_N1(_n2),And(_n2<_N2,And(And(_x2>=0,And(_n1>=0,_n2>=0)),_x2<CELLCOUNT1))),d1array8(volArray,_x2,_N2) == If(((((-(_n1))+(4)))>=(2)),If(((_x2)==(((((((_n2)+(1)))*(4)))-(((-(_n1))+(4)))))),((-(_n1))+(4)),d1array(volArray,_x2)),If(((_x2)==(((((((_n2)+(1)))*(4)))-(((-(_n1))+(4)))))),0,d1array(volArray,_x2))))))
	_s.add(ForAll([_x2,_n1,_n2],Implies(And(_n1<_N1(_n2),And(_n2<_N2,And(And(_x2>=0,And(_n1>=0,_n2>=0)),_x2<CELLCOUNT1))),d1array8(volArray,_x2,_N2) == If(((((-(_n1))+(4)))>=(2)),If(((_x2)==(((((((_n2)+(1)))*(4)))-(((-(_n1))+(4)))))),((-(_n1))+(4)),d1array8(volArray,_x2,((_n2)+(1)))),If(((_x2)==(((((((_n2)+(1)))*(4)))-(((-(_n1))+(4)))))),0,d1array8(volArray,_x2,((_n2)+(1))))))))
	_s.add(ForAll([_x2,_n1,_n2],Implies(And(_n1<_N1(_n2),And(_n2<_N2,And(And(_x2>=0,And(_n1>=0,_n2>=0)),_x2<CELLCOUNT1))),d1array10(volArray,_x2,_N3) == If(((((-(_n1))+(4)))>=(2)),If(((_x2)==(((((((_n2)+(1)))*(4)))-(((-(_n1))+(4)))))),((-(_n1))+(4)),d1array10(volArray,_x2,_N3)),If(((_x2)==(((((((_n2)+(1)))*(4)))-(((-(_n1))+(4)))))),0,d1array10(volArray,_x2,_N3))))))
	_s.add(volArray1 == volArray)
	_s.add((_N3==(__VERIFIER_nondet_int2-0)))
	_s.add(_k1>=0)
	_s.add(_k3>=0)
	_s.add(ForAll([_n2],_N1(_n2)>=0))
	_s.add(_N2>=0)
	_s.add(_N3>=0)
	_s.add(((__VERIFIER_nondet_int2%4)==0))
	_s.add((__VERIFIER_nondet_int2>1))
	_s.add(Not(ForAll([_n3],Implies(And(_n3<_N3,_n3>=0),Implies(((((__VERIFIER_nondet_int2)%(4)))==(0)),Or(((d1array10(volArray,_n3,_N3))>=(2)),((d1array10(volArray,_n3,_N3))==(0))))))))

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
