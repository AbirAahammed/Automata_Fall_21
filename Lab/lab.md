# DFA practice
## 1
regex = (0*001)+(0*0100*)+(1000*)
![(0*001)+(0*0100*)+(1000*)](lab_1.png)

## 2
regex = 0(1+0)0*+(1+0)0*+0*
![0(1+0)0*+(1+0)0*+0*](lab_2.png)

## 3 a
$+0+01+011+011(0*1*)*+1+10+101+101(0*1*)*+11+11(0*1*)*
simplified: $+0+0(1+11(0+1)*)+1+1(0+(01+1)(0+1)*)
![$+0+0(1+11(0+1)*)+1+1(0+(01+1)(0+1)*)](lab_3a.png)

## 3 b

(0*1*)*001(0*1*)*
![(0*1*)*001(0*1*)*](lab_3b.png)