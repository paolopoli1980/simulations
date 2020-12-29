from __future__ import division
from vpython import *
import matplotlib.pyplot as plt
import math

scene2 = canvas(title='Rotating rail',
     x=0, y=0, width=1600, height=600,
     center=vector(5,0,0), background=vector(1,1,1))
f1=open("numtrack.txt","w")
f2=open("numspeed.txt","w")
f3=open("analtrack.txt","w")
f4=open("analspeed.txt","w")

class rail:
    def __init__(self):
        self.x=0
        self.y=0
        self.w=0
        self.r=0
        self.Rx=0
        self.Ry=0
        self.v=0
        
class body:
    def __init__(self):
        self.mass=0
        self.x=0
        self.y=0
        self.v_t=0
        self.r=0
     

r=rail()
m1=body()
tmax=6
t=0
ts=0
dt=0.005
R=20
r.w=1
r.r=R
m1.r=R/4
alfainmem=0
tR=0
rod = cylinder(pos=vector(0,0,0),axis=vector(R,0,0),radius=.5,color=color.blue)
body = ring(pos=vector(R/2,0,0), axis=vector(1,0,0), radius=.5, thickness=0.1,color=color.red)
listanalpointsx=[]
listanalpointsy=[]
listnumpointsx=[]
listnumpointsy=[]
listtimepoints=[]
listvelnumpoints=[]
listvelanalpoints=[]
while t<tmax:
    rate(60)
    t+=dt
    if m1.r<=r.r:
        m1.v_t+=r.w**2*m1.r*dt
        tR=t
    m1.r+=m1.v_t*dt
    
    r.Rx=r.r*math.cos(r.w*t)
    r.Ry=r.r*math.sin(r.w*t)
    rod.axis=vector(r.Rx,r.Ry,0)

    if m1.r<=r.r:
        m1.Rx=m1.r*math.cos(r.w*t)
        m1.Ry=m1.r*math.sin(r.w*t)    
        alfainmem=r.w*t
        body.axis=vector(math.cos(r.w*t),math.sin(r.w*t),0)
        analx=((R/8)*math.exp(r.w*t)+(R/8)*math.exp(-r.w*t))*math.cos(r.w*t)
        analy=((R/8)*math.exp(r.w*t)+(R/8)*math.exp(-r.w*t))*math.sin(r.w*t)
        analvx=((R/8)*r.w*math.exp(r.w*t)-(R/8)*r.w*math.exp(-r.w*t))*math.cos(r.w*t)-((R/8)*math.exp(r.w*t)+(R/8)*math.exp(-r.w*t))*r.w*math.sin(r.w*t)
        analvy=((R/8)*r.w*math.exp(r.w*t)-(R/8)*r.w*math.exp(-r.w*t))*math.sin(r.w*t)+((R/8)*math.exp(r.w*t)+(R/8)*math.exp(-r.w*t))*r.w*math.cos(r.w*t)
        analxR=analx
        analyR=analy
        vnum=math.sqrt(m1.v_t**2+(r.w*m1.r)**2)

    if m1.r>r.r:
        ts+=dt
        m1.Rx=m1.r*math.cos(alfainmem)-R*math.sin(alfainmem)*r.w*ts
        m1.Ry=m1.r*math.sin(alfainmem)+R*math.cos(alfainmem)*r.w*ts    
        body.axis=vector(math.cos(alfainmem),math.sin(alfainmem),0)
        analx=(-(R/8)*r.w*math.exp(-r.w*tR)+(R/8)*r.w*math.exp(r.w*tR))*math.cos(r.w*tR)*ts-r.w*R*math.sin(r.w*tR)*ts+analxR
        analy=(-(R/8)*r.w*math.exp(-r.w*tR)+(R/8)*r.w*math.exp(r.w*tR))*math.sin(r.w*tR)*ts+r.w*R*math.cos(r.w*tR)*ts+analyR
        analvx=(-(R/8)*r.w*math.exp(-r.w*tR)+(R/8)*r.w*math.exp(r.w*tR))*math.cos(r.w*tR)-r.w*R*math.sin(r.w*tR)
        analvy=(-(R/8)*r.w*math.exp(-r.w*tR)+(R/8)*r.w*math.exp(r.w*tR))*math.sin(r.w*tR)+r.w*R*math.cos(r.w*tR)
        vnum=math.sqrt(m1.v_t**2+(r.w*R)**2)
    body.pos=vector(m1.Rx,m1.Ry,0)

    analv=math.sqrt(analvx**2+analvy**2)
    
    
    listnumpointsx.append(m1.Rx)
    listnumpointsy.append(m1.Ry)
    listanalpointsx.append(analx)
    listanalpointsy.append(analy)
    listtimepoints.append(t)
    listvelnumpoints.append(vnum)
    listvelanalpoints.append(analv)
    
    f1.write(str(m1.Rx)+"       "+str(m1.Ry)+"\n")
    f2.write(str(t)+"        "+str(vnum)+"\n")
    f3.write(str(analx)+"      "+str(analy)+"\n")
    f4.write(str(t)+"       "+str(analv)+"\n")
plt.plot(listnumpointsx,listnumpointsy)
plt.plot(listanalpointsx,listanalpointsy)
plt.show()
plt.plot(listtimepoints,listvelnumpoints)
plt.plot(listtimepoints,listvelanalpoints)

plt.show()
f1.close()
f1.close()
f3.close()
f4.close()
    


