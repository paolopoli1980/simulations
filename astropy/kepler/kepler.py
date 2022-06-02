import numpy as np
import matplotlib.pyplot as plt
import math
fig, (ax1, ax2, ax3) = plt.subplots(3)
ax1.set_title('Kepler Orbits')
ax2.set_title('Gravitational Potential Energy')
ax3.set_title('Gravitational Total Energy')
ax3.set_xlabel('Teta')
ax3.set_ylabel('E')



for i in range(30): 
    G=1
    M=400+20*(i+1)
    w=1
    m=1
    r=10
    vr=0
    l=m*r**2*w
    c=l/m
    k=G*M
    E=m/2*(vr**2+r**2*w**2)-k*m/r
    Ex=E/m
    q=math.sqrt(2*Ex/c**2+k**2/c**4)
    #teta=90*math.pi/180
    teta=0
    r=(c**2/k)/(1+c**2*q*math.cos(teta)/k)
    x=[]
    y=[]
    energylist=[]
    rlist=[]
    totenergy=[]
    tetalist=[]
    print (r)
    limit=40.0

    while teta<math.pi*2*1:
        start=True
        teta+=0.01

        r=(c**2/k)/(1+c**2*q*math.cos(teta)/k)
        

        
        if E>=0:
            if (math.fabs(r*math.cos(teta))<limit) and start==True:
                x.append(r*math.cos(teta))
                y.append(r*math.sin(teta))
                rlist.append(r)
                tetalist.append(teta)
                energylist.append(-k/r)
                totenergy.append(E)
        else:
            x.append(r*math.cos(teta))
            y.append(r*math.sin(teta))
            rlist.append(r)
            tetalist.append(teta)
            energylist.append(-k/r)       
            totenergy.append(E)
        
    ax1.plot(x, y,'.')
    ax2.plot(rlist,energylist)
    ax3.plot(tetalist,totenergy)
    
    #plt.scatter(x,y,5)

    
plt.show()    
print (E)    
