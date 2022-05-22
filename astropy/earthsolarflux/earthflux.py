import numpy as np
import matplotlib.pyplot as plt
import math

latitudinecity = {
  "Rome": 41.8933203,
  "Cairo":31.2357257,
  "Kinshasa":-4.3217055,
  "Helsinki":60.16749,
  "Zero":0
}

ws=7.164*10**(-4)
wt=0.2616666
a=0.999995
b=0.999835
xf=-0.016705
#xf=0
t=0
latitudine=latitudinecity["Zero"]
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
    phi=phi/((-a*math.cos(ws*t+teta)+xf)**2+b**2*math.sin(ws*t+teta)**2)
    if phi<0:
        phi=0
        
    
    philist.append(phi)
    tlist.append(t)
fig, ax = plt.subplots()

ax.plot(tlist, philist, linewidth=2.0)


   

plt.show()
                            
