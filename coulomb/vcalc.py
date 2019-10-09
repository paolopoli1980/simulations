import math
qp=2*1.602*10**(-19)
qe=-1.602*10**(-19)
mp=2*1.6726231*10**(-27)
me=9.109*10**(-31)
const=8.85418781762*10**(-12)
ree=2*5.29*10**(-11)
rpe=5.29*10**(-11)

fpe=qp*qe*const/rpe**2
fee=qe*qe*const/ree**2

ftot=fpe+fee

atot=-(ftot/me)
v=math.sqrt(atot*rpe)
print (v)
