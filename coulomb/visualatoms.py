from __future__ import division
from vpython import * 


ncharges=6
f1=open("datamotio.txt","r")
atomlist=[]
atoms=[]
w=10**11
for i in range(ncharges):
    stringa=f1.readline()
    atomlist=stringa.split(';')
    print (atomlist)
    atoms.append(sphere(pos=vec(float(atomlist[1])*w,float(atomlist[2])*w,float(atomlist[3])*w),radius=float(atomlist[0]),color=color.red))
 
f1.close()

f1=open("datamotio.txt","r")
niterations=40000
for j in range(niterations):
    rate(400)
    for k in range(ncharges):
        stringa=f1.readline()
        atomlist=stringa.split(';')

        atoms[k].pos.x=float(atomlist[1])*w
        atoms[k].pos.y=float(atomlist[2])*w
        atoms[k].pos.z=float(atomlist[3])*w
        #print(atoms[k].pos.x,atoms[k].pos.y,atoms[k].pos.z)
