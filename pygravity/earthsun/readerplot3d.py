#from mpl.toolkits import mplot3d

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from matplotlib import cm
f1=open('datamotio.txt','r')
f2=open('energy.txt','r')
string='***'
nbody=2
npoints=3000
x=[[0 for i in range(nbody)] for j in range(npoints)]
y=[[0 for i in range(nbody)] for j in range(npoints)]
z=[[0 for i in range(nbody)] for j in range(npoints)]
print (x)
fig = plt.figure()
energy=[]

ax = plt.axes(projection='3d')
while len(string)>1:
    #print (string)
    

    for i in range(nbody):
        try:
            string=f1.readline()
            lista=string.split(';')
            #print (lista)
            x[i].append(float(lista[1]))
            y[i].append(float(lista[2]))
            z[i].append(float(lista[3]))

        except:
             break
string='***'            
while len(string)>1:
    #print (string)
    

    for i in range(nbody):
        try:
            string=f2.readline()
            
            #print (lista)        
            
            energy.append(float(string))

        except:
             break            
#ax.scatter3D(x2, y2, z2, c=z2, cmap='Greens');   
#plt.plot(x1,y1,'r--',x2,y2,'bs')  
# Data for a three-dimensional line



# Data for three-dimensional scattered points
for i in range(nbody):
    #my_col = cm.jet(np.random.rand(0,1))
    if i%4==0:
        ax.scatter(x[i], y[i], z[i], c='r', marker='o') 
    if i%4==1:
        ax.scatter(x[i], y[i], z[i], c='b', marker='^') 
    if i%4==2:
        ax.scatter(x[i], y[i], z[i], c='g', marker='*') 
    if i%4==3:
        ax.scatter(x[i], y[i], z[i], c='y', marker='o') 

    #ax.scatter3D(x[i], y[i], z[i], c=z[i], cmap=2);  

#plt.plot(x[1],y[1])
plt.show()
plt.plot(energy)
plt.show()
f1.close()
f2.close()
