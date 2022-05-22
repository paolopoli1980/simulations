import numpy as np
import matplotlib.pyplot as plt
import math

G=1
M=260
w=1
m=10
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
print (r)
while teta<2*math.pi:
    teta+=0.01

    
    r=(c**2/k)/(1+c**2*q*math.cos(teta)/k)
    #if math.fabs(r*math.cos(teta))<20:
    x.append(r*math.cos(teta))
    y.append(r*math.sin(teta))
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)


   

plt.show()    
print (E)    
