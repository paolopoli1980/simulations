import numpy as np
import matplotlib.pyplot as plt
import math

latitudinecity = {
  "Rome": 41.8933203,
  "Cairo":31.2357257,
  "Kinshasa":-4.3217055,
  "Helsinki":60.16749,
  "Hammerfest":70.65,
  "Zero":90.0
}

namecity=["Rome","Cairo","Kinshasa","Helsinki","Hammerfest","Zero"]
fig, (ax1, ax2, ax3,ax4,ax5,ax6) = plt.subplots(6)
#ax1.set_title('Kepler Orbits')
#ax2.set_title('Gravitational Potential Energy')
#ax3.set_title('Gravitational Total Energy')
#ax4.set_title('Teta')
#ax5.set_title('E')
ax6.set_xlabel('Hour')
ax6.set_ylabel('Flux')
for i in range(len(namecity)):
    ws=7.164*10**(-4)
    wt=0.2616666
    a=0.999995
    b=0.999835
    xf=-0.016705
    Au=149597870.7
    #xf=0
    t=0
    latitudine=latitudinecity[namecity[i]]
    alfa=-math.pi*(latitudine-90)/180
    omega=23.5*math.pi/180*1
    betazero=0
    teta=0
    philist=[]
    tlist=[]
    while t<365*24*1: 
        t+=0.05
        beta=wt*t+betazero
        phi=(-a*math.cos(ws*t+teta)+xf)*(math.cos(beta)*math.sin(alfa)*math.cos(omega)-math.cos(alfa)*math.sin(omega))
        phi=phi-b*math.sin(ws*t+teta)*math.sin(beta)*math.sin(alfa)
        phi=phi/math.sqrt((-a*math.cos(ws*t+teta)+xf)**2+b**2*math.sin(ws*t+teta)**2)
        angle1=math.atan(6400/(Au*math.sqrt((-a*math.cos(ws*t+teta)+xf)**2+b**2*math.sin(ws*t+teta)**2)))
        angle2=math.atan(6400/(0.98328*Au))
        phi=phi*(angle1/angle2)**2
        
        if phi<0:
            phi=0
            
        
        philist.append(phi)
        tlist.append(t)
    
    if i==0:
        ax1.plot(tlist, philist, linewidth=2.0, color='blue')
    if i==1:
        ax2.plot(tlist, philist, linewidth=2.0,color='red')
    if i==2:
        ax3.plot(tlist, philist, linewidth=2.0, color='yellow')
    if i==3:
        ax4.plot(tlist, philist, linewidth=2.0,color='green')

    if i==4:
        ax5.plot(tlist, philist, linewidth=2.0,color='purple')
    if i==5:
        ax6.plot(tlist, philist, linewidth=2.0,color='cyan')

plt.show()
                            
