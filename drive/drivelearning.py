# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 15:02:20 2016

@author: paolo
"""

import pygame 
import math 
import graphics
import globalv
import dynamics
import matplotlib.pyplot as plt
import time


ax=0
ay=0
a=(ax**2+ay**2)**0.5
astart=a
x=0
y=0
vx=10
vy=0
px=0
py=0
pmemx=0
pmemy=0
maxtime=5000
pygame.init()
 
sizex=512
sizey=512
amax=a 
dt=0.05
incalfa=0.25
tol=5
ux=1
uy=0
wallsense=3
detectsense=5
size = [sizex,sizey]
crashpar=10
timer=0
screen = pygame.display.set_mode(size)
surfaceRender = pygame.Surface(screen.get_size() , pygame.SRCALPHA)
surfaceGrayRender = pygame.Surface(screen.get_size() , pygame.SRCALPHA)

 
pygame.display.set_caption("My Game")
 
done = False
configuration="" 
clock = pygame.time.Clock()
 
 
pygame.mouse.set_visible(0) 
idd=0
listpoints=[]
p=(0,0) 
f1=open("f1.sch","r")
stringa="x"

 
while len(stringa)>0:

    stringa=f1.readline()
    if len(stringa)>0:
        x=float(stringa[0:len(stringa)-1])
        stringa=f1.readline()
        y=float(stringa[0:len(stringa)-1])
        listpoints.append((x,y))
    
f1.close()

    
globalv.v=5
listpositions=[]
listversors=[]   
listvel=[]  
listacc=[]
refreshpoints=[]
  
while not done and idd==0:
    
     
    if idd==0:    
        for event in pygame.event.get():
               
            for el in listpoints:
                pygame.draw.circle(screen,globalv.BLACK,(int(el[0]),int(el[1])),2)
               
           # graphics.draw_root(screen,listpoints)
            if idd==0:
                pos = pygame.mouse.get_pos()
                
                x = pos[0]
                y = pos[1]
 
            
            
     
            if event.type == pygame.QUIT:
                done = True
                
            pos = pygame.mouse.get_pos()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if idd==0:
                    idd=1  
                    p=(x,y)                   
            if idd==0:
                graphics.draw_stick_figure(screen, x, y)
            
                
            pygame.display.flip()
            clock.tick(100)
               
            screen.fill(globalv.WHITE)
        

u=[]
     
pygame.quit()
starttime=time.time()
if idd==1:
#    time=0
    u[:]=dynamics.funz1(x,y,vx,vy,ax,ay,incalfa,tol,ux,uy,listpoints,dt,sizex,wallsense,detectsense,sizey,crashpar,astart,pmemx,pmemy,timer,amax,maxtime,refreshpoints)
  #  u[:]=dynamics.funz2(x,y,vx,vy,ax,ay,incalfa,tol,ux,uy,listpoints,dt,sizex,wallsense,detectsense,sizey,crashpar,astart,pmemx,pmemy,timer,amax,maxtime,refreshpoints,px,py)

    listpositions=[]
    
    
    while u[8]!=1 and time!=maxtime:
        #time+=1
    
        u[:]=dynamics.funz1(x,y,vx,vy,ax,ay,incalfa,tol,ux,uy,listpoints,dt,sizex,wallsense,detectsense,sizey,crashpar,astart,pmemx,pmemy,timer,amax,maxtime,refreshpoints)
 #       u[:]=dynamics.funz2(x,y,vx,vy,ax,ay,incalfa,tol,ux,uy,listpoints,dt,sizex,wallsense,detectsense,sizey,crashpar,astart,pmemx,pmemy,timer,amax,maxtime,refreshpoints,px,py)
        
        x=u[0]
        y=u[1]
        ux=u[2]
        uy=u[3]
        vx=u[4]
        vy=u[5]
        ax=u[6]
        ay=u[7]
        timer=u[9]
        listpositions.append([x,y])
        listversors.append([ux,uy])
        listvel.append(math.sqrt(vx**2+vy**2))
        listacc.append(math.sqrt(ax**2+ay**2))
     #   px=u[11]
     #   py=u[12]
endtime=time.time() 
print endtime-starttime
ready=raw_input("ready?")
print listversors 
print listvel
print listpositions
j=-1
 
screen = pygame.display.set_mode(size)
surfaceRender = pygame.Surface(screen.get_size() , pygame.SRCALPHA)
surfaceGrayRender = pygame.Surface(screen.get_size() , pygame.SRCALPHA)

 
pygame.display.set_caption("My Game")
 
done = False
configuration="" 
clock = pygame.time.Clock()
 
 
pygame.mouse.set_visible(0) 

for i in range(1):
    
    j=-1
    xbef=0
    ybef=0
    crashpar=5*detectsense
    screen.fill(globalv.WHITE)  

    for elx in listpoints:
          
          pygame.draw.circle(screen,globalv.BLACK,(int(elx[0]),int(elx[1])),2)

    for el in listpositions:
        j+=1
#        for elx in u[10]:
#          pygame.draw.circle(screen,globalv.BLACK,(int(elx[0]),int(elx[1])),2)
             
        
       # for elx in listpoints:
          
        #    pygame.draw.circle(screen,globalv.BLACK,(int(elx[0]),int(elx[1])),2)
        pygame.draw.circle(screen,globalv.WHITE,(int(xbef),int(ybef)),4)
        pygame.draw.circle(screen,globalv.BLUE,(int(el[0]),int(el[1])),4)
        pygame.draw.line(screen,globalv.WHITE,(int(xbef),int(ybef)),(int(xbef+listversors[j-1][0]*20),int(ybef+listversors[j-1][1]*20)))
        pygame.draw.line(screen,globalv.RED,(int(el[0]),int(el[1])),(int(el[0]+listversors[j][0]*20),int(el[1]+listversors[j][1]*20)))
        if j>7:
            if listversors[j-1][0]!=listversors[j][0] or listversors[j-2][0]!=listversors[j][0] or listversors[j-3][0]!=listversors[j][0] or listversors[j-4][0]!=listversors[j][0] or listversors[j-5][0]!=listversors[j][0] or listversors[j-6][0]!=listversors[j][0]or listversors[j-7][0]!=listversors[j][0]or listversors[j-8][0]!=listversors[j][0] :
                for elx in listpoints:
              
                    pygame.draw.circle(screen,globalv.BLACK,(int(elx[0]),int(elx[1])),2)
             
        xbef=el[0]
        ybef=el[1]
        pygame.display.flip()
        clock.tick(400)
           
#        screen.fill(globalv.WHITE)  
    plt.plot(listacc)
plt.show()            
         
pygame.quit() 
    
