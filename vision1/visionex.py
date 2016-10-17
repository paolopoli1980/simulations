# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:02:44 2016

@author: paolo
"""

from pylab import*
import numpy as np
from PIL import Image
from random import randint
import math

def ex1():
    img= Image.open('imex6.png')
    img = img.convert('L')
    im = img.load()
    img.show()
    numbercolor=255
    listpoint=[]
    number=100
    ntry=10
    xmax=0
    ymax=0
    el=0
    for k in range(number):
	
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if im[i,j]!=numbercolor and im[i,j]!=0 and im[i,j]!=1:    
                    listpoint.append([i,j])
                      
                  
                  
        for i in range(img.size[0]):
            for  j in range(img.size[1]):
                if im[i,j]==numbercolor:
                    try:
                        if im[i-1,j]<numbercolor and im[i+1,j]<numbercolor and im[i,j+1]<numbercolor and im[i,j-1]<numbercolor:
                            im[i,j]=1
                    except:
                        pass
        perc=img.size[0]*img.size[1]/10000
        print perc    
        if len(listpoint)<=perc:
            break
        if len(listpoint)>perc:
            casual=randint(0,len(listpoint))
            el+=1
            
            x=listpoint[casual][0]
            y=listpoint[casual][1]
            alfainc=0
            for t in range(ntry):
                massimo=0
                #print "merda"
                xnew=x
                ynew=y
                if t>0:
                    x=(xmax+x)/2
                    y=(ymax+y)/2
                    alfainc=0
    
		if t>ntry/2:
                    x=xmax
                    y=ymax
                    alfainc=0
	         #   print "xxx"		
	
                while alfainc<6.29:
                    alfainc+=0.005
                    xnew=x
                    ynew=y
                    
                    try:
                        while im[xnew,int(ynew)]<numbercolor:
                          
                            
                            xnew=xnew+cos(alfainc)
                            ynew=ynew+sin(alfainc)
                            dist=math.sqrt((x-xnew)**2+(y-ynew)**2)
                            if dist>massimo:
                                massimo=dist
				if im[xnew,int(ynew)]!=1 and im[xnew,int(ynew)]!=numbercolor:
	                                xmax=xnew
        	                        ymax=ynew
                                
                            try:
                                if im[xnew,int(ynew)]!=numbercolor:
                                    #print "cacchio"
                                    im[xnew,int(ynew)]=1
                            except:
                                pass
                    except:
                        pass                
            print "finish"    
            listpoint=[]    
            print el       
        
    
                  
 
    print listpoint
    elem.append(el)             
    img.show() 
elem=[]
for i in range(1):
    ex1()
print elem    
