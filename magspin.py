# -*- coding: cp1252 -*-

from visual import *
import time
from math import sqrt
from visual.graph import *

#apertura dei files uno per scrittura e l'altro per lettura
f0=open("dipoli.txt " , "w")
f1=open("dipoli.txt " , "r")
#Dichiarazione variabili
conta=0
z=[]
y=[]
x=[]
vx=[]
vy=[]
vz=[]
dipoli=[] 
campomagneticox=[]
campomagneticoy=[]
campomagneticoz=[]
numero_dipoli=0
numero_dipolix=0
numero_dipoliy=0
massimo_dipoli=0 
densita=0
s1=0
s2=0
j=0
distanza=0
m_0=0.0000001
#m_0=0
m_r=1
delta_mux=0
delta_muy=0
delta_muz=0
dt=0.001
tempo=0
tempofine=1
zoomxfin=0
zoomyfin=0
zoomzfin=0
zoomx=0
zoomy=0
zoomz=0
delta=0
lunghezza=0
altezza=0
larghezza=0
contatore2=-1
supplemento =0
reticolo=[]
zconfig=0 
freccia=[]
coefj=0
alfa=0
interazioni=0
rapporto=0
memvx=[]
memvy=[]
memvz=[]
vf=0
identi=0
indice=0
totalemodulo=0
tantum=0
choose=0
vxx=[]
vyy=[]
vzz=[]
via=0
dimensione=0
valx=0
valy=0
valz=0
val=0
angol=0
angol2=0
segno=0
fatcoefj=0
#print "bla"
#dichiarazione matrici 
reticolo = [ [ [ 0 for t in range(200)] for u in range(200)] for w in range(200)] 
somma_deltax = [ [  0 for t in range(10000)] for u in range(5)]
somma_deltay = [ [  0 for t in range(10000)] for u in range(5)]
somma_deltaz = [ [  0 for t in range(10000)] for u in range(5)]
#fine dichiarazione
oscillation = gdisplay(xtitle='t', ytitle='Mx=verde,My=giallo,Mz=rosso,|M|=azzurro')
 
f2 = gcurve(color=color.cyan) # a graphics curve 
f3 = gcurve(color=color.red) # a graphics curve
f4 = gcurve(color=color.yellow)
f5 = gcurve(color=color.green)
 
      
            
#questa procedura disegna la scatola e relativi assi
def scatola(lunghezza,larghezza,altezza,deltax,deltay,deltaz):
    square = curve(pos=[(0,0,0),(lunghezza/deltax,0,0),(lunghezza/deltax,larghezza/deltay,0),(0,larghezza/deltay,0),(0,0,0)])   
    square = curve(pos=[(0,0,altezza/deltaz),(lunghezza/deltax,0,altezza/deltaz),(lunghezza/deltax,larghezza/deltay,altezza/deltaz),(0,larghezza/deltay,altezza/deltaz),(0,0,altezza/deltaz)])    
    square = curve(pos=[(0,0,altezza/deltaz),(0,0,0)])    
    square = curve(pos=[(0,larghezza/deltay,altezza/deltaz),(0,larghezza/deltay,0)])    
    square = curve(pos=[(lunghezza/deltax,0,altezza/deltaz),(lunghezza/deltax,0,0)])    
    square = curve(pos=[(lunghezza/deltax,larghezza/deltay,altezza/deltaz),(lunghezza/deltax,larghezza/deltay,0)])    
    freccia.append(arrow(pos=(0,0,0), axis=(0,0,altezza/deltaz+1), shaftwidth=0.1, color=color.yellow))
    freccia.append(arrow(pos=(0,0,0), axis=(0,larghezza/deltay+1,0), shaftwidth=0.1, color=color.red))
    freccia.append(arrow(pos=(0,0,0), axis=(lunghezza/deltax+1,0,0), shaftwidth=0.1, color=color.white))

#questa procedura legge i valori calcolati istante per istante per disegnare i dipoli
def lettura_file(contatore,lunghezza,larghezza,altezza,deltax,deltay,deltaz):
    linea1=0
    linea2=0
    linea21=0  
    linea3=0
    linea4=0
    linea5=0
    contatore2=-1
    scatola(lunghezza,larghezza,altezza,deltax,deltay,deltaz)       
    arresto=""
#    arresto=raw_input("premi un qualsiasi bottone per avviare la visualizzazione") 
#forma la lista di dipoli
    for k in range(0,contatore):
         
        dipoli.append(arrow(pos=(x[k],y[k],z[k]), axis=(vx[k],vy[k],vz[k]), shaftwidth=0.1, color=color.green))
#legge nel file e disegna i dipoli essi vengono (graficamente) normalizzati per poterli visualizzare
#    testo = text(pos=(lunghezza/deltax+1,0,0),text="x", align='center', depth=-0.3, color=color.white,height=0.5)
#    testo = text(pos=(0,larghezza/deltay+1,0),text="y", align='center', depth=-0.3, color=color.white,height=0.5)
#    testo = text(pos=(0,0,altezza/deltaz+1),text="z", align='center', depth=-0.3, color=color.white,height=0.5)
    rate(500) 
    list1=[]
    list2=[]
    list21=[]
    list3=[]
    list4=[]
    list5=[]     
    while 1==1:
        contatore2=contatore2+1
        if contatore2>contatore-1:
            contatore2=0 
        linea1=f1.readline()
        if linea1=="*":
            break
        linea2=f1.readline()
        linea21=f1.readline()    
        linea3=f1.readline()
        linea4=f1.readline()
        linea5=f1.readline()
        list1.append(linea1)
        list2.append(linea2)
        list21.append(linea21)
        list3.append(linea3)
        list4.append(linea4)
        list5.append(linea5)     
    c=-1
    #print "list2"   
   # print len(list2)
    for el in list2:
        #print c
        c+=1
        if c>contatore-1:
            c=0 
 
        dipoli[c].pos.x=float(list1[c])
        dipoli[c].pos.y=float(list2[c])
        dipoli[c].pos.z=float(list21[c])
    c=-1
    c2=-1    
 
    while 1==1:
        rate(100)
        c2+=1
        c+=1
        if c>contatore-1:
            c=0 
        #print c 
        
        try: 
            dipoli[c].axis.x=float(list3[c2])/(9*10**-24)
            dipoli[c].axis.y=float(list4[c2])/(9*10**-24) 
            dipoli[c].axis.z=float(list5[c2])/(9*10**-24) 
        except:
            break
        #time.sleep(0.001)         
    
def prodotto_vettoriale(i,valx,valy,valz,valx2,valy2,valz2):

    delta_mux=valy*valz2-valz*valy2
    delta_muy=-valx*valz2+valz*valx2
    delta_muz=valx*valy2-valy*valx2

    return delta_mux,delta_muy,delta_muz            

def dipolo_classico3d():

    def moto_dipoli3d(conta_tantum,choose,fatcoefj,Bz):
        rate(10) 
       
        
 
     #qui memomrizzo tutti i valori dei momenti magnetici in modo da poterli usare nei calcoli
        for j in range(0,int(numero_dipoli)):
              memvx[j]=vx[j]
              memvy[j]=vy[j]
              memvz[j]=vz[j]
        #calcolo lo spostamento di ogni singolo dipolo per istante            
        for i in range(0,int(numero_dipoli)):
             #interazione dipolo-dipolo     
              delta_mux,delta_muy,delta_muz=prodotto_vettoriale(i,vx[i],vy[i],vz[i],campomagneticox[i],campomagneticoy[i],campomagneticoz[i]);
             #metodo eulero esplicito impostato
             #**************************************************
              
              somma_deltax[choose][i]=delta_mux*float(interazioni[0:1])
              somma_deltay[choose][i]=delta_muy*float(interazioni[0:1])
              somma_deltaz[choose][i]=delta_muz*float(interazioni[0:1])
               
             
             #***************************************************
             
             #questo sotto è il coefficiente J     
              coefj=((m_0)*10**(-48)*81)/(deltax**alfa2)*fatcoefj

              delta_mux=0
              delta_muy=0
              delta_muz=0
              s_deltax=0
              s_deltay=0
              s_deltaz=0
              #**********seconda interazione quella isotropica
              #**********calcolo lo spostamento dovuto a questa interazione sul dipolo considerato
              
              for k in range(0,int(numero_dipoli)):
                    #*********normalizzo il dipolo considerato
                    valx=memvx[i]/(9*10**-24)
                    valy=memvy[i]/(9*10**-24)
                    valz=memvz[i]/(9*10**-24)
                              
                    if k!=i:
                          #**********normalizzo gli altri dipoli circostanti                            
                            
                          valx2=memvx[k]/(9*10**-24)
                          valy2=memvy[k]/(9*10**-24)
                          valz2=memvz[k]/(9*10**-24)
                          #*******print(vx[k])
                          #*******calcolo il secondo termine dell'equazione del moto
                          delta_mux,delta_muy,delta_muz=prodotto_vettoriale(i,valx,valy,valz,valx2,valy2,valz2)
   
                          distanza=sqrt(((x[i]-x[k])*deltax)*((x[i]-x[k])*deltax)+((y[i]-y[k])*deltay)*((y[i]-y[k])*deltay)+((z[i]-z[k])*deltaz)*((z[i]-z[k])*deltaz))
                          #****mi rimetto a distanze unitarie  
                          distanza=distanza/(deltax)
                          #*****calcolo gli spostamenti derivati dalla seconda interazione     
                          s_deltax=delta_mux*coefj*float(interazioni[1:2])/(distanza**alfa)+s_deltax
                          s_deltay=delta_muy*coefj*float(interazioni[1:2])/(distanza**alfa)+s_deltay
                          s_deltaz=delta_muz*coefj*float(interazioni[1:2])/(distanza**alfa)+s_deltaz
                           
                          #******ritorno ai valori nominali    
                           
 
              if float(interazioni[1:2])==1:
                    somma_deltax[choose][i]=somma_deltax[choose][i]+s_deltax
                    somma_deltay[choose][i]=somma_deltay[choose][i]+s_deltay
                    somma_deltaz[choose][i]=somma_deltaz[choose][i]+s_deltaz
                            
# pezzo con aggiunta campo magnetico***********************************************************
              delta_mux,delta_muy,delta_muz=prodotto_vettoriale(i,valx,valy,valz,0,0,Bz)

              s_deltax=delta_mux*coefj*float(interazioni[1:2])+s_deltax
              s_deltay=delta_muy*coefj*float(interazioni[1:2])+s_deltay
              s_deltaz=delta_muz*coefj*float(interazioni[1:2])+s_deltaz
 
              somma_deltax[choose][i]=somma_deltax[choose][i]+s_deltax
              somma_deltay[choose][i]=somma_deltay[choose][i]+s_deltay
              somma_deltaz[choose][i]=somma_deltaz[choose][i]+s_deltaz
 
 #*******************************************************

             #*****terza interazione Exchange******
              s_deltax=0
              s_deltay=0
              s_deltaz=0
              for k in range(0,int(numero_dipoli)):
   
                    valx=memvx[i]/(9*10**-24)
                    valy=memvy[i]/(9*10**-24)
                    valz=memvz[i]/(9*10**-24)
                              
                    if k!=i:
                          valx2=memvx[k]/(9*10**-24)
                          valy2=memvy[k]/(9*10**-24)
                          valz2=memvz[k]/(9*10**-24)
                   
        #dalla analisi dell'hamiltoniana e dal ricavare un campo magnetico associato il risultato del termine è il seguente                   
                          delta_mux,delta_muy,delta_muz=prodotto_vettoriale(i,valx,valy,valz,0,0,valz2)
   
                          distanza=sqrt(((x[i]-x[k])*deltax)*((x[i]-x[k])*deltax)+((y[i]-y[k])*deltay)*((y[i]-y[k])*deltay)+((z[i]-z[k])*deltaz)*((z[i]-z[k])*deltaz))
                          distanza=distanza/(deltax)
       #stesso calcolo di prima aggiunto il rapporto                              
                          s_deltax=delta_mux*coefj*rapporto*float(interazioni[2:3])/(distanza**alfa)+s_deltax
                          s_deltay=delta_muy*coefj*rapporto*float(interazioni[2:3])/(distanza**alfa)+s_deltay
                          s_deltaz=delta_muz*coefj*rapporto*float(interazioni[2:3])/(distanza**alfa)+s_deltaz
                             
              if float(interazioni[2:3])==1:
                    somma_deltax[choose][i]=somma_deltax[choose][i]+s_deltax
                    somma_deltay[choose][i]=somma_deltay[choose][i]+s_deltay
                    somma_deltaz[choose][i]=somma_deltaz[choose][i]+s_deltaz
                     
# pezzo con aggiunta campo magnetico***********************************************************
              delta_mux,delta_muy,delta_muz=prodotto_vettoriale(i,valx,valy,valz,0,0,Bz)
  
               
              s_deltax=delta_mux*coefj*rapporto*float(interazioni[2:3])+s_deltax
              s_deltay=delta_muy*coefj*rapporto*float(interazioni[2:3])+s_deltay
              s_deltaz=delta_muz*coefj*rapporto*float(interazioni[2:3])+s_deltaz
 

  
              somma_deltax[choose][i]=somma_deltax[choose][i]+s_deltax
              somma_deltay[choose][i]=somma_deltay[choose][i]+s_deltay
              somma_deltaz[choose][i]=somma_deltaz[choose][i]+s_deltaz
 
 #*******************************************************

   
            
         
#calcola il campo su ogni dipolo          

    def calcolo_campo3d():
       versx=0
       versy=0
       versz=0
       c=-1 
       prodotto_scalare=0
       tt=0
       
#azzera ogni volta i campi sui dipoli
       for tt in range(0,int(numero_dipoli)):
             campomagneticox[tt]= 0
             campomagneticoy[tt]= 0
             campomagneticoz[tt]= 0
#calcola al tempo t tutti i campi magnetici da dipoli che agiscono su singolo dipolo       
       for j in range(0,int(numero_dipoli)):
              
            
           for i in range(0,int(numero_dipoli)):
              # print(i)   
               if i!=j:
         
                   distanza=sqrt(((x[j]-x[i])*deltax)*((x[j]-x[i])*deltax)+((y[j]-y[i])*deltay)*((y[j]-y[i])*deltay)+((z[j]-z[i])*deltaz)*((z[j]-z[i])*deltaz))
                   versx=(x[i]-x[j])*deltax/distanza
                   versy=(y[i]-y[j])*deltay/distanza
                   versz=(z[i]-z[j])*deltaz/distanza                         
                   prodotto_scalare=vx[i]*versx+vy[i]*versy+vz[i]*versz

                   campomagneticox[j]=m_r*m_0*(3*prodotto_scalare*versx-vx[i])/(distanza*distanza*distanza)+campomagneticox[j]                        
                   campomagneticoy[j]=m_r*m_0*(3*prodotto_scalare*versy-vy[i])/(distanza*distanza*distanza)+campomagneticoy[j]                                           
                   campomagneticoz[j]=m_r*m_0*(3*prodotto_scalare*versz-vz[i])/(distanza*distanza*distanza)+campomagneticoz[j]

           campomagneticoz[j]=campomagneticoz[j]+Bz 
          # print Bz
           #print campomagneticoz[j]
                   
     
       
       #if (conta_tantum2==tantum) :
    #dati di ingresso  
    lunghezza=input("Lenght in nm=")
    larghezza=input("Height in nm=")
    altezza=input("Width in nm=")  
    

   # delta=input("inserisci la differenza spaziale della griglia =")
    densita=input("inserisci la densità =")
   # zoomx=input("inserisci x punto finestra iniziale =")
   # zoomy=input("inserisci y punto finestra iniziale =")
   # zoomz=input("inserisci z punto finestra iniziale =")
   # zoomxfin=input("inserisci x punto finestra finale =")
   # zoomyfin=input("inserisci y punto finestra finale =")
   # zoomzfin=input("inserisci z punto finestra finale =")
    dt=input("dt step in seconds=")
    tempofine=input("stop time in seconds=")
    alfa=input("exponential coefficient spin-spin (you can put 1)=")
    fatcoefj=input("coefj(you can put 1)=")
    rapporto=input("D=coef*J (you can put 1) =")
    interazioni=raw_input("Insert interaction you want on(dipol-dipol,exchange,isotropic) (111 for all, 000 for nothing)=")
    tantum=input("Number frames for calculation (you can put 1)=")
    Bz=input("Static magnetic field in Z direction(you can put 0)=")
    #interazioni="123"
    #print(interazioni[0:1])
    zconfig=raw_input("z to have every dipols on Z direction, m to half-half Z direction,p perturbated in light way in Z,X to have the dipols in x direction,b in  xz direction=")
    dimensione=input("dimension of the system")
    dimensione=float(dimensione)
    tantum=float(tantum)
    
 #parte nel caso volessimo fissare i dati di ingresso      
 #   lunghezza=0.1*4
 #   larghezza=0.1*4
 #   altezza=0.1*4
   
    delta=0.1
 #   densita=1
    alfa=3
    alfa2=3
    zoomx=0
    zoomy=0
    zoomz=0
    zoomxfin=lunghezza
    zoomyfin=larghezza
    zoomzfin=altezza
  #  rapporto=1
  #  interazioni="111"
  #  tantum=1
    
    #supplemento=0
    #m_r=1
  #  tempofine=0.5
  #  dt=0.04
    #dimensione=3 
   # dt=float(dt/1000)

    lunghezza=lunghezza*10**-9
    larghezza=larghezza*10**-9
    altezza=altezza*10**-9
    delta=delta*10**-9      
    deltax=delta
    deltay=delta
    deltaz=delta
    zoomx=zoomx*10**-9
    zoomy=zoomy*10**-9
    zoomz=zoomz*10**-9
    zoomxfin=zoomxfin*10**-9
    zoomyfin=zoomyfin*10**-9
    zoomzfin=zoomzfin*10**-9
    
    
    


    #calcola il numero di dipoli  
    numero_dipoli=(lunghezza)*(larghezza)*(altezza)/(deltax*deltay*deltaz)*densita
    numero_dipolix=lunghezza/(deltax)
    numero_dipoliy=larghezza/(deltay)
    numero_dipoliz=altezza/(deltaz)
    if dimensione==1:
        numero_dipoli=numero_dipolix
    if dimensione==2:
        numero_dipoli=numero_dipoliy*numero_dipoliz
        
        
        
    
    print(int(numero_dipoli))
    totalemodulo=numero_dipoli
    contatore=0
    ii=0
    jj=0
    c=-1
    i=-1
  #riempie il reticolo di dipoli con norma uguale al magnetone di Bohr
    for j in range(0,int(numero_dipoli)):
              memvx.append(0)
              memvy.append(0)
              memvz.append(0)
        
    while (i <int(numero_dipoli)):

        
        ii=random.randint(0,int(lunghezza/deltax)+1)
        jj=random.randint(0,int(larghezza/deltay)+1)
        kk=random.randint(0,int(altezza/deltaz)+1)
        if dimensione==1:
            kk=int(altezza/(2*deltaz))
            jj=int(larghezza/(2*deltay))
        if dimensione==2:
            kk=int(altezza/(2*deltaz))
            
        
      
        if (reticolo[ii][jj][kk]==0):
             
            i=i+1
            #print(i)    
            reticolo[ii][jj][kk]=1
            x.append(ii)
            y.append(jj) 
            z.append(kk) 
            vx.append(random.random()/2)
            vy.append(random.random()/2)
            vz.append(0)
            s1=random.randint(1,3)
             
            campomagneticox.append(0)
            campomagneticoy.append(0)
            campomagneticoz.append(0)        
            
            if s1==1:
                vx[i]=vx[i]
                vy[i]=vy[i]
                
                vz[i]=sqrt(1-(vx[i]*vx[i]+vy[i]*vy[i]))*(-9*10**(-24))
                vx[i]=vx[i]*(-9*10**(-24))
                vy[i]=vy[i]*(-9*10**(-24))

            if s1==2:
                vx[i]=-vx[i]
                vy[i]=-vy[i]
                vz[i]=-sqrt(1-(vx[i]*vx[i]+vy[i]*vy[i]))*(-9*10**(-24))
                vx[i]=vx[i]*(-9*10**(-24))
                vy[i]=vy[i]*(-9*10**(-24))


            if (zconfig=='p'):

                angol=random.randint(1,60)
                angol2=random.randint(1,60)
                val=random.randint(0,2)
                segno=random.randint(1,3)
                vx[i]=0
                vy[i]=0
                vz[i]=9*10**-24
                if (segno==2):
                    segno=-1
                if (val==0):
                   # print(angol)
                    vx[i]=float(float(angol)/100)
                    #print(vx[i])
                    vy[i]=float(angol2/100)
                    vz[i]=float(sqrt(1-vx[i]**2-vy[i]**2))
                    vx[i]=vx[i]*9*10**-24*segno
                    vy[i]=vy[i]*9*10**-24*segno
                    vz[i]=vz[i]*9*10**-24
 
            if (zconfig=='z'):
                vx[i]=0
                vy[i]=0
                vz[i]=9*10**-24
            if (zconfig=='x'):
                vx[i]=9*10**-24
                vy[i]=0
                vz[i]=0

            if (zconfig=='b'):
                vx[i]=4.5*10**-24
                vy[i]=0
                vz[i]=4.5*10**-24


            if (zconfig=='m') and (i<=int(numero_dipoli/2)):
                vx[i]=0
                vy[i]=0
                vz[i]=9*10**-24
            if (zconfig=='m') and (i>int(numero_dipoli/2)):                
                vx[i]=0
                vy[i]=0
                vz[i]=-9*10**-24

            if ((z[i]>=zoomz/deltaz) and (x[i]>=zoomx/deltax) and (y[i]>=zoomy/deltay) and (x[i]<=zoomxfin/deltax+1) and (y[i]<=zoomyfin/deltay+1) and (z[i]<=zoomzfin/deltaz+1)):
 
              
                contatore=contatore+1
    totalemodulo=0 
   
    
    tempo=0
    #inizia il calcolo  
    conta_tantum2=0
    conta_tantum=0
    choose=0
    contatore2=-1
    for r in range(0,int(numero_dipoli)):

            somma_deltax[0][r]=0                   
            somma_deltay[0][r]=0
            somma_deltaz[0][r]=0
            somma_deltax[1][r]=0                   
            somma_deltay[1][r]=0
            somma_deltaz[1][r]=0
            somma_deltax[2][r]=0                   
            somma_deltay[2][r]=0
            somma_deltaz[2][r]=0

            vxx.append(0)
            vyy.append(0)
            vzz.append(0)
            #print(vxx[r])
    while (tempo<tempofine):
        #via=0     
        conta_tantum=conta_tantum+1
        for r in range(0,int(numero_dipoli)):
            vxx[r]=vx[r]
            vyy[r]=vy[r]
            vzz[r]=vz[r]
 
        dt=dt/2
      #  print(dt)
        if (float(interazioni[0:1])==1):
             
            calcolo_campo3d() #calcoli il c1 in fn       
        for j in range(0,int(numero_dipoli)):
            campomagneticoz[j]=campomagneticoz[j]+Bz 

        choose=0
        moto_dipoli3d(conta_tantum,choose,fatcoefj,Bz)  
 
        for r in range(0,int(numero_dipoli)):
            vx[r]=vxx[r]+somma_deltax[choose][r]*dt
            vy[r]=vyy[r]+somma_deltay[choose][r]*dt
            vz[r]=vzz[r]+somma_deltaz[choose][r]*dt            
        
     
        #calcolo il campo magnetico solo nell'interazione dipolo dipolo           
        if (float(interazioni[0:1])==1):
            calcolo_campo3d()        
        choose=1
        

 
        moto_dipoli3d(conta_tantum,choose,fatcoefj,Bz) #calcola i c2

        for r in range(0,int(numero_dipoli)):
            vx[r]=vxx[r]+somma_deltax[choose][r]*dt
            vy[r]=vyy[r]+somma_deltay[choose][r]*dt
            vz[r]=vzz[r]+somma_deltaz[choose][r]*dt            
        
        choose=2
        if (float(interazioni[0:1])==1):
             calcolo_campo3d()        
 
        moto_dipoli3d(conta_tantum,choose,fatcoefj,Bz) #calcola i c3
       
        dt=2*dt
        for r in range(0,int(numero_dipoli)):

            vx[r]=vxx[r]+somma_deltax[choose][r]*dt
            vy[r]=vyy[r]+somma_deltay[choose][r]*dt
            vz[r]=vzz[r]+somma_deltaz[choose][r]*dt            
      
         
        choose=3
        if (float(interazioni[0:1])==1):
            calcolo_campo3d()        
 

        moto_dipoli3d(conta_tantum,choose,fatcoefj,Bz) #calcola i c4
        kk=0
        energia=0
        magx=0
        magy=0
        magz=0
   
        #grafico delle grandezze interessate
       
       
      
      
        for r in range(0,int(numero_dipoli)):
            vx[r]=vxx[r]+dt/6*(somma_deltax[0][r]+2*somma_deltax[1][r]+2*somma_deltax[2][r]+somma_deltax[3][r])                       
            vy[r]=vyy[r]+dt/6*(somma_deltay[0][r]+2*somma_deltay[1][r]+2*somma_deltay[2][r]+somma_deltay[3][r])                       
            vz[r]=vzz[r]+dt/6*(somma_deltaz[0][r]+2*somma_deltaz[1][r]+2*somma_deltaz[2][r]+somma_deltaz[3][r])                                                                     
            
            magx=magx+vx[r]
            magy=magy+vy[r]
            magz=magz+vz[r]
                        
            if (conta_tantum==tantum):    
             #scrive nel file solo i dipoli nella finestra interessata
                   
                if ((z[r]>=zoomz/deltaz) and (x[r]>=zoomx/deltax) and (y[r]>=zoomy/deltay) and (x[r]<=zoomxfin/deltax+1) and (y[r]<=zoomyfin/deltay+1) and (z[r]<=zoomzfin/deltaz+1)):
                                 
                    contatore2=contatore2+1
                    f0.write(str(x[r])+"\n")
                    f0.write(str(y[r])+"\n")
                    f0.write(str(z[r])+"\n")
                    f0.write(str(vx[r])+"\n")
                    f0.write(str(vy[r])+"\n")
                    f0.write(str(vz[r])+"\n")
                                                 
            
        f2.plot(pos=(tempo,sqrt((magx**2+magy**2+magz**2))/(numero_dipoli*9*10**-24))) # plot 
        f3.plot(pos=(tempo,(magz)/(numero_dipoli*9*10**-24)))# plot
        f4.plot(pos=(tempo,(magy)/(numero_dipoli*9*10**-24)))# plot
        f5.plot(pos=(tempo,(magx)/(numero_dipoli*9*10**-24)))# plot

        tempo=tempo+dt
        
        if conta_tantum==tantum:
            conta_tantum=0
    totalemodulo=0  
    for i in range(0,int(numero_dipoli)):
             totalemodulo=totalemodulo+sqrt(vx[i]*vx[i]+vy[i]*vy[i]+vz[i]*vz[i])
    #print("scrivo")  
    print(totalemodulo/(9*10**-(24)))
     
    
    f0.write("*")
    f0.close()
    #legge i dipoli nel file
     
    lettura_file(contatore,lunghezza,larghezza,altezza,deltax,deltay,deltaz)
    f1.close()
              
          
          
    
    
    
#print "OK"

dipolo_classico3d();

 
