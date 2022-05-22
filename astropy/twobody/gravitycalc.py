##############################################################################################
##########A simple newtonian gravitational model on bodies ####################################
##############################################################################################
##############################################################################################

#import numpy as np
import math
class body:
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
        self.index=0
        self.G=6.67408*10**(-11)
        self.force=0
        self.acceleration=0
        self.radius=0

    def bodies_forces(self,numberofmasses,bodies):
        self.ax=0	
        self.ay=0
        self.az=0
        for i in range(numberofmasses):
            if i!=self.index:
                #print (i,self.index)
                r=math.sqrt((self.x-bodies[i].x)**2+(self.y-bodies[i].y)**2+(self.z-bodies[i].z)**2)
                self.force=self.mass*bodies[i].mass*self.G/r**2
                self.acceleration=self.force/self.mass
                ux=(bodies[i].x-self.x)/r
                uy=(bodies[i].y-self.y)/r
                uz=(bodies[i].z-self.z)/r
                self.ax+=self.acceleration*ux
                self.ay+=self.acceleration*uy
                self.az+=self.acceleration*uz
        return [self.ax,self.ay,self.az]                             

def eulero(j,dt,numberofmasses,bodies):
    bodies[j].virtualx=bodies[j].x+bodies[j].vx*dt
    bodies[j].virtualy=bodies[j].y+bodies[j].vy*dt
    bodies[j].virtualz=bodies[j].z+bodies[j].vz*dt

    bodies[j].virtualvx=bodies[j].vx+bodies[j].bodies_forces(numberofmasses,bodies)[0]*dt
    bodies[j].virtualvy=bodies[j].vy+bodies[j].bodies_forces(numberofmasses,bodies)[1]*dt
    bodies[j].virtualvz=bodies[j].vz+bodies[j].bodies_forces(numberofmasses,bodies)[2]*dt
    
    
    
def rk4(j,dt,numberofmasses,bodies):
   # print (bodies[j].bodies_forces(numberofmasses))
    kv=[[bodies[j].vx,bodies[j].vy,bodies[j].vz],[0,0,0],[0,0,0],[0,0,0]]
    kx=[[bodies[j].x,bodies[j].y,bodies[j].z],[0,0,0],[0,0,0],[0,0,0]]
    ka=[[bodies[j].bodies_forces(numberofmasses,bodies)[0],bodies[j].bodies_forces(numberofmasses,bodies)[1],bodies[j].bodies_forces(numberofmasses,bodies)[2]],[0,0,0],[0,0,0],[0,0,0]]
    
    kx[1][0]=bodies[j].x+bodies[j].vx*dt/2
    kx[1][1]=bodies[j].y+bodies[j].vy*dt/2
    kx[1][2]=bodies[j].z+bodies[j].vz*dt/2
    bodies[j].x=kx[1][0]
    bodies[j].y=kx[1][1]
    bodies[j].z=kx[1][2]
    
    ka[1][0]=bodies[j].bodies_forces(numberofmasses,bodies)[0]
    ka[1][1]=bodies[j].bodies_forces(numberofmasses,bodies)[1]
    ka[1][2]=bodies[j].bodies_forces(numberofmasses,bodies)[2]

    bodies[j].x=kx[0][0]
    bodies[j].y=kx[0][1]
    bodies[j].z=kx[0][2]
    
    kv[1][0]=bodies[j].vx+ka[0][0]*dt/2
    kv[1][1]=bodies[j].vy+ka[0][1]*dt/2
    kv[1][2]=bodies[j].vz+ka[0][2]*dt/2
    
    kx[2][0]=kx[0][0]+kv[1][0]*dt/2
    kx[2][1]=kx[0][1]+kv[1][1]*dt/2
    kx[2][2]=kx[0][2]+kv[1][2]*dt/2

    bodies[j].x=kx[2][0]
    bodies[j].y=kx[2][1]
    bodies[j].z=kx[2][2]

    ka[2][0]=bodies[j].bodies_forces(numberofmasses,bodies)[0]
    ka[2][1]=bodies[j].bodies_forces(numberofmasses,bodies)[1]
    ka[2][2]=bodies[j].bodies_forces(numberofmasses,bodies)[2]

    bodies[j].x=kx[0][0]
    bodies[j].y=kx[0][1]
    bodies[j].z=kx[0][2]

    kv[2][0]=bodies[j].vx+ka[1][0]*dt/2
    kv[2][1]=bodies[j].vy+ka[1][1]*dt/2
    kv[2][2]=bodies[j].vz+ka[1][2]*dt/2
    
    kx[3][0]=kx[0][0]+kv[2][0]*dt
    kx[3][1]=kx[0][1]+kv[2][1]*dt
    kx[3][2]=kx[0][2]+kv[2][2]*dt

    bodies[j].x=kx[3][0]
    bodies[j].y=kx[3][1]
    bodies[j].z=kx[3][2]
    
    ka[3][0]=bodies[j].bodies_forces(numberofmasses,bodies)[0]
    ka[3][1]=bodies[j].bodies_forces(numberofmasses,bodies)[1]
    ka[3][2]=bodies[j].bodies_forces(numberofmasses,bodies)[2]
   
    kv[3][0]=bodies[j].vx+ka[2][0]*dt
    kv[3][1]=bodies[j].vy+ka[2][1]*dt
    kv[3][2]=bodies[j].vz+ka[2][2]*dt

    bodies[j].x=kx[0][0]
    bodies[j].y=kx[0][1]
    bodies[j].z=kx[0][2]
	

    bodies[j].virtualvx=bodies[j].vx+dt/6*(ka[0][0]+2*ka[1][0]+2*ka[2][0]+ka[3][0])
    bodies[j].virtualvy=bodies[j].vy+dt/6*(ka[0][1]+2*ka[1][1]+2*ka[2][1]+ka[3][1])
    bodies[j].virtualvz=bodies[j].vz+dt/6*(ka[0][2]+2*ka[1][2]+2*ka[2][2]+ka[3][2])
    
    bodies[j].virtualx=bodies[j].x+dt/6*(kv[0][0]+2*kv[1][0]+2*kv[2][0]+kv[3][0])
    bodies[j].virtualy=bodies[j].y+dt/6*(kv[0][1]+2*kv[1][1]+2*kv[2][1]+kv[3][1])
    bodies[j].virtualz=bodies[j].z+dt/6*(kv[0][2]+2*kv[1][2]+2*kv[2][2]+kv[3][2])
    
    
    


        
        
        
        
