import numpy as np
import matplotlib.pyplot as plt
import math
delta=0.01
fig, (ax1) = plt.subplots(1)
q=0.98
t=0
ho=1/(13*10**(9))
delta=0.01
plus=135
nsteps=int(2/delta)+plus
ax1.set_ylabel('Time')
ax1.set_xlabel('R(t)/R0')
q=[0.014,0.028,0.25,0.5,0.7,0.9]
listlegend=['qo='+str(q[0]),'qo='+str(q[1]),'qo='+str(q[2]),'qo='+str(q[3]),'qo='+str(q[4]),'qo='+str(q[5])]
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

    
    ax1.plot(ratiolist,tlist, linewidth=2.0, color=color[cont],label=listlegend[cont])
legend = ax1.legend(loc='upper right', shadow=True, fontsize='x-large')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('C0')

plt.axvline(x=1, ymin=0.01, ymax=1)
plt.show()
    
