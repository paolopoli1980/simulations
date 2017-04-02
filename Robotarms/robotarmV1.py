
from visual import *
import numpy as np
import time
class robot:

    def __init__(self):
        self.index=0
        self.length=0
        self.x=0
        self.y=0
        self.z=0
        self.angle1=0
        self.angle2=0
        self.totangle1=0
        self.totangle2=0
        self.ux=self.length
        self.uy=0
        self.uz=0
        self.radius=0

    def rot_vector(self,ux,uy,uz,key):
        if key=='left' or key=='right':
            uxold=ux
            uyold=uy
            ux=uxold*np.cos(self.angle1)-uyold*np.sin(self.angle1)
            uy=uxold*np.sin(self.angle1)+uyold*np.cos(self.angle1)
        if key=='up' or key=='down':
            uxold=ux
            uzold=uz
            ux=uxold*np.cos(self.angle2)+uzold*np.sin(self.angle2)
            uz=-uxold*np.sin(self.angle2)+uzold*np.cos(self.angle2)
                    
        return ux,uy,uz

    def movement(self,n,key,dyn):
        vecdistx=np.zeros((narms-n))
        vecdisty=np.zeros((narms-n))
        vecdistz=np.zeros((narms-n))

        vecdistx[0]=arms[n].ux
        vecdisty[0]=arms[n].uy
        vecdistz[0]=arms[n].uz
        pointer=[]
        for i in range(1,narms-n):
            vecdistx[i]=vecdistx[i-1]+arms[i+n].ux
            vecdisty[i]=vecdisty[i-1]+arms[i+n].uy
            vecdistz[i]=vecdistz[i-1]+arms[i+n].uz
        for i in range(0,narms-n):
            vecoldx=vecdistx[i]
            vecoldy=vecdisty[i]
            vecoldz=vecdistz[i]
            vecdistx[i]=self.rot_vector(vecoldx,vecoldy,vecoldz,key)[0]
            vecdisty[i]=self.rot_vector(vecoldx,vecoldy,vecoldz,key)[1]
            vecdistz[i]=self.rot_vector(vecoldx,vecoldy,vecoldz,key)[2]

        sx=0
        sy=0
        sz=0
        for i in range (n):
            sx=arms[i].ux+sx
            sy=arms[i].uy+sy
            sz=arms[i].uz+sz

            
        for i in range(0,narms-n):
            if i>0:
                arms[n+i].ux=vecdistx[i]-vecdistx[i-1]
                arms[n+i].uy=vecdisty[i]-vecdisty[i-1]
                arms[n+i].uz=vecdistz[i]-vecdistz[i-1]
                arms[n+i].x=vecdistx[i-1]+sx
                arms[n+i].y=vecdisty[i-1]+sy
                arms[n+i].z=vecdistz[i-1]+sz

            else:
                arms[n+i].ux=vecdistx[i]
                arms[n+i].uy=vecdisty[i]
                arms[n+i].uz=vecdistz[i]
                
        l=0 
        for i in range(narms):
            l=np.sqrt(arms[i].ux**2+arms[i].uy**2+arms[i].uz**2)
            arms[i].ux=arms[i].ux*arms[i].length/l
            arms[i].uy=arms[i].uy*arms[i].length/l
            arms[i].uz=arms[i].uz*arms[i].length/l

        if dyn==1:    
            for i in range(narms):
                cyl[i].pos.x=arms[i].x
                cyl[i].pos.y=arms[i].y
                cyl[i].pos.z=arms[i].z
    
                cyl[i].axis.x=arms[i].ux
                cyl[i].axis.y=arms[i].uy
                cyl[i].axis.z=arms[i].uz

        
def build_arms():
    i=0
    
    for el in arms:
        
        el.length=6
        el.x=el.length*i
        el.ux=el.length
        i+=1
    i=0 
    for j in range(narms):
        arms[j].radius=1-0.05*j
    for el in arms:
        i+=1
        cyl.append(cylinder(pos=(el.x,el.y,el.z),axis=(el.ux,el.uy,el.uz),radius=el.radius))
            

        

        
def pseudo_inv(arms,narms,x,y,z,dyn,v):
         
    global xf,yf,zf
    matjac=np.zeros((3,2*narms))
    k=-1
    for j in range(narms):
        k+=1
        arms[j].angle1=0.005
        arms[j].angle2=0.005
        dx=0
        dy=0
        dz=0
        uxxold=arms[j].ux
        uyyold=arms[j].uy
        uzzold=arms[j].uz
        for t in range(narms):
 
            dx=dx+arms[t].ux
            dy=dy+arms[t].uy
            dz=dz+arms[t].uz
 
        key='left'
        arms[j].movement(j,key,dyn)
        dx2=0
        dy2=0
        dz2=0
        dxtot=0
        dytot=0
        dztot=0
        for t in range(narms):
            dx2=dx2+arms[t].ux
            dy2=dy2+arms[t].uy
            dz2=dz2+arms[t].uz
        dxtot=(dx2-dx)/arms[j].angle1
        dytot=(dy2-dy)/arms[j].angle1
        dztot=(dz2-dz)/arms[j].angle1
        matjac[0][k]=dxtot
        matjac[1][k]=dytot
        matjac[2][k]=dztot                
        arms[j].ux=uxxold
        arms[j].uy=uyyold
        arms[j].uz=uzzold

        key='up'
        k+=1
        arms[j].movement(j,key,dyn)
        dx2=0
        dy2=0
        dz2=0
        dxtot=0
        dytot=0
        dztot=0
        for t in range(narms):
            dx2=dx2+arms[t].ux
            dy2=dy2+arms[t].uy
            dz2=dz2+arms[t].uz
        dxtot=(dx2-dx)/arms[j].angle2
        dytot=(dy2-dy)/arms[j].angle2
        dztot=(dz2-dz)/arms[j].angle2
        matjac[0][k]=dxtot
        matjac[1][k]=dytot
        matjac[2][k]=dztot                
        arms[j].ux=uxxold
        arms[j].uy=uyyold
        arms[j].uz=uzzold
    mat=np.linalg.pinv(matjac)

    uxx=[]
    uyy=[]
    uzz=[]
    
    for j in range(narms):
            uxx.append(arms[j].ux)
            uyy.append(arms[j].uy)
            uzz.append(arms[j].uz)
   


    xf=0
    yf=0
    zf=0        
    xi=0
    yi=0
    zi=0
    
    
    for j in range(narms):
        xf=xf+arms[j].ux
        yf=yf+arms[j].uy
        zf=zf+arms[j].uz
#    v=np.zeros(3)
    Delta=np.zeros(2*narms)
    v[0]=(-xf+x)
    v[1]=(-yf+y)
    v[2]=(-zf+z)
    print mat
    print v
    print mat[1][2]
    for l in range(2*narms):
        for m in range(3):
            Delta[l]=Delta[l]+mat[l][m]*v[m]
    print "delta"
    print Delta
    k=-1
    dyn=1
    for j in range(narms):
        print j
        k+=1
        
        print Delta[k]
        Delta[k]=Delta[k]-int(Delta[k]/(2*np.pi))*2*np.pi
        alfa=0
        dyn=1
        while np.abs(alfa)<np.abs(Delta[k]):
            rate(800)
            key='left'
            if Delta[k]>=0:
                arms[j].angle1=0.005

                alfa+=arms[j].angle1
            else:
                arms[j].angle1=-0.005

                alfa+=arms[j].angle1
                
            
            arms[j].movement(j,key,dyn)
        alfa=0    
        k+=1
        
        Delta[k]=Delta[k]-int(Delta[k]/(2*np.pi))*2*np.pi

         
        while np.abs(alfa)<np.abs(Delta[k]):
            rate(800)
           
            key='up'

            if Delta[k]>=0:
                arms[j].angle2=0.005
                alfa+=arms[j].angle2
            else:
                arms[j].angle2=-0.005

                alfa+=arms[j].angle2

            
            arms[j].movement(j,key,dyn)
          
  
         
  
#**************main variables*******************
cyl=[]
narms=4
arms=[robot() for i in range(narms) ]
build_arms() 
n=0    
x=-12
y=8
z=-6
ball=(sphere(pos=(x,y,z),radius=0.5,color=color.green))
v=np.zeros(3)
global xf,yf,zf
#************************************************

dyn=1
toll=0.5
xf=10000
yf=10000
zf=10000    

while 1==1:
    v[0]=10000
    v[1]=10000
    v[2]=10000 
 
    key = scene.kb.getkey()
    if key=='c':
        dyn=1
        n=input("number arm:=")
        key=''
    if key=='left':
        dyn=1
        print "got it"
        arms[n].angle1=0.05
        arms[n].totangle1+=0.05
        arms[n].movement(n,key,dyn)
        key=''
        
    if key=='right':
        dyn=1
        print "got it"
        arms[n].angle1=-0.05
        arms[n].totangle1-=0.05
        arms[n].movement(n,key,dyn)
        key=''

    if key=='up':
        dyn=1
        print "got it"
        arms[n].angle2=0.05
        arms[n].totangle2+=0.05
        arms[n].movement(n,key,dyn)
        key=''
    if key=='down':
        dyn=1
        print "got it"
        arms[n].angle2=-0.05
        arms[n].totangle2-=0.05
        arms[n].movement(n,key,dyn)
        key=''
    if key=='1':
        dyn=0
        xf=10000
        yf=10000
        zf=10000
        print "got it"
        while np.abs(np.sqrt((xf-x)**2+(yf-y)**2+(zf-z)**2))>toll:
            pseudo_inv(arms,narms,x,y,z,dyn,v)
            print "dist"
            print xf,yf,zf
            print np.abs(np.sqrt((xf-x)**2+(yf-y)**2+(zf-z)**2))
        key=''    
    if key=='2':
        x=0
        y=0
        z=0
        lt=0
        alfa=0
        
        for i in range(10):
            lt=0
            for j in range(narms):
                lt=lt+arms[j].length
            lt-=1
            alfa+=i*2*np.pi/10.0
            x=lt*np.cos(alfa)
            y=lt*np.sin(alfa)       
            ball.pos.x=x
            ball.pos.y=y
            ball.pos.z=z
            dyn=0
            xf=10000
            yf=10000
            zf=10000
            print "got it"
            while np.abs(np.sqrt((xf-x)**2+(yf-y)**2+(zf-z)**2))>toll:
                pseudo_inv(arms,narms,x,y,z,dyn,v)
                print "dist"
                print xf,yf,zf
                print np.abs(np.sqrt((xf-x)**2+(yf-y)**2+(zf-z)**2))
        key=''            