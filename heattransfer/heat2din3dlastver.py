import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from pylab import *

dimx=50
dimy=50
temp=np.zeros((3,dimy,dimx))
#xspace=np.zeros(dimx)
#yspace=np.zeros(dimy)
temp[1]=100.0
'''
for i in range(365):
    for j in range(9):
        x=20+j*np.cos(i*np.pi/180.0)
        y=20+j*np.sin(i*np.pi/180)
    
        temp[1][int(x)][int(y)]=120.0
'''    
for i in range(15,35):
    for j in range(15,35):
        temp[1][i][j]=120.0

for i in range(15,20):
    for j in range(5,15):
        temp[1][i][j]=120.0

for i in range(30,35):
    for j in range(5,15):
        temp[1][i][j]=120.0

temp[1][0]=22.0
temp[1][dimy-1]=22.0
for i in range(dimy):
    temp[1][i][0]=22.0
    temp[1][i][dimx-1]=22.0
memtemp=np.zeros((4,dimy,dimx))
temp[0]=22.0
temp[2]=22.0
print (temp)
tempbackup=temp.copy()
nsteps=4

graph3d=True
alfa=0.1
psideupdw=0.1
psidedxsx=0.1
pup=0.1
paramsideupdw=0
paramsidedxsx=0
paramup=pup

dt=0.01
dx=dy=dz=0.1
maxtempgraf=120
dtmaxratio=1.15
isolated3d=True
contmem=0
for k in range(nsteps):
    for j in range(1,dimy-1):
        for i in range(1,dimx-1):
            
            if j-1==0 or j+1==dimy-1:
                
                paramsideupdw=psideupdw
            else:
                paramsideupdw=1

            if i-1==0 or i+1==dimx-1:
                parmsidedxsx=psidedxsx
            else:
                paramsidedxsx=1

            if isolated3d!=True:

			
                dtemp=(alfa*(temp[1][j][i-1]+temp[1][j][i+1]-2*temp[1][j][i])*paramsidedxsx/dx**2+alfa*(temp[1][j-1][i]+temp[1][j+1][i]-2*temp[1][j][i])*paramsideupdw/dy**2+alfa*(temp[0][j][i]+temp[2][j][i]-2*temp[1][j][i])*paramup/dz**2)*dt
            if isolated3d==True:
                dtemp=(alfa*(temp[1][j][i-1]+temp[1][j][i+1]-2*temp[1][j][i])*paramsidedxsx/dx**2+alfa*(temp[1][j-1][i]+temp[1][j+1][i]-2*temp[1][j][i])*paramsideupdw/dy**2)*dt

            tempbackup[1][j][i]+=dtemp

            
    temp=tempbackup.copy()
    if k+1==nsteps/4 or k+1==nsteps/2 or k+1==3*nsteps/4 or k+1==nsteps:
        memtemp[contmem]=temp[1].copy()
        contmem+=1
        print (contmem)
        
for j in range(dimy):
    for i in range(dimx):
        if temp[1][j][i]>maxtempgraf/dtmaxratio:
            plot(i*dx,j*dy,'y.')
           # ax.scatter(j*0.1, i*0.1, temp[1][j][i], c='r', marker='o') 
        if temp[1][j][i]<maxtempgraf/dtmaxratio:
            plot(i*dx,j*dy,'r.')
           # ax.scatter(j*0.1, i*0.1, temp[1][j][i], c='r', marker='o') 

        if temp[1][j][i]<0.75*maxtempgraf/dtmaxratio:
            plot(i*dx,j*dy,'g.')
           # ax.scatter(j*0.1, i*0.1, temp[1][j][i], c='r', marker='o') 

        if temp[1][j][i]<0.5*maxtempgraf/dtmaxratio:
            plot(i*dx,j*dy,'b.')
            #ax.scatter(j*0.1, i*0.1, temp[1][j][i], c='r', marker='o') 
        
        
grid(True)
show()

if graph3d==True:
    for k in range(contmem):
        fig = plt.subplot(1+k,1,1)
        ax = plt.axes(projection='3d')
        ax.set_zlabel('T')
        for j in range(dimy):
            for i in range(dimx):
                if memtemp[k][j][i]>maxtempgraf/dtmaxratio:
                    
                    ax.scatter(j*0.1, i*0.1, memtemp[k][j][i], c='y', marker='o') 
                if memtemp[k][j][i]<maxtempgraf/dtmaxratio:
                    
                    ax.scatter(j*0.1, i*0.1, memtemp[k][j][i], c='r', marker='o') 

                if memtemp[k][j][i]<0.75*maxtempgraf/dtmaxratio:
                    
                    ax.scatter(j*0.1, i*0.1, memtemp[k][j][i], c='g', marker='o') 

                if memtemp[k][j][i]<0.5*maxtempgraf/dtmaxratio:
                    
                    ax.scatter(j*0.1, i*0.1, memtemp[k][j][i], c='b', marker='o') 
        plt.show()

print (temp)

