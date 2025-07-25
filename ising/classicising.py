﻿# -*- coding: utf-8 -*-
"""
Created on Wed Dec 05 18:46:57 2012

@author: paolo
"""

#modello di ising mono e bidimensionale

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
 
 

 
spin=[]
 
def ising_bidimensionale(coefj,delta_temperatura,tipo_allineamento,n_spinx,n_spiny,temperatura_iniziale,temperatura_finale,interazioni):

    magnetizzazione=[]
    energia=0
    mem_temp=[]
    numero_passi=0
             
    #divide le tre situazioni iniziali possibili diverse

    if tipo_allineamento=="up": 
        spin=np.zeros((n_spinx,n_spiny))+0.5
         
    if tipo_allineamento=="dw": 
        spin=np.zeros((n_spinx,n_spiny))-0.5
         
    if tipo_allineamento=="rn":
         
        spin=np.random.randint(-1,1,(n_spinx,n_spiny))+0.5
    #setta il contorno a up
    for i in range(n_spinx):
        spin[0,i]=0.5
        spin[n_spiny-1,i]=0.5
    for i in range(n_spiny):
        spin[i,0]=0.5
        spin[i,n_spinx-1]=0.5
        
   
   #calcolo energia iniziale

    
    for j in range(n_spiny):    
        for i in range(n_spinx):
    
           x=i
           y=j
           x2=int(i+1)
           if i>0:
               x3=int(i-1)
           y2=int(j+1)
           if j>0 :
               y3=int(j-1)
           
           
            
           if (i==0):
               x3=int(n_spinx-1)
               x2=1     
           if (j==0):
               y3=int(n_spiny-1)
               y2=1
           
           if (i==n_spinx-1):
               x3=int(n_spinx-2)
               x2=0
             

           if (j==n_spiny-1):
               y3=int(n_spiny-2)
               y2=0
            
           energia=energia-coefj*(spin[x,y]*spin[x2,y]+spin[x,y]*spin[x3,y]+spin[x,y]*spin[x,y2]+spin[x,y]*spin[x,y3]) 
      #     print energia

   #inizia simulazione con incremento o decremento temperatura     
           #comandi per disegnare i grafici degli spin  
           if spin[i,j]>0 :
               plot(i*1,j , 'b.')
                 
           else :
               plot(i*1,j , 'r.')
      
    grid(True)
   
    
    show()   
    
    
    temperatura=temperatura_iniziale    
    if (temperatura_iniziale>temperatura_finale):
        delta_temperatura=-delta_temperatura
    else:
        delta_temperatura=delta_temperatura

    temperatura=temperatura_iniziale        
    numero_passi=int((temperatura_finale-temperatura_iniziale)/delta_temperatura)
  
    if delta_temperatura<0:
     
         temperatura=temperatura_iniziale        
         numero_passi=-int((temperatura_iniziale-temperatura_finale)/delta_temperatura)    
  
 
    conta_colonna=-1   
    energia_list=[]             
         
   
    while (conta_colonna<numero_passi-2):
        conta_colonna=conta_colonna+1        
     
        temperatura=temperatura+delta_temperatura
        print(temperatura)
           
      
       
        # qui processa gli spin con il metodo montecarlo tenendo conto del
        #numero di iterazioni date
        
        if temperatura>0:
            
            for i in range(numero_iterazioni):
                casual=np.random.randint(1,n_spinx-1)
                casual2=np.random.randint(1,n_spiny-1)
                tiro=0
              
               #queste variabili servono per i bordi e le condizioni al contorno
 
                x=casual-1
                x2=casual+1
                y=casual2-1
                y2=casual2+1
  
   
                if (casual==0):
                    x=n_spinx-1
                    #x=1
                if (casual==n_spinx-1):
                    x2=0
                    #x2=n_spinx-2    
                                         
                if (casual2==n_spiny-1):
                    y2=0
                    #y2=n_spiny-2
                if (casual2==0):
                    y=n_spiny-1
                    #y=1
                          
            
     
                if spin[casual,casual2]<0:
                    spin[casual,casual2]=0.5
                else:    
                    spin[casual,casual2]=-0.5             
                 
           
              
              #la differenza di energia tra cambiare uno singolo spin e no                

                somma=spin[x,casual2]+spin[x2,casual2]+spin[casual,y2]+spin[casual,y]                
                if (somma==2):                
                    delta_energia=-spin[casual,casual2]*8*coefj
                if (somma==1):                
                    delta_energia=-spin[casual,casual2]*4*coefj
                if (somma==0):                
                    delta_energia=0
                if (somma==-1):                
                    delta_energia=+spin[casual,casual2]*4*coefj
                if (somma==-2):                
                    delta_energia=+spin[casual,casual2]*8*coefj     
                         
            
            # metodo di montecarlo.....         
                energia=energia+delta_energia    
              
                if delta_energia>0:
 
                    tiro=np.random.uniform(0,1) 
                 
                if tiro>np.exp(-delta_energia/ temperatura):
                    spin[casual,casual2]=-spin[casual,casual2]
                    energia=energia-delta_energia
       
        
 
        #memorizza i valori da mettere sul grafico
        
        magnetizzazione.append(0) 
        mem_temp.append(temperatura)
        
         
        energia_list.append(energia/(n_spinx*n_spiny))        

        for j in range(n_spiny):
            
            for i in range(n_spinx):
 
 
                magnetizzazione[conta_colonna]=magnetizzazione[conta_colonna]+2*spin[i,j]            
                #calcolo la situazione finale per le varie grandezze in considerazione             
                if (temperatura_iniziale<temperatura_finale):
                    if (temperatura>temperatura_finale-k*delta_temperatura):
                        if spin[i,j]>0 :
                            plot(i,j , 'b.')
  
                        else :
                            plot(i,j , 'r.')
   
                if (temperatura_iniziale>temperatura_finale):
                  #  print(temperatura_finale-k*delta_temperatura)                                             
                    if (temperatura<temperatura_finale-k*delta_temperatura):
                         
                        if spin[i,j]>0 :
                            plot(i,j , 'b.')
                           
                        else :
                            plot(i,j , 'r.')
                            
            
             
        magnetizzazione[conta_colonna]=magnetizzazione[conta_colonna]/(n_spinx*n_spiny)       
      #  print(magnetizzazione[conta_colonna])
        grid(True)
   # xlabel('KT')
   # ylabel('<M>')
        #show()
    plt.figure(figsize=(10,7))        
    plt.xlabel('KT')
    plt.ylabel('Blue <M>, Green <E>')
    #cv=[0]
    #for i in range(len(energia_list)-1):
     #   cv.append((energia_list[i+1]-energia_list[i])/((mem_temp[1]-mem_temp[0])))
    
    plt.plot(mem_temp,magnetizzazione)    
    plt.plot(mem_temp,energia_list)        
    #plt.plot(mem_temp,cv)
    plt.show()
    print (temperatura)             
     


def ising_monodimensionale(coefj,delta_temperatura,tipo_allineamento,n_spin,temperatura_iniziale,temperatura_finale,interazioni,conta_k):
    
    #settaggio iniziale 
     
    magnetizzazione=[]   #vettore magnetizzazione nel tempo
    energia=0            #energia totale
    mem_temp=[]          #vettore temperature   
    numero_passi=0       
    #selezionano i tre tipi di allineamenti iniziali possibili    
    
    if tipo_allineamento=="up": 
        spin=np.zeros(n_spin)+0.5
    if tipo_allineamento=="dw": 
        spin=np.zeros(n_spin)-0.5
        
    if tipo_allineamento=="rn":
        
 
        spin=np.zeros(n_spin)
        for i in range(n_spin):        
            casual=np.random.randint(0,2)-0.5    
            
            spin[i]=casual
   
        #inizio simulazione
    
        #calcolo energia iniziale
    
    
    for i in range(n_spin):
       #energia stando attenti alle condizioni al contorno 
        if i<(n_spin-1) :
            energia=energia - coefj*spin[i]*spin[i+1]
        if i==(n_spin-1):
            energia=energia - coefj*spin[0]*spin[n_spin-1]
     
   #inizia simulazione con incremento o decremento temperatura     
    temperatura=temperatura_iniziale    
    
    #in base al calo o alla crescita della temperatura cambia il segno alla delta temperatura

    if (temperatura_iniziale>temperatura_finale):
        delta_temperatura=-delta_temperatura
        
                    
                    
            
    else:
        delta_temperatura=delta_temperatura
        
    temperatura=temperatura_iniziale        
    #calcola il numero dei passi
    numero_passi=int((temperatura_finale-temperatura_iniziale)/delta_temperatura)
    
    if delta_temperatura<0:
 
         temperatura=temperatura_iniziale        
         numero_passi=-int((temperatura_iniziale-temperatura_finale)/delta_temperatura)    
         
    #variabili che gestisocono rispettivamente il passo nel grafico e l'energia sulle ordinate     
    conta_colonna=-1   
    energia_list=[]      
    aggrego=-1
   #inizia il ciclo incrementando o decrementando le temperatura 
    while (conta_colonna<numero_passi-2):
       # print (temperatura)
        conta_colonna=conta_colonna+1        
   
        temperatura=temperatura+delta_temperatura
           
        #qui itera più volte a pari temperatura,una volta sarabbe poco,a occhio si da una stima di questo parametro
        #bisogna dare la possibilità al sistema di potere cambiare sarà poi montecarlo a fare selezione sui grandi
        #numeri
        if temperatura>0:        
            for i in range(numero_iterazioni):
            #sceglie uno spin a caso e lo gira processandolo con Montecarlo
            
                casual=np.random.randint(0,n_spin)
                tiro=0
                 
             
                if spin[casual]<0:
                    spin[casual]=0.5
                    
                else:    
                    spin[casual]=-0.5             
                x=casual-1
                x2=casual+1

                if (casual==0):
                    x=n_spin-1
    
                if (casual==n_spin-1):
                    x2=0
                somma=spin[x]+spin[x2]              
                if (somma==1):
                    delta_energia=-spin[casual]*coefj* 2
                if (somma==0):
                    delta_energia=0
                if (somma==-1):
                    delta_energia=spin[casual]*coefj* 2
                                                    

    
                
           
                     #montecarlo.....         
                energia=energia+delta_energia    
                #se il delta è minore di zero è accettato nel caso è maggiore di zero si usa
                #il metodo Metropolis per accettarlo o no
                
                if delta_energia>0:
                     
                    tiro=np.random.uniform(0,1) 
                 
                if tiro>np.exp(-delta_energia/ temperatura):
                    spin[casual]=-spin[casual]
                    energia=energia-delta_energia
                 
     
        
        
        #if (conta_colonna % conta_k)==0:
        #variabili per i grafici 
        aggrego=aggrego+1
          
        magnetizzazione.append(0) 
        mem_temp.append(temperatura)
        
         
        energia_list.append(4*energia/(n_spin))        
        
        for i in range(n_spin):
           
                                  
            magnetizzazione[aggrego]=magnetizzazione[aggrego]+spin[i]            
            if (conta_colonna % conta_k)==0:        
                if spin[i]>0 :
                    plot(i,conta_colonna , 'b.')
                   
                else :
                    plot(i,conta_colonna , 'r.')
                
        magnetizzazione[aggrego]=2*magnetizzazione[aggrego]/n_spin       
    grid(True)
    xlabel('Spin')
    ylabel('Time')
    show()

    plt.figure(figsize=(10,7))        
    plt.xlabel('KT')
    plt.ylabel('Blue <M>, Green <E>')    
    #cv=[0]
   # for i in range(len(energia_list)-1):
    #    cv.append((energia_list[i+1]-energia_list[i])/((mem_temp[1]-mem_temp[0])))     
    plt.plot(mem_temp,magnetizzazione)    
    plt.plot(mem_temp,energia_list)        
   # plt.plot(mem_temp,cv)
    plt.show()
    #print (temperatura)         
 
    
     

                   
                        
         
     

 
 

#tipo_allineamento=raw_input("tipo di allineamento (up,dw,rn)=")
#temperatura_iniziale=input("temperatura iniziale in KT=")
#temperatura_finale=input("temperatura finale in kT=")
#delta_temperatura=input("delta temperatura=")
#numero_iterazioni =input("numero iterazioni=")
#n_spin=input("numero_di_spin=")
tipo_allineamento="rn"
temperatura_iniziale=0.15
temperatura_finale=0.001
delta_temperatura=0.001
numero_iterazioni=10000 #numero di possibilità al cambio spin per la stessa temperatura
n_spin=400#numero di spin nel caso 1D
coefj=0.8*10**(-1) #positiva se ferromagnetico negativo antiferromagnetico
if temperatura_iniziale>temperatura_finale:
    temperatura_iniziale=temperatura_iniziale+delta_temperatura
if temperatura_iniziale<temperatura_finale:
    temperatura_iniziale=temperatura_iniziale-delta_temperatura
k=2 #serve per bloccare il grafico a temperatura_finale-k*delta_temperatura
n_spinx=60  #numero di spin nel caso 2D
n_spiny=60        
conta_k=1 # serve nel 1D disegna nel grafico temporale un set di spin ogni conta_k
 
 
 
#ising_monodimensionale(coefj,delta_temperatura,tipo_allineamento,n_spin,temperatura_iniziale,temperatura_finale,numero_iterazioni,conta_k)   

ising_bidimensionale(coefj,delta_temperatura,tipo_allineamento,n_spinx,n_spiny,temperatura_iniziale,temperatura_finale,numero_iterazioni)
 
