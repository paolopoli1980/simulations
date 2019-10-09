##############################################################################################
##########A simple electrostatic model on atoms ####################################
##############################################################################################
##############################################################################################

#import numpy as np
import math
class atom:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
        self.vx=0
        self.vy=0
        self.vz=0
        self.ax=0
        self.ay=0
        self.az=0
        self.virtualx=0
        self.virtualy=0
        self.virtualz=0
        self.virtualvx=0
        self.virtualvy=0
        self.virtualvz=0
        self.virutalax=0
        self.virtualay=0
        self.virtualaz=0        
        self.mass=0
        self.charge=0
        self.index=0
        self.colconst=8.85418781762*10**(-12)
        self.force=0
        self.acceleration=0
        self.radius=0

    def atomic_forces(self,numberofcharges):
	self.ax=0
	self.ay=0
	self.az=0
        for i in range(numberofcharges):
            if i!=self.index:
                r=math.sqrt((self.x-atoms[i].x)**2+(self.y-atoms[i].y)**2+(self.z-atoms[i].z)**2)
                self.force=self.charge*atoms[i].charge*self.colconst/r**2
                self.acceleration=self.force/self.mass
                ux=(-atoms[i].x+self.x)/r
                uy=(-atoms[i].y+self.y)/r
                uz=(-atoms[i].z+self.z)/r
                self.ax+=self.acceleration*ux
                self.ay+=self.acceleration*uy
                self.az+=self.acceleration*uz
        return [self.ax,self.ay,self.az]                             

def eulero(j,dt,numberofcharges):
    atoms[j].virtualx=atoms[j].x+atoms[j].vx*dt
    atoms[j].virtualy=atoms[j].y+atoms[j].vy*dt
    atoms[j].virtualz=atoms[j].z+atoms[j].vz*dt

    atoms[j].virtualvx=atoms[j].vx+atoms[j].atomic_forces(numberofcharges)[0]*dt
    atoms[j].virtualvy=atoms[j].vy+atoms[j].atomic_forces(numberofcharges)[1]*dt
    atoms[j].virtualvz=atoms[j].vz+atoms[j].atomic_forces(numberofcharges)[2]*dt
    
    
    
def rk4(j,dt,numberofcharges):
   # print (atoms[j].atomic_forces(numberofcharges))
    kv=[[atoms[j].vx,atoms[j].vy,atoms[j].vz],[0,0,0],[0,0,0],[0,0,0]]
    kx=[[atoms[j].x,atoms[j].y,atoms[j].z],[0,0,0],[0,0,0],[0,0,0]]
    ka=[[atoms[j].atomic_forces(numberofcharges)[0],atoms[j].atomic_forces(numberofcharges)[1],atoms[j].atomic_forces(numberofcharges)[2]],[0,0,0],[0,0,0],[0,0,0]]
    
    kx[1][0]=atoms[j].x+atoms[j].vx*dt/2
    kx[1][1]=atoms[j].y+atoms[j].vy*dt/2
    kx[1][2]=atoms[j].z+atoms[j].vz*dt/2
    atoms[j].x=kx[1][0]
    atoms[j].y=kx[1][1]
    atoms[j].z=kx[1][2]
    
    ka[1][0]=atoms[j].atomic_forces(numberofcharges)[0]
    ka[1][1]=atoms[j].atomic_forces(numberofcharges)[1]
    ka[1][2]=atoms[j].atomic_forces(numberofcharges)[2]

    atoms[j].x=kx[0][0]
    atoms[j].y=kx[0][1]
    atoms[j].z=kx[0][2]
    
    kv[1][0]=atoms[j].vx+ka[0][0]*dt/2
    kv[1][1]=atoms[j].vy+ka[0][1]*dt/2
    kv[1][2]=atoms[j].vz+ka[0][2]*dt/2
    
    kx[2][0]=kx[0][0]+kv[1][0]*dt/2
    kx[2][1]=kx[0][1]+kv[1][1]*dt/2
    kx[2][2]=kx[0][2]+kv[1][2]*dt/2

    atoms[j].x=kx[2][0]
    atoms[j].y=kx[2][1]
    atoms[j].z=kx[2][2]

    ka[2][0]=atoms[j].atomic_forces(numberofcharges)[0]
    ka[2][1]=atoms[j].atomic_forces(numberofcharges)[1]
    ka[2][2]=atoms[j].atomic_forces(numberofcharges)[2]

    atoms[j].x=kx[0][0]
    atoms[j].y=kx[0][1]
    atoms[j].z=kx[0][2]

    kv[2][0]=atoms[j].vx+ka[1][0]*dt/2
    kv[2][1]=atoms[j].vy+ka[1][1]*dt/2
    kv[2][2]=atoms[j].vz+ka[1][2]*dt/2
    
    kx[3][0]=kx[0][0]+kv[2][0]*dt
    kx[3][1]=kx[0][1]+kv[2][1]*dt
    kx[3][2]=kx[0][2]+kv[2][2]*dt

    atoms[j].x=kx[3][0]
    atoms[j].y=kx[3][1]
    atoms[j].z=kx[3][2]
    
    ka[3][0]=atoms[j].atomic_forces(numberofcharges)[0]
    ka[3][1]=atoms[j].atomic_forces(numberofcharges)[1]
    ka[3][2]=atoms[j].atomic_forces(numberofcharges)[2]
   
    kv[3][0]=atoms[j].vx+ka[2][0]*dt
    kv[3][1]=atoms[j].vy+ka[2][1]*dt
    kv[3][2]=atoms[j].vz+ka[2][2]*dt

    atoms[j].x=kx[0][0]
    atoms[j].y=kx[0][1]
    atoms[j].z=kx[0][2]
	

    atoms[j].virtualvx=atoms[j].vx+dt/6*(ka[0][0]+2*ka[1][0]+2*ka[2][0]+ka[3][0])
    atoms[j].virtualvy=atoms[j].vy+dt/6*(ka[0][1]+2*ka[1][1]+2*ka[2][1]+ka[3][1])
    atoms[j].virtualvz=atoms[j].vz+dt/6*(ka[0][2]+2*ka[1][2]+2*ka[2][2]+ka[3][2])
    
    atoms[j].virtualx=atoms[j].x+dt/6*(kv[0][0]+2*kv[1][0]+2*kv[2][0]+kv[3][0])
    atoms[j].virtualy=atoms[j].y+dt/6*(kv[0][1]+2*kv[1][1]+2*kv[2][1]+kv[3][1])
    atoms[j].virtualz=atoms[j].z+dt/6*(kv[0][2]+2*kv[1][2]+2*kv[2][2]+kv[3][2])
    
    
    

numberofcharges=6
atoms=[]
for i in range(numberofcharges):
    atoms.append(atom())

##############proton#####################
atoms[0].x=0
atoms[0].y=0
atoms[0].z=0
atoms[0].vx=1*10**(-5)*2
atoms[0].vy=0
atoms[0].vz=0
atoms[0].ax=0
atoms[0].ay=0
atoms[0].az=0
atoms[0].mass= 2*1.6726231*10**(-27)
atoms[0].charge=2*1.602*10**(-19)
atoms[0].index=0
atoms[0].radius=2
##########################################
##############elettron#####################
atoms[1].x=5.29*10**(-11)
atoms[1].y=0
atoms[1].z=0
atoms[1].vx=1*10**(-5)*2
atoms[1].vy=9.084326066600729e-05
atoms[1].vz=0
atoms[1].ax=0
atoms[1].ay=0
atoms[1].az=0
atoms[1].mass= 9.109*10**(-31) 
atoms[1].charge=-1.602*10**(-19)
atoms[1].index=1
atoms[1].radius=1

##########################################

##############proton#####################
atoms[2].x=10*10**(-10)*0.25
atoms[2].y=0
atoms[2].z=0
atoms[2].vx=-1*10**(-5)*2
atoms[2].vy=0
atoms[2].vz=0
atoms[2].ax=0
atoms[2].ay=0
atoms[2].az=0
atoms[2].mass= 2*1.6726231*10**(-27)
atoms[2].charge=2*1.602*10**(-19)
atoms[2].index=2
atoms[2].radius=2
##########################################
##############elettron#####################
atoms[3].x=-5.29*10**(-11)+10*10**(-10)*0.25
atoms[3].y=0
atoms[3].z=0
atoms[3].vx=-1*10**(-5)*2
atoms[3].vy=-9.084326066600729e-05
atoms[3].vz=0
atoms[3].ax=0
atoms[3].ay=0
atoms[3].az=0
atoms[3].mass= 9.109*10**(-31) 
atoms[3].charge=-1.602*10**(-19)
atoms[3].index=3
atoms[3].radius=1
##########################################
##############elettron#####################

atoms[4].x=-5.29*10**(-11)*1
atoms[4].y=0
atoms[4].z=0
atoms[4].vx=1*10**(-5)*2
atoms[4].vy=-9.084326066600729e-05
atoms[4].vz=0
atoms[4].ax=0
atoms[4].ay=0
atoms[4].az=0
atoms[4].mass= 9.109*10**(-31) 
atoms[4].charge=-1.602*10**(-19)
atoms[4].index=4
atoms[4].radius=1

##########################################
##############elettron#####################
atoms[5].x=+5.29*10**(-11)*1+10*10**(-10)*0.25
atoms[5].y=0
atoms[5].z=0
atoms[5].vx=-1*10**(-5)*2
atoms[5].vy=9.084326066600729e-05
atoms[5].vz=0
atoms[5].ax=0
atoms[5].ay=0
atoms[5].az=0
atoms[5].mass= 9.109*10**(-31) 
atoms[5].charge=-1.602*10**(-19)
atoms[5].index=5
atoms[5].radius=1

##########################################
niterations=40000
dt=10**(-9)*1
f1=open("datamotio.txt","w")
string=""
for i in range(niterations):
    for j in range(numberofcharges):
        rk4(j,dt,numberofcharges)
        #eulero(j,dt,numberofcharges)
    for j in range(numberofcharges):
        atoms[j].x=atoms[j].virtualx
        atoms[j].y=atoms[j].virtualy
        atoms[j].z=atoms[j].virtualz
        atoms[j].vx=atoms[j].virtualvx
        atoms[j].vy=atoms[j].virtualvy
        atoms[j].vz=atoms[j].virtualvz
        string=str(atoms[j].radius)+str(';')+str(atoms[j].x)+str(";")+str(atoms[j].y)+str(";")+str(atoms[j].z)+str(";")+str(atoms[j].vx)+str(";")+str(atoms[j].vy)+str(";")+str(atoms[j].vz)+str(";") 
        f1.write(string+str('\n'))
f1.close()        
        
#for el in atoms:
#    print (el.acceleration)
        
        
        
        
