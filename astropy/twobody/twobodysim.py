import pygame
from pygame.locals import *
from sys import exit
import os
import random
import sys
import numpy as np
import matplotlib.pyplot as plt
import sys
import gravitycalc
import math
def start():

    numberofmasses=2
    bodies=[]
    f1=open("input_file.txt","r")
    m1=float(str(f1.readline())[:-1])
    s1x=float(str(f1.readline())[:-1])
    s1y=float(str(f1.readline())[:-1])
    m2=float(str(f1.readline())[:-1])
    s2x=float(str(f1.readline())[:-1])
    s2y=float(str(f1.readline())[:-1])    
    d=float(str(f1.readline())[:-1])
    dt=float(str(f1.readline())[:-1])
    #tframe=float(str(f1.readline())[:-1])



    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    black=(0,0,0)
    for i in range(numberofmasses):
        bodies.append(gravitycalc.body())

    bodies[0].x=-d/2
    bodies[0].y=0
    bodies[0].z=0
    bodies[0].vx=s1x
    bodies[0].vy=s1y
    bodies[0].vz=0
    bodies[0].ax=0
    bodies[0].ay=0
    bodies[0].az=0
    bodies[0].mass=m1
    bodies[0].G=1

    bodies[0].index=0
    bodies[0].radius=2

    bodies[1].x=d/2
    bodies[1].y=0
    bodies[1].z=0
    bodies[1].vx=s2x
    bodies[1].vy=s2y
    bodies[1].vz=0
    bodies[1].ax=0
    bodies[1].ay=0
    bodies[1].az=0
    bodies[1].mass=m2
    bodies[1].index=1
    bodies[1].radius=1
    bodies[1].G=1

    pressed=False
    memx1=[]
    memy1=[]
    memx2=[]
    memy2=[]
    #dt=365*24*3600/niterations
    #dt=31536000*200/niterations
    
    t=0
    totenergy=0
    energiapot=0
    energiakin=0
    cont=0
    #for el in bodies:
    #    print (el.acceleration)


    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([800, 800])
     
    # set the pygame window name


    # Run until the user asks to quit
    running = True
    pygame.display.set_caption('Two bodies simulation')
    font = pygame.font.Font('freesansbold.ttf', 12) 
    text1 = font.render('x1='+str(bodies[0].x), True,  black,white)
    text2 = font.render('y1='+str(bodies[0].y), True,  black,white)
    #text3 = font.render('z1='+str(bodies[0].z), True,  black,white)

    text4 = font.render('x2='+str(bodies[1].x), True,  black,white)
    text5 = font.render('y2='+str(bodies[1].y), True,  black,white)        
   # text6 = font.render('z2='+str(bodies[1].z), True,  black,white)        
    text7 = font.render('Energy='+str(totenergy), True,  black,white)        
    text8 = font.render('t='+str(t), True,  black,white)        
    
    textRect1 = text1.get_rect()
    textRect1.center = (100, 10)
    textRect2 = text2.get_rect()
    textRect2.center = (100, 30)
    #textRect3 = text3.get_rect()
    #textRect3.center = (100, 55)
    textRect4 = text4.get_rect()
    textRect4.center = (100, 50)
    textRect5 = text5.get_rect()
    textRect5.center = (100, 70)
    #textRect6 = text6.get_rect()
    #textRect6.center = (100, 115)
    textRect7 = text7.get_rect()
    textRect7.center = (100, 90)
    textRect8 = text8.get_rect()
    textRect8.center = (100, 110)

    while running:
        #print(t)
        memx1.append(bodies[0].x)
        memy1.append(bodies[0].y)
        memx2.append(bodies[1].x)
        memy2.append(bodies[1].y)
        for j in range(numberofmasses):
            for k in range(j,numberofmasses):
                if k!=j:
                    
                    dist=math.sqrt((bodies[k].x-bodies[j].x)**2+(bodies[k].y-bodies[j].y)**2+(bodies[k].z-bodies[j].z)**2)
                    energiapot-=bodies[k].mass*bodies[j].mass*bodies[k].G/dist
            energiakin+=0.5*bodies[j].mass*(bodies[j].vx**2+bodies[j].vy**2+bodies[j].vz**2)
        totenergy=energiapot+energiakin
        
       # mu=bodies[0].mass*bodies[1].mass/(bodies[0].mass+bodies[1].mass)
        #energiakin=0.5*mu*(bodies[0].vx-bodies[1].vx)**2+(bodies[0].vy-bodies[1].vy)**2+(bodies[0].vz-bodies[1].vz)**2
       # dist=math.sqrt((bodies[0].x-bodies[1].x)**2+(bodies[0].y-bodies[1].y)**2+(bodies[0].z-bodies[1].z)**2)
       # energiapot-=bodies[0].mass*bodies[1].mass*bodies[0].G/dist
        #totenergy=energiapot+energiakin
        text1 = font.render('x='+str(bodies[0].x), True,  black,white)
        text2 = font.render('y='+str(bodies[0].y), True,  black,white)
        text3 = font.render('z='+str(bodies[0].z), True,  black,white)
        text4 = font.render('x='+str(bodies[1].x), True,  black,white)
        text5 = font.render('y='+str(bodies[1].y), True,  black,white)
        text6 = font.render('z='+str(bodies[1].z), True,  black,white)
        text7 = font.render('E='+str(totenergy), True,  black,white)      
        text8 = font.render('t='+str(t), True,  black,white)
        for j in range(numberofmasses):
            gravitycalc.rk4(j,dt,numberofmasses,bodies)
            #gravitycalc.eulero(j,dt,numberofmasses,bodies)
        energiakin=0
        for j in range(numberofmasses):
            #print(j)
            
            bodies[j].x=bodies[j].virtualx
            bodies[j].y=bodies[j].virtualy
            bodies[j].z=bodies[j].virtualz
            bodies[j].vx=bodies[j].virtualvx
            bodies[j].vy=bodies[j].virtualvy
            bodies[j].vz=bodies[j].virtualvz

            #energiakin+=0.5*bodies[j].mass*(bodies[j].vx**2+bodies[j].vy**2+bodies[j].vz**2)
                    
        energiapot=0    


        # Did the user click the window close button?

        string=""
        
            

        t+=dt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
     
               tasti_premuti = pygame.key.get_pressed()        

                
               if event.key == K_o:
                   if pressed==False:
                       pressed=True
                   else:
                       pressed=False              

        # Fill the background with white
        screen.fill((255, 255, 255))

        # Draw a solid blue circle in the center
  
        pygame.draw.circle(screen, (0, 0, 255), (400+int(25*bodies[0].x), 400+int(25*bodies[0].y)), 10)
        pygame.draw.circle(screen, (100, 100, 55), (400+int(25*bodies[1].x), 400+int(25*bodies[1].y)), 10)
        if pressed==True:
            for h in range(len(memx1)):
                pygame.draw.circle(screen, (0, 0, 255), (400+int(25*memx1[h]), 400+int(25*memy1[h])), 1)
                pygame.draw.circle(screen, (100, 100, 55), (400+int(25*memx2[h]), 400+int(25*memy2[h])), 1)
                
                

                   
               

        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        #screen.blit(text3, textRect3)
        screen.blit(text4, textRect4)
        screen.blit(text5, textRect5)
        #screen.blit(text6, textRect6)
        screen.blit(text7, textRect7)
        screen.blit(text8, textRect8)            
    #
        # Flip the display
        pygame.display.flip()
      
    pygame.quit()
