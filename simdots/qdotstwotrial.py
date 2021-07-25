import math
import numpy as np
import matplotlib.pyplot as plt
import random
#s=[[math.sqrt(0.25),math.sqrt(0.75)],[math.sqrt(0.4),math.sqrt(0.6)],[math.sqrt(2)**(-1),math.sqrt(2)**(-1)]]

#s=[[0.7,0.3],[0.7,0.3],[0.9,0.1]]
#s=[[0.3,0.7],[0.1,0.9],[0.4,0.6]]
#news=s.copy()
#s=[[random.uniform(0,1),random.uniform(0,1)],[random.uniform(0,1),random.uniform(0,1)],[random.uniform(0,1),random.uniform(0,1)],[random.uniform(0,1),random.uniform(0,1)]]
#s=[[random.uniform(0,1),random.uniform(0,1)],[random.uniform(0,1),random.uniform(0,1)],[random.uniform(0,1),random.uniform(0,1)]]
#s=[[1,0.0],[1,0.0],[1,0.0]]
#s=[[0.7,0.3],[0.8,0.2],[0.2,0.8],[0.5,0.6]]
#s=[[0.8,0.2],[0.8,0.2],[0.8,0.],[0.8,0.2]]
s=[[0.7,0.3],[0.7,0.3],[0.1,0.9]]

print(s)
news=s.copy()
#t=[[1,1,0,0,0,1,0,1],[0,0,1,0,0,1,0,1],[0,1,0,1,1,1,0,0],[1,0,1,0,0,0,1,0]]
#t=[[1,1,1,0,1,0,1,0],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,1,1,0,1,0,1,0]]
t=[[0,0,1,1],[0,1,0,1],[1,0,0,1]]
print (len(s))
for j in range(3):
    s[j]=s[j]/np.linalg.norm(s[j])
    
print(s)
scopy=[[0,0],[0,0],[0,0]]
ls2=[]
ls=[[],[],[],[]]
ls2=[[],[],[],[]]
for n in range(20):
    scopy=[[0,0],[0,0],[0,0],[0,0]]
                              
    print('***********************')

    news[0]=[s[1][0]*s[2][0],s[1][0]*s[2][1],s[1][1]*s[2][0],s[1][1]*s[2][1]]
    news[1]=[s[0][0]*s[2][0],s[0][0]*s[2][1],s[0][1]*s[2][0],s[0][1]*s[2][1]]
    news[2]=[s[0][0]*s[1][0],s[0][0]*s[1][1],s[0][1]*s[1][0],s[0][1]*s[1][1]]
    
   # news[0]=[s[1][0]*s[2][0]*s[3][0],s[1][0]*s[2][0]*s[3][1],s[1][0]*s[2][1]*s[3][0],s[1][0]*s[2][1]*s[3][1],s[1][1]*s[2][0]*s[3][0],s[1][1]*s[2][0]*s[3][1],s[1][1]*s[2][1]*s[3][0],s[1][1]*s[2][1]*s[3][1]]
   # news[1]=[s[0][0]*s[2][0]*s[3][0],s[0][0]*s[2][0]*s[3][1],s[0][0]*s[2][1]*s[3][0],s[0][0]*s[2][1]*s[3][1],s[0][1]*s[2][0]*s[3][0],s[0][1]*s[2][0]*s[3][1],s[0][1]*s[2][1]*s[3][0],s[0][1]*s[2][1]*s[3][1]]
   # news[2]=[s[0][0]*s[1][0]*s[3][0],s[0][0]*s[1][0]*s[3][1],s[0][0]*s[1][1]*s[3][0],s[0][0]*s[1][1]*s[3][1],s[0][1]*s[1][0]*s[3][0],s[0][1]*s[1][0]*s[3][1],s[0][1]*s[1][1]*s[3][0],s[0][1]*s[1][1]*s[3][1]]
   # news[3]=[s[0][0]*s[1][0]*s[2][0],s[0][0]*s[1][0]*s[2][1],s[0][0]*s[1][1]*s[2][0],s[0][0]*s[1][1]*s[2][1],s[0][1]*s[1][0]*s[2][0],s[0][1]*s[1][0]*s[2][1],s[0][1]*s[1][1]*s[2][0],s[0][1]*s[1][1]*s[2][1]]   
    #news[3]=[s[0][0]*s[1][0],s[0][0]*s[1][1],s[0][1]*s[1][0],s[0][1]*s[1][1],0.,0.,0.,0.]      

    #print ('******news*********')
    #print (news)
    for i in range(2**2):
        
        scopy[0][int(t[0][i])]+=float(news[0][i])
        scopy[1][int(t[1][i])]+=float(news[1][i])
        scopy[2][int(t[2][i])]+=float(news[2][i])
       # scopy[3][int(t[3][i])]+=float(news[3][i])
        #if i<8:
            #scopy[3][int(t[3][i])]+=float(news[3][i])
    #print (scopy)    
    for j in range(3):
        #print(j)
        
        scopy[j]=scopy[j]/np.linalg.norm(scopy[j])
    print (scopy)                  
    for j in range(3):
        s[j]=scopy[j].copy()
        #print('{},{}'.format(j,s[j]**1))  
        ls[j].append(s[j][0]**2)
        ls2[j].append(s[j][1]**2)
plt.plot(ls[0])
plt.plot(ls[1])
plt.plot(ls[2])
#plt.plot(ls[3])
plt.show()
plt.clf()

plt.plot(ls2[0])
plt.plot(ls2[1])
plt.plot(ls2[2])
#plt.plot(ls2[3])
plt.show()
