# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:28:34 2016

@author: paolo
"""
import math
import globalv

 
  

def rotation(ux,uy,alfa):
    rx=ux*math.cos(alfa)-uy*math.sin(alfa)
    ry=ux*math.sin(alfa)+uy*math.cos(alfa)
    return rx,ry
    
def euler(ax,ay,vx,vy,x,y,dt):
    
    vx=vx+ax*dt
    vy=vy+ay*dt
    x=x+vx*dt
    y=y+vy*dt
    return (vx,vy,x,y)
    
   
def check_crash(x,y,listpoints,ux,uy,tol,sizex,wallsense,sizey,refreshpoints):
    stop=0
    for el in listpoints:
  
        if math.sqrt((x-el[0])**2+(y-el[1])**2)<wallsense or x<5 or x>sizex-10 or y<5 or y>sizey-10:
            stop=1
            #refreshpoints.append([el[0],el[1]])
    return stop        

def check_precrash(x,y,listpoints,ux,uy,tol,sizex,detectsense,wallsense):
    detect=0
    dist=1000000000000

    for el in listpoints:

        if math.sqrt((x-el[0])**2+(y-el[1])**2)<dist:
            dist=math.sqrt((x-el[0])**2+(y-el[1])**2)
             
        if math.sqrt((x-el[0])**2+(y-el[1])**2)<3*wallsense:
            detect=1
            
    return detect,dist    
    
     
    
def pathcheck1(x,y,listpoints,ux,uy,tol,sizex,incalfa,dt,wallsense,detectsense,sizey,pmemx,pmemy):
    p=[]
    alfa=0
    p.append(rotation(ux,uy,math.pi*0.3))
    distmem=0
    while alfa<0.6*math.pi:
        alfa+=incalfa
      #  print alfa
        p=rotation(ux,uy,math.pi*0.4-alfa)
        dett=0
        xm=x
        ym=y
        t=0  
        dt=0.5          
        while dett!=1:
            t+=dt
            xm=x+p[0]*t
            ym=y+p[1]*t
            
            for el in listpoints:
             
                if math.sqrt((xm-el[0])**2+(ym-el[1])**2)<detectsense or xm<5 or xm>sizex-10 or ym<5 or ym>sizey-10:
                  
                    dett=1
                    #pmemx=el[0]
                    #pmemy=el[1]
                    if math.sqrt((x-el[0])**2+(y-el[1])**2)>distmem:
                        distmem=math.sqrt((x-el[0])**2+(y-el[1])**2)
                        uxx=p[0]
                        uyy=p[1]
                     #   print "set",ux,uy
      #  timer=0                    
    return uxx,uyy                
        
        
                        
    
    
 
    
def funz1(x,y,vx,vy,ax,ay,incalfa,tol,ux,uy,listpoints,dt,sizex,wallsense,detectsense,sizey,crashpar,astart,pmemx,pmemy,timer,amax,maxtime,refreshpoints):
    ok=0
    globalv.v=100
    a=math.sqrt(ax**2+ay**2)
    v=math.sqrt(vx**2+vy**2)
    timer+=1
   # print "timer",timer
    if timer==maxtime:
        ok=1
        
#    if check_precrash(x,y,listpoints,ux,uy,tol,sizex,detectsense)[1]<crashpar and check_precrash(x,y,listpoints,ux,uy,tol,sizex,detectsense)[1]>detectsense:
 #       if v>0.5:
  #          a-=0.5
 #   a=astart*math.atan(check_precrash(x,y,listpoints,ux,uy,tol,sizex,detectsense)[1]-1*crashpar)*2/math.pi
   # a=1 
    ax=a*ux
    ay=a*uy 
   # print "checkdist",check_precrash(x,y,listpoints,ux,uy,tol,sizex,detectsense)[1]-crashpar
  # print "a",a
    if check_precrash(x,y,listpoints,ux,uy,tol,sizex,detectsense,wallsense)[0]==1:
        uxx=pathcheck1(x,y,listpoints,ux,uy,tol,sizex,incalfa,dt,wallsense,detectsense,sizey,pmemx,pmemy)[0]
        uyy=pathcheck1(x,y,listpoints,ux,uy,tol,sizex,incalfa,dt,wallsense,detectsense,sizey,pmemx,pmemy)[1]
#        a=math.sqrt(ax**2+ay**2)
        v=math.sqrt(vx**2+vy**2)
        
        a=amax
        k=v
        ux=uxx
        uy=uyy
            
        vx=k*ux
        vy=k*uy

       # ax=k*ux
        #ay=k*uy
        #print "versori", ux,uy,math.sqrt(vx**2+vy**2)
                
    if check_crash(x,y,listpoints,ux,uy,tol,sizex,wallsense,sizey,refreshpoints)==1:
        vx=0
        vy=0
        ax=0
        ay=0
        ok=1
       # print "stop"
        #exit()

    vxx=euler(ax,ay,vx,vy,x,y,dt)[0]
    vyy=euler(ax,ay,vx,vy,x,y,dt)[1]
    xx=euler(ax,ay,vx,vy,x,y,dt)[2]
    yy=euler(ax,ay,vx,vy,x,y,dt)[3]
    x=xx
    y=yy
    vy=vyy
    vx=vxx
    
    return x,y,ux,uy,vx,vy,ax,ay,ok,timer,refreshpoints 
    
 

 


    
    
    
        