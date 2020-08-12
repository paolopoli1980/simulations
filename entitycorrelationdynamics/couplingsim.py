import numpy as np
import matplotlib.pyplot as plt

def euler_resolution(maxt,dt,c,gamma21,gamma31,gamma32,omega21,omega31,omega32,omegapot,e3,e2,e1):
    t=0

    #print (V,c)

    while t<maxt:
       # v12=gamma21*np.exp(-1j*omega21*t)*np.exp(1j*omegapot*t)
       # v21=gamma21*np.exp(1j*omega21*t)*np.exp(-1j*omegapot*t)
       # v13=gamma31*np.exp(-1j*omega31*t)*np.exp(1j*omegapot*t)
       # v31=gamma31*np.exp(1j*omega31*t)*np.exp(-1j*omegapot*t)
       # v23=gamma32*np.exp(-1j*omega32*t)*np.exp(1j*omegapot*t)
       # v32=gamma32*np.exp(1j*omega32*t)*np.exp(-1j*omegapot*t)
       # v12=gamma21*np.exp(-1j*omega21*t)*np.exp(1j*omegapot*t)
        v12=gamma21*np.exp(-1j*omega21*t)*np.cos(omegapot*t)
        v21=gamma21*np.exp(1j*omega21*t)*np.cos(omegapot*t)
        v13=gamma31*np.exp(-1j*omega31*t)*np.cos(omegapot*t)
        v31=gamma31*np.exp(1j*omega31*t)*np.cos(omegapot*t)
        v23=gamma32*np.exp(-1j*omega32*t)*np.cos(omegapot*t)
        v32=gamma32*np.exp(1j*omega32*t)*np.cos(omegapot*t)

        V=np.array([[2,v12,0,0,0],[v21,1,v31,0,0],[0,v31,0,v31,0],[0,0,v31,-1,v12],[0,0,0,v12,-2]])
       # V=np.array([[0,0,v13],[0,0,0],[v31,0,0]])
        #V=np.array([[0,v12],[v21,0]])

        dc=np.matmul(V,c)*dt/((0+1j)*hbar)
        c=c+dc
       # print (c)
        y=c*np.conjugate(c)
        t+=dt
        listvalues.append(y)
        tvalues.append(t)

listvalues=[]        
gamma21=1.0*0
gamma31=np.sqrt(3/2)*0
gamma32=1.0*0
hbar=1
e3=2
e2=1
e1=0
omega21=(e2-e1)/hbar*0
omega31=(e3-e1)/hbar*0
omega32=(e3-e2)/hbar*0

omegapot=omega31
c=np.array([1,0,0,0,0])
dt=0.0001
maxt=20
tvalues=[]
print (listvalues)
euler_resolution(maxt,dt,c,gamma21,gamma31,gamma32,omega21,omega31,omega32,omegapot,e3,e2,e1)
plt.plot(tvalues,listvalues)
plt.show()

