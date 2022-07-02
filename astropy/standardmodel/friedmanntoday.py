import numpy as np
import matplotlib.pyplot as plt
import math
delta=0.01
fig, (ax1) = plt.subplots(1)
q=0.98
t=0
ho=1/(13*10**(9))
delta=0.01
plus=1200
nsteps=int(2/delta)+plus
ax1.set_ylabel('Time')
ax1.set_xlabel('R(t)/R0')
#q=[radiation,matter,spatial,cosmology(dark energy)]
q=[[1,0,0,0],[0,1,0,0],[0,0,0,1],[0.,0.028,0.972,0.],[0,0.28,0,0.72]]
listlegend=['qo='+str(q[0]),'qo='+str(q[1]),'qo='+str(q[2]),'qo='+str(q[3]),'qo='+str(q[4])]
color=['blue','red','yellow','green','pink','orange']
cont=-1
ax1.set_title('Friedmann all Densities included')
for elem in q:
    cont+=1
    tlist=[]
    ratiolist=[]
    t=0#gjj
    qtot=0
    
    for i in range(nsteps):
    
        ratio=i*delta+delta
        qtot=0
        for j in range(4):
            if j<3:
                qtot+=elem[j]*ratio**(j-2)
            if j==3:
                qtot+=elem[j]*ratio**(2)
                
            
        try:
            t=t+(1/math.sqrt(qtot))*delta/ho
            tlist.append(t)
            ratiolist.append(ratio)
            #print (t,ratio)
        except:
            pass

    
    ax1.plot(ratiolist,tlist, linewidth=2.0, color=color[cont],label=listlegend[cont])
legend = ax1.legend(loc='upper left', shadow=True, fontsize='x-large')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('C0')

plt.axvline(x=1, ymin=0.01, ymax=1)
plt.show()
    
