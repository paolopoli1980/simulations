import sys
sys.path.append("../")
import gravitycalc
import math
numberofmasses=2
bodies=[]

au=149597870700

for i in range(numberofmasses):
    bodies.append(gravitycalc.body())

bodies[0].x=0
bodies[0].y=0
bodies[0].z=0
bodies[0].vx=0
bodies[0].vy=0
bodies[0].vz=0
bodies[0].ax=0
bodies[0].ay=0
bodies[0].az=0
bodies[0].mass=1.989*10**30

bodies[0].index=0
bodies[0].radius=2

bodies[1].x=1*au
bodies[1].y=0
bodies[1].z=0
bodies[1].vx=0
bodies[1].vy=29788.62*1.1
bodies[1].vz=0
bodies[1].ax=0
bodies[1].ay=0
bodies[1].az=0
bodies[1].mass=5.972*10**24 
bodies[1].index=1
bodies[1].radius=1



niterations=1500
dt=365*24*3600*8/niterations
#dt=31536000/niterations
f1=open("datamotio.txt","w")
f2=open("energy.txt","w")

string=""
for i in range(niterations):
    for j in range(numberofmasses):
        gravitycalc.rk4(j,dt,numberofmasses,bodies)
        #gravitycalc.eulero(j,dt,numberofmasses,bodies)
    energiakin=0
    for j in range(numberofmasses):
        #print(j)
	
        bodies[j].x=bodies[j].virtualx
        bodies[j].y=bodies[j].virtualy
        bodies[j].z=bodies[j].virtualz
        bodies[j].vx=bodies[j].virtualvx
        bodies[j].vy=bodies[j].virtualvy
        bodies[j].vz=bodies[j].virtualvz
        string=str(bodies[j].radius)+str(';')+str(bodies[j].x/au)+str(";")+str(bodies[j].y/au)+str(";")+str(bodies[j].z/au)+str(";")+str(bodies[j].vx)+str(";")+str(bodies[j].vy)+str(";")+str(bodies[j].vz)+str(";") 

        energiakin+=0.5*bodies[j].mass*(bodies[j].vx**2+bodies[j].vy**2+bodies[j].vz**2)
        	
        f1.write(string+str('\n'))
    energiapot=0    
    for j in range(numberofmasses):
        for k in range(j,numberofmasses):
            if k!=j:
                
                dist=math.sqrt((bodies[k].x-bodies[j].x)**2+(bodies[k].y-bodies[j].y)**2+(bodies[k].z-bodies[j].z)**2)
                energiapot-=bodies[k].mass*bodies[j].mass*bodies[k].G/dist
    totenergy=energiapot+energiakin
    f2.write(str(totenergy)+'\n')
f1.close()        
f2.close()


#for el in bodies:
#    print (el.acceleration)
