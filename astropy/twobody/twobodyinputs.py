import numpy as np
import sys
import time
from pygame.locals import *
import twobodysim
import tkinter as tk  
from functools import partial  
import math   
   
def call_result(label_result, mass1,speedx1,speedy1,mass2,speedx2,speedy2,distance,dt,contframe):
    f1=open("input_file.txt","w")
    g=6.67*10**-11
    ms=1.989*10**(30)
    mass1 = (mass1.get())  
    mass2 = (mass2.get())
    speedx1 = (speedx1.get())
    speedx2 = (speedx2.get())
    speedy1 = (speedy1.get())
    speedy2 = (speedy2.get())
    distance = (distance.get())
    contframe = (contframe.get()) 
    dt= (dt.get())
    
    result = str(float(mass1)*ms) + "Kg," + str(float(mass2)*ms)+"Kg"
    
    
    label_result.config(text="Masses = %s" % result)
    f1.write(str(float(mass1))+"\n")
    f1.write(str(float(speedx1))+"\n")
    f1.write(str(float(speedy1))+"\n")   
    f1.write(str(float(mass2))+"\n")
    f1.write(str(float(speedx2))+"\n")
    f1.write(str(float(speedy2))+"\n")      
    f1.write(str(float(distance))+"\n")
    f1.write(str(float(dt))+"\n")
    #f1.write(str(float(contframe))+"\n")    
    f1.close()
    twobodysim.start()
    return  
   
root = tk.Tk()  
root.geometry('400x200+100+200')  
  
root.title('Calculator')  
   
mass1 = tk.StringVar()  
mass2 = tk.StringVar()  
speedx1 = tk.StringVar()
speedy1 = tk.StringVar()
speedx2= tk.StringVar()
speedy2= tk.StringVar()
distance = tk.StringVar()
dt = tk.StringVar()
contframe= tk.StringVar()
labelNum1 = tk.Label(root, text="Mass 1 (Sun masses)").grid(row=1, column=0)  
  
labelNum2 = tk.Label(root, text="Speedx 1 m/s").grid(row=2, column=0)  

labelNum3 = tk.Label(root, text="Speedy 1 m/s").grid(row=3, column=0)

labelNum4 = tk.Label(root, text="Mass 2 (Sun masses)").grid(row=4, column=0)  
  
labelNum5 = tk.Label(root, text="Speedx 2 m/s").grid(row=5, column=0)

labelNum6 = tk.Label(root, text="Speedy 2 m/s").grid(row=6, column=0)

labelNum7 = tk.Label(root, text="Distance Au").grid(row=7, column=0)

labelNum8 = tk.Label(root, text="Delta t s").grid(row=8, column=0)  

#labelNum7 = tk.Label(root, text="Frames").grid(row=7, column=0)  

labelResult = tk.Label(root)  
  
labelResult.grid(row=10, column=2)  
  
entryNum1 = tk.Entry(root, textvariable=mass1).grid(row=1, column=2)  
  
entryNum2 = tk.Entry(root, textvariable=speedx1).grid(row=2, column=2)

entryNum3 = tk.Entry(root, textvariable=speedy1).grid(row=3, column=2)

entryNum4 = tk.Entry(root, textvariable=mass2).grid(row=4, column=2)  
  
entryNum5 = tk.Entry(root, textvariable=speedx2).grid(row=5, column=2)  

entryNum6 = tk.Entry(root, textvariable=speedy2).grid(row=6, column=2)  

entryNum7 = tk.Entry(root, textvariable=distance).grid(row=7, column=2)  

entryNum8 = tk.Entry(root, textvariable=dt).grid(row=8, column=2)  

#entryNum7 = tk.Entry(root, textvariable=contframe).grid(row=7, column=2)  


call_result = partial(call_result, labelResult, mass1, speedx1,speedy1,mass2,speedx2,speedy2,distance,dt,contframe)

#textbox2 = tk.Entry(root, textvariable=strmass1).grid(row=7,column=2)

#first=(mass1.get())
#Text1=tk.Text(root,text=first).grid(row=5,column=2)
  
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=10, column=0)  
  
root.mainloop()

