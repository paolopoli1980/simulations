import random
import math
import dots


#################### setting part ########################

numberdots=3
maxstate=1
dotsx=[]
for i in range(numberdots):
    dotsx.append(dots.dot(i))

for j in range(numberdots):
    
    dotsx[j].maxstate=maxstate
    

################# connection part #######################

dotsx[0].connections=[1,2]
dotsx[1].connections=[0,2]
dotsx[2].connections=[0,1]
for i in range(numberdots):
    dotsx[i].state=0
###############################################################
dotsx[0].states=[0,0,1,1]
dotsx[1].states=[0,1,0,1]
dotsx[2].states=[1,0,0,1]


niter=100
listofstates=[]

simdot=dots.simdot()

liststates=simdot.simdots(niter,dotsx).copy()
print (liststates)
