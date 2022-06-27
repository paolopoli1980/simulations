import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title('mass');

g=[4.0,6.0,8.0,9.81]
r=[1400*10**3,2400*10**3,3400*10**3,4400*10**3,5400*10**3,6400*10**3]
ggrav=6.67*10**(-11)
points=[]
#fig = plt.figure(figsize = (10, 7))
#ax = plt.axes(projection ="3d")
x=[]
y=[]
z=[]

ax.scatter3D(x, y, z, color = "green")
print ('g   ,  r    ,    m')
for el in g:
    for elem in r:
        m=el*elem**2/ggrav
        ax.scatter(el,elem,m)
        print(el,elem,m)
        
        
plt.show()
