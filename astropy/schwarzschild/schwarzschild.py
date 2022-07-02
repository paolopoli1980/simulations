import numpy as np
import matplotlib.pyplot as plt
import math

m=[1*1.989*10**30,2*1.989*10**30]
g=6.67*10**(-11)
c=3*10**(8)

#r.append(696340)
fig, (ax1) = plt.subplots(1)

gamma=1
gammaorbit=1

color=['blue','red','green','orange']
listlegend=['rest','circular orbit']
cont=-1
ax1.set_ylabel('Time')
ax1.set_xlabel('r')
for elem in m:
    listr=[]
    listgamma=[]
    listnewtongravity=[]
    cont+=1
    rs=2*g*elem/c**2
    r=[rs*i*0.1 for i in range(200)]
    for el in r:
        if el>=rs:
            gamma=np.sqrt(1-2*g*elem/(el*c**2))
            print (el,gamma)
            listr.append(el)
            listgamma.append(gamma)
    ax1.plot(listr,listgamma, linewidth=2.0, color=color[cont],label=listlegend[0])
    listr=[]
    listgamma=[]
    cont+=1
    print('********************************************************')
    for el in r:
        if el>=1.5*rs:
            gammaorbit=np.sqrt(1-1.5*rs/el)
            listr.append(el)
            listgamma.append(gammaorbit)
            print (el,gammaorbit)

    ax1.plot(listr,listgamma, linewidth=2.0, color=color[cont],label=listlegend[1])
    listr=[]
    listnewtongravity=[]
'''
    for el in r:
        if el>0:
            newtongravity=g*elem/el**2
            listnewtongravity.append(newtongravity)
            listr.append(el)
    ax2.plot(listr,listnewtongravity,linewidth=2.0, color=color[cont])
'''

legend = ax1.legend(loc='upper right', shadow=True, fontsize='x-large')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('C0')

#plt.axvline(x=1, ymin=0.01, ymax=1)
plt.show()
