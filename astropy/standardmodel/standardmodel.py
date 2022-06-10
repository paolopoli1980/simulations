import numpy as np
import matplotlib.pyplot as plt
import math
delta=0.01
fig, (ax1) = plt.subplots(1)
q=0.98
t=0
ho=1/(13*10**(9))
delta=0.01
plus=0
nsteps=int(2/delta)+plus

q=[0.014,0.028,0.5,0.5,0.5,0.51]
color=['blue','red','yellow','green','pink','orange']
cont=-1
for elem in q:
    cont+=1
    tlist=[]
    ratiolist=[]    
    for i in range(nsteps):
        ratio=i*delta+delta
        try:
            t=t+(1/math.sqrt(1-2*elem+2*elem/ratio))*delta/ho
            tlist.append(t)
            ratiolist.append(ratio)
            #print (t,ratio)
        except:
            pass

    
    ax1.plot(ratiolist,tlist, linewidth=2.0, color=color[cont])
plt.axvline(x=1, ymin=0.1, ymax=0.9)
plt.show()
    
