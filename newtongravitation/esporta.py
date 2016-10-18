import time

from visual import * 
from visual.graph import *

 

f0=open("C:/Documents and Settings/Administrator/Desktop/paoloprg/posizione0.txt " , "r")
f1=open("C:/Documents and Settings/Administrator/Desktop/paoloprg/posizione1.txt " , "r")
f2=open("C:/Documents and Settings/Administrator/Desktop/paoloprg/posizione2.txt " , "r")
f3=open("C:/Documents and Settings/Administrator/Desktop/paoloprg/posizione3.txt " , "r")
f4=open("C:/Documents and Settings/Administrator/Desktop/paoloprg/posizione4.txt " , "r")

f10=open("C:/Documents and Settings/Administrator/Desktop/paoloprg/p1.txt " , "w")
f11=open("C:/Documents and Settings/Administrator/Desktop/paoloprg/p2.txt " , "w")
f12=open("C:/Documents and Settings/Administrator/Desktop/paoloprg/p3.txt " , "w")
f13=open("C:/Documents and Settings/Administrator/Desktop/paoloprg/p4.txt " , "w")
f14=open("C:/Documents and Settings/Administrator/Desktop/paoloprg/p5.txt " , "w")
 
dt=0.01
linea1=0
linea2=0
linea3=0
linea4=0
numero=0
t=0
contatore=0

limite=input('inserisci il numero di files')
 
 
 

 
 
 
         
     
 
              
         
        
             
        
contatore=0      
while contatore<limite:
 
        linea1="pippo"
        while linea1<>"":

                if contatore==0:
                        linea1 = (f0.readline())
                        f10.write(linea1)
                        linea1 = (f0.readline())
                        f10.write(linea1)
                        linea1 = (f0.readline())
                        f10.write(linea1)                        
                
                if contatore==1:
                        linea1 = f1.readline()
                        f11.write(linea1)
                        linea1 = f1.readline()
                        f11.write(linea1)
                        linea1 = f1.readline()
                        f11.write(linea1)                        
   
                if contatore==2:
                        linea1 = f2.readline()
                        f12.write(linea1)
                        linea1 = f2.readline()
                        f12.write(linea1)
                        linea1 = f2.readline()
                        f12.write(linea1)
                        
        contatore=contatore+1

f0.close;
f1.close;
f2.close;
f3.close;
f4.close;
f10.close;
f11.close;
f12.close;
f13.close;
f14.close;
