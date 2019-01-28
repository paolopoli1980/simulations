import pygame
from pygame.locals import *
from sys import exit
import time
import random
import math


class robot:
    
    def __init__(self):
        self.type=0
        self.x=0
        self.y=0
        self.vers=[]
        self.vx=0
        self.vy=0
        self.crash=0
        self.radius=0
        self.oldx=0
        self.oldy=0
        self.maxdist=0
        self.memvx=0
        self.memvy=0
        self.ndist=0
        self.start=1
        self.visualang=0

    
    def visual(self,vx,vy):
        
        
        incx=0
        incy=0
        
        print (self.x,self.y)
        print (len(matrix_win))
        while matrix_win[int(self.y+incy)][int(self.x+incx)]!=1 and self.x+incx>20 and self.x+incx<width-20 and self.y+incy>20 and self.y+incy<480:
       # while self.x+incx>20 and self.x+incx<width-20 and self.y+incy>20 and self.y+incy<480:

            incx+=vx*0.25
            incy+=vy*0.25
           # print ("in")
        print ("0ut")    
        print (self.x+incx,self.y+incy)
            
                
                
        if math.sqrt(incx**2+incy**2)>self.maxdist:
            red=(255,0,0)
            self.maxdist=math.sqrt(incx**2+incy**2)
            self.memvx=vx
            self.memvy=vy
            
            pygame.draw.line(win,red,(int(self.x),int(self.y)),((int((self.x+incx))),(int((self.y+incy)))))    
            self.vers=[self.memvx,self.memvy]
            time.sleep(0.5)
        
        
    
    
        
    def algorithm(self,tipo):
        
        
        
        if tipo==0:
            angle=random.uniform(0,2*math.pi)
            vx=math.cos(angle)
            vy=math.sin(angle)
            print (vx,vy)
           # t=input("insert")
            self.vers=[vx,vy]
        if tipo==1:
            self.memvx=0
            self.memvy=0
            self.maxdist=0
            for i in range(int(self.ndist)):
                angle=random.uniform(0,2*math.pi)
                vx=math.cos(angle)
                vy=math.sin(angle)
                self.visual(vx,vy)
          #  print (self.memvx,self.memvy)    
            self.vers=[self.memvx,self.memvy]    
            print (self.vers)
        if tipo==2:
            if self.start==1:
                angle=random.uniform(0,2*math.pi)
                vx=math.cos(angle)
                vy=math.sin(angle)
                self.start=2    
            else:
                
                pass

    def check_crash(self,width,height):
        self.crash=0
        if self.x>width-20-self.radius:
            self.crash=1
            self.x=width-20-self.radius
        if self.x<20+self.radius:
            self.crash=1
            self.x=20+self.radius
        if self.y<20+self.radius:
            self.crash=1
            self.y=20+self.radius
        if self.y>480-self.radius:
            self.crash=1
            self.y=480-self.radius
            #print (point)
        if matrix_win[int(self.y)][int(self.x)]==1:
            self.crash=1
            self.x=self.oldx
            self.y=self.oldy            

        return self.crash
    
    def moving(self,tipo,start,width,height):
     
        

        blue=(0,0,255)
        red=(255,0,0)
        if tipo==0 or tipo==1:
            self.radius=8
            
            if (self.check_crash(width,height)==1) or (start==1):
                self.algorithm(tipo)
                start=0
                
            if self.check_crash(width,height)==0:
                self.oldx=self.x
                self.oldy=self.y
                self.x+=self.vers[0]
                self.y+=self.vers[1]
              # print(self.vers[0],self.vers[1])
            
        pygame.draw.circle(win,blue,(int(self.x),int(self.y)),self.radius)
        pygame.draw.line(win,red,(int(self.x),int(self.y)),((int((self.oldx+self.vers[0]*self.radius*2))),(int((self.oldy+self.vers[1]*self.radius*2)))))    
    
    def position(self,x,y):
        blue=(0,0,255)
        pygame.draw.circle(win,blue,(x,y),5)
    


def menu():
    win.blit(button[0],(650,520))
    win.blit(button[1],(650,550))
    win.blit(button[2],(650,580))
    win.blit(button[3],(550,520))
    


def draw_borders(width,height):
    blue=(0,0,255)
    pygame.draw.rect(win, blue, [0,0,width,20])
    pygame.draw.rect(win, blue, [0,0,20,500])
    pygame.draw.rect(win, blue, [0,480,width,20])
    pygame.draw.rect(win, blue, [width-20,0,width,500])

#############################################
#-----------general setting------------------
#############################################

nrobots=3
enable_target=False
numberobots=1
numberoftargets=0
WHITE=(255,255,255)
red=(255,0,0)
black=(0,0,0)
pygame.init()
scenario=[]
size=width, height =800,600
win=pygame.display.set_mode(size)
print (win)
pygame.display.set_caption("Robot world")
#pygame.Surface.fill(color='white', rect=None, special_flags=0)
run=True
win.fill(WHITE)
setoflinepoints=[]
button=[pygame.image.load('buttons/button2.png').convert(),pygame.image.load('buttons/button3.png').convert(),pygame.image.load('buttons/button4.png').convert(),pygame.image.load('buttons/button5.png').convert()]
robots=[]
matrix_win = [[0 for y in range(width)] for x in range(height)]


global vx,vy

for i in range (nrobots):
    robots.append(robot())
############################################
#-------------start the cycle---------------
############################################
drawing_activation=False
countmouseclick=-1
putarget=0
putrobot=False
realtime=False
xr=0
yr=0
start=1
vx=0
vy=0

while run:
    win.fill((255,255,255))    
    menu()
    draw_borders(width,height)
    pos = pygame.mouse.get_pos()
    for line in setoflinepoints:
       # print (line)
        pygame.draw.line(win,red,(line[0],line[1]),(line[2],line[3]),1)
        minx=0
        miny=0
        maxx=0
        maxy=0
    if putarget==1:
        pygame.draw.circle(win,black,(targetx,targety),5)
    if realtime==True:
        
        robots[int(select)].moving(int(select),start,width,height)
        start=0
    for event in pygame.event.get():

            
        if (putrobot==True and event.type==pygame.MOUSEBUTTONUP):
            print (select)
            print (pos[0],pos[1])
            robots[int(select)].x=pos[0]
            robots[int(select)].y=pos[1]
            putrobot=False
            realtime=True
            xr=pos[0]
            yr=pos[1]
            
                
        if enable_target==True and event.type==pygame.MOUSEBUTTONUP and putarget==0 and putrobot==False:
            putarget=1
            targetx=pos[0]
            targety=pos[1]
            
        if drawing_activation==True and event.type==pygame.MOUSEBUTTONUP and putrobot==False:
            if countmouseclick==1:
#                pygame.draw.line(win,red,(xdrawline,ydrawline),(pos[0],pos[1]),1)
#                pygame.draw.line(win,red,(1,1),(100,300),width=1)
                setoflinepoints.append([xdrawline,ydrawline,pos[0],pos[1]])
                countmouseclick=-1
                drawing_activation=False
                print ("drawn")

                deltax=pos[0]
                deltay=pos[1]
                print (deltax,deltay)
                
                distxy=math.sqrt((pos[0]-xdrawline)**2+(pos[1]-ydrawline)**2)
                if math.fabs(pos[0]-xdrawline)<=math.fabs(pos[1]-ydrawline):
                    deltat=math.fabs((pos[0]-xdrawline)/distxy)
                    cont=math.fabs(distxy/deltat)
                else:
                    deltat=math.fabs((pos[1]-ydrawline)/distxy)
                    cont=math.fabs(distxy/deltat)
                ct=0
                ct*=0.1
                while ct<=distxy:
                    
                    matrix_win[int(deltay)][int(deltax)]=1
                    matrix_win[int(deltay)][int(deltax)-1]=1
                    matrix_win[int(deltay)][int(deltax)+1]=1
                    matrix_win[int(deltay)-1][int(deltax)]=1
                    matrix_win[int(deltay)+1][int(deltax)]=1
                    matrix_win[int(deltay)+1][int(deltax)+1]=1
                    matrix_win[int(deltay)-1][int(deltax)+1]=1
                    matrix_win[int(deltay)+1][int(deltax)-1]=1
                    matrix_win[int(deltay)-1][int(deltax)-1]=1

                #   print (deltax,deltay)
                    deltax=pos[0]+(xdrawline-pos[0])*ct/distxy
                    deltay=pos[1]+(ydrawline-pos[1])*ct/distxy
                    ct+=deltat
                   # print (ct)
                    
                #print (matrix_win)     
                    
                    
                    
                    
                

            if countmouseclick==0:
                #pygame.draw.rect(win, red, [pos[0],pos[1],1,1])
                countmouseclick=1
                xdrawline=pos[0]
                ydrawline=pos[1]
                print ("ba")                
                

        if event.type==pygame.QUIT:
            run=False
            
        if event.type==pygame.MOUSEBUTTONUP:
            print(pos)
            if pos[0]>650 and pos[0]<739 and pos[1]>520 and pos[1]<541:
                drawing_activation=False
                if enable_target==True:
                    print( "select the robot you want:=")
                    for i in range(nrobots):
                        if i==0:
                            print(str(i)+"->move in a random position when crash on some barrier")
                        if i==1:    
                            print(str(i)+"choose four random directions and choose the longest path")
                        if i==2:
                            print(str(i)+"It carry on to follow the longest path in a specific visual range")
                            
                    select=input("Select your robot and put it on the screen")    
                    if select=='1':
                        robots[1].ndist=input("put the number of distances it has to consider")                        
                    if select=='2':
                        robots[2].visualang=input("put the angle of the robot visual\n")
                        robots[2].ndist=input("put the number of distances it has to consider")

                    putrobot=True       
                        

            if pos[0]>650 and pos[0]<739 and pos[1]>580 and pos[1]<601 and putrobot==False:
                drawing_activation=False
                if len(setoflinepoints)>0:
                    del setoflinepoints[len(setoflinepoints)-1]

            if pos[0]>650 and pos[0]<739 and pos[1]>550 and pos[1]<573 and putrobot==False:
                drawing_activation=True
                countmouseclick=0
                
            if pos[0]>550 and pos[0]<639 and pos[1]>520 and pos[1]<541 and putrobot==False:
                drawing_activation=False
                enable_target=True
                        
                

    pygame.display.update()
#    pygame.display.flip()  

    
    
pygame.quit()    
