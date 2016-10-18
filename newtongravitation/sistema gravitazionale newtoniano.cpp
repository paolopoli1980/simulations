//programma di simulazione con confronto metodi di un campo a potenziale 
//gravitazionale.

#include<conio.h>
#include<stdio.h>
#include<math.h>
#include<iostream> 
#include <stdlib.h>
#include<time.h>

//#include<iostream.h>

double x[10],y[10],z[10],dt,ax[10],ay[10],az[10],massa[10],xp[5][10],yp[5][10],zp[5][10],distanza_origine[10];
double vvx,vvy,vvz,t,xx[10],yy[10],zz[10],vx[10],vy[10],vz[10],n,limt,vpx[5][10],vpy[5][10],vpz[5][10],apx[5][10],apy[5][10],apz[5][10];
double distx,disty,distz,energia[10],energia_potenziale[10],passimo_massimo,tolleranza;
 
double aax,aay,aaz; 
double rx[5],ry[5],rz[5],axx[8][10],ayy[8][10],azz[8][10],vxx[8][10],vyy[8][10],vzz[8][10],dtt[10];
double idrk4,passo_massimo,tol,erx[10],ery[10],erz[10],err[10],passo_minimo;  

double  px[6][10],py[6][10],pz[6][10];
double delta[10]; 
float startime,endtime,diff;
int id2;  

int kk,kk2,contatore,numero_punti,numero_scelta,numero_masse_movimento,contatore2,contatore_interno;
int conta_ciclo,cc,id,step_energia,conta_step[10],conta_step2[10],step_posizione;
int valore; 

void inserimento_dati();
void eulero();
void Adams_bashforth2();
void rk4();
void heun();
 


 
void calcola_accelerazione();
void scrivi_file();
void chiusura_files();
void crea_file();
void calcola_accelerazione_parziale();




FILE *velocita0;
FILE*posizione0; 
FILE*masse0;
FILE*energy0;
FILE*distanza0;

FILE *velocita1;
FILE*posizione1; 
FILE*masse1;
FILE*energy1;
FILE*distanza1;

FILE *velocita2;
FILE*posizione2; 
FILE*masse2;
FILE*energy2;
FILE*distanza2;

FILE *velocita3;
FILE*posizione3; 
FILE*masse3;
FILE*energy3;
FILE*distanza3;

FILE *velocita4;
FILE*posizione4; 
FILE*masse4;
FILE*energy4;
FILE*distanza4;

FILE *velocita5;
FILE*posizione5; 
FILE*masse5;
FILE*energy5;
FILE*distanza5;

FILE *velocita6;
FILE*posizione6; 
FILE*masse6;
FILE*energy6;
FILE*distanza6;

FILE *velocita7;
FILE*posizione7; 
FILE*masse7;
FILE*energy7;
FILE*distanza7;

FILE *velocita8;
FILE*posizione8; 
FILE*masse8;
FILE*energy8;
FILE*distanza8;

FILE *velocita9;
FILE*posizione9; 
FILE*masse9;
FILE*energy9;
FILE*distanza9;

FILE*masse_fisse;
//Creazione dei files di salvataggio
//*********************
//*********************
//*********************
void crea_file()
{
      masse_fisse = fopen("massefisse.txt", "w");    
      
      velocita0 = fopen ("velocita0.txt", "w"); 
      posizione0 = fopen("posizione0.txt","w");
      energy0=fopen("energia0.txt","w");
      distanza0=fopen("distanza0.txt","w");

      velocita1 = fopen ("velocita1.txt", "w"); 
      posizione1 = fopen("posizione1.txt","w");
      energy1=fopen("energia1.txt","w");
      distanza1=fopen("distanza1.txt","w");
       
      velocita2 = fopen ("velocita2.txt", "w"); 
      posizione2 = fopen("posizione2.txt","w");
      energy2=fopen("energia2.txt","w");
      distanza2=fopen("distanza2.txt","w");
  
      velocita3 = fopen ("velocita3.txt", "w"); 
      posizione3 = fopen("posizione3.txt","w");
      energy3=fopen("energia3.txt","w");
      distanza3=fopen("distanza3.txt","w");

      velocita4 = fopen ("velocita4.txt", "w"); 
      posizione4 = fopen("posizione4.txt","w");
      energy4=fopen("energia4.txt","w");
      distanza4=fopen("distanza4.txt","w");

      velocita5 = fopen ("velocita5.txt", "w"); 
      posizione5 = fopen("posizione5.txt","w");
      energy5=fopen("energia5.txt","w");
      distanza5=fopen("distanza5.txt","w");

      velocita6 = fopen ("velocita6.txt", "w"); 
      posizione6 = fopen("posizione6.txt","w");
      energy6=fopen("energia6.txt","w");
      distanza6=fopen("distanza6.txt","w");

      velocita7 = fopen ("velocita7.txt", "w"); 
      posizione7 = fopen("posizione7.txt","w");
      energy7=fopen("energia7.txt","w");
      distanza7=fopen("distanza7.txt","w");
      
      velocita8 = fopen ("velocita8.txt", "w"); 
      posizione8 = fopen("posizione8.txt","w");
      energy8=fopen("energia8.txt","w");
      distanza8=fopen("distanza8.txt","w");
      
      velocita9 = fopen ("velocita9.txt", "w"); 
      posizione9 = fopen("posizione9.txt","w");
      energy9=fopen("energia9.txt","w");
      distanza9=fopen("distanza9.txt","w");
}                  
//*************************
//*************************
//*************************


//*1*scrittura dei dati nei files
//****************************
//****************************
//****************************

void scrivi_file()

{ int id2;
 
      
     if (contatore==0)
     {
         conta_step[0]++;                           
         conta_step2[0]++;
         if (conta_step2[0]==step_posizione)         
         {
       //  printf("scirvo");
         
         fprintf(velocita0,"%.20lf\n",vx[contatore]);
         fprintf(posizione0,"%.20lf\n",x[contatore]);
         fprintf(velocita0,"%.20lf\n",vy[contatore]);
         fprintf(posizione0,"%.20lf\n",y[contatore]);
         fprintf(velocita0,"%.20lf\n",vz[contatore]);
         fprintf(posizione0,"%.20lf\n",z[contatore]);
         conta_step2[0]=0;
         }
         
         if (conta_step[0]==step_energia)         
         {
  
            fprintf(energy0,"%.20lf\n",energia[contatore]);
            fprintf(distanza0,"%.20lf\n",distanza_origine[contatore]);
            conta_step[0]=0;
 
         } 
         } 

         if (contatore==1)
         {
         conta_step[1]++;          
         conta_step2[1]++;
         if (conta_step2[1]==step_posizione)
         {
         fprintf(velocita1,"%.20lf\n",vx[contatore]);
         fprintf(posizione1,"%.20lf\n",x[contatore]);
         fprintf(velocita1,"%.20lf\n",vy[contatore]);
         fprintf(posizione1,"%.20lf\n",y[contatore]);
         fprintf(velocita1,"%.20lf\n",vz[contatore]);
         fprintf(posizione1,"%.20lf\n",z[contatore]);
         conta_step2[1]=0;         
         }
         if (conta_step[1]==step_energia)         
         {
            fprintf(energy1,"%.20lf\n",energia[contatore]);
            fprintf(distanza1,"%.20lf\n",distanza_origine[contatore]);
            conta_step[1]=0; 
         } 
         } 


      if (contatore==2)
      { 
         conta_step[2]++;              
         conta_step2[2]++;
         if (conta_step2[2]==step_posizione)
         {
         
         fprintf(velocita2,"%.20lf\n",vx[contatore]);
         fprintf(posizione2,"%.20lf\n",x[contatore]);
         fprintf(velocita2,"%.20lf\n",vy[contatore]);
         fprintf(posizione2,"%.20lf\n",y[contatore]);
         fprintf(velocita2,"%.20lf\n",vz[contatore]);
         fprintf(posizione2,"%.20lf\n",z[contatore]);
         conta_step2[2]=0;
         }
          if (conta_step[2]==step_energia)         
         {
            fprintf(energy2,"%.20lf\n",energia[contatore]);
            fprintf(distanza2,"%.20lf\n",distanza_origine[contatore]);
            conta_step[2]=0;
         } 
         } 

      if (contatore==3)
      {
         conta_step[3]++; 
         conta_step2[3]++;    
         if (conta_step2[3]==step_posizione)
         {
         fprintf(velocita3,"%.20lf\n",vx[contatore]);
         fprintf(posizione3,"%.20lf\n",x[contatore]);
         fprintf(velocita3,"%.20lf\n",vy[contatore]);
         fprintf(posizione3,"%.20lf\n",y[contatore]);
         fprintf(velocita3,"%.20lf\n",vz[contatore]);
         fprintf(posizione3,"%.20lf\n",z[contatore]);
         conta_step2[3]=0;
         
         }
         
          if (conta_step[3]==step_energia)         
         {
            fprintf(energy3,"%.20lf\n",energia[contatore]);
            fprintf(distanza3,"%.20lf\n",distanza_origine[contatore]);
            conta_step[3]=0;
         } 
         }

       if (contatore==4)
       {
         conta_step[4]++;
         conta_step2[4]++;
         if (conta_step2[4]==step_posizione)
         {
         
         fprintf(velocita4,"%.20lf\n",vx[contatore]);
         fprintf(posizione4,"%.20lf\n",x[contatore]);
         fprintf(velocita4,"%.20lf\n",vy[contatore]);
         fprintf(posizione4,"%.20lf\n",y[contatore]);
         fprintf(velocita4,"%.20lf\n",vz[contatore]);
         fprintf(posizione4,"%.20lf\n",z[contatore]);
         conta_step2[4]=0;         
         }
          if (conta_step[4]==step_energia)         
         {
            fprintf(energy4,"%.20lf\n",energia[contatore]);
            fprintf(distanza4,"%.20lf\n",distanza_origine[contatore]);
            conta_step[4]=0;
         } 
         }

       if (contatore==5)
       {
         conta_step[5]++;
         conta_step2[5]++;
         if (conta_step2[5]==step_posizione)
         {
         
         fprintf(velocita5,"%.20lf\n",vx[contatore]);
         fprintf(posizione5,"%.20lf\n",x[contatore]);
         fprintf(velocita5,"%.20lf\n",vy[contatore]);
         fprintf(posizione5,"%.20lf\n",y[contatore]);
         fprintf(velocita5,"%.20lf\n",vz[contatore]);
         fprintf(posizione5,"%.20lf\n",z[contatore]);
         conta_step2[5]=0;
         }
          if (conta_step[5]==step_energia)         
         {
            fprintf(energy5,"%.20lf\n",energia[contatore]);
            fprintf(distanza5,"%.20lf\n",distanza_origine[contatore]);
            conta_step[5]=0;
         } 
         }

       if (contatore==6)
       {
         conta_step[6]++;
         conta_step2[6]++;
         if (conta_step2[6]==step_posizione)
         {        
         fprintf(velocita6,"%.20lf\n",vx[contatore]);
         fprintf(posizione6,"%.20lf\n",x[contatore]);
         fprintf(velocita6,"%.20lf\n",vy[contatore]);
         fprintf(posizione6,"%.20lf\n",y[contatore]);
         fprintf(velocita6,"%.20lf\n",vz[contatore]);
         fprintf(posizione6,"%.20lf\n",z[contatore]);
         conta_step2[6]=0;         
         }
         if (conta_step[6]==step_energia)         
         {
            fprintf(energy6,"%.20lf\n",energia[contatore]);
            fprintf(distanza6,"%.20lf\n",distanza_origine[contatore]);            
            conta_step[6]=0;
         } 
         }

        if (contatore==7)
        {
          conta_step[7]++;
          conta_step2[7]++;
          if (conta_step2[7]=step_posizione)         
          {
          fprintf(velocita7,"%.20lf\n",vx[contatore]);
          fprintf(posizione7,"%.20lf\n",x[contatore]);
          fprintf(velocita7,"%.20lf\n",vy[contatore]);
          fprintf(posizione7,"%.20lf\n",y[contatore]);
          fprintf(velocita7,"%.20lf\n",vz[contatore]);
          fprintf(posizione7,"%.20lf\n",z[contatore]);
          conta_step2[7]=0;         
          }
          
         if (conta_step[7]==step_energia)         
         {
            fprintf(energy7,"%.20lf\n",energia[contatore]);
            fprintf(distanza7,"%.20lf\n",distanza_origine[contatore]);            
            conta_step[7]=0;
         } 
         }

        if (contatore==8)
        {
          conta_step[8]++;
          conta_step2[8]++;
          if (conta_step2[8]=step_posizione)         
          {
          
          fprintf(velocita8,"%.20lf\n",vx[contatore]);
          fprintf(posizione8,"%.20lf\n",x[contatore]);
          fprintf(velocita8,"%.20lf\n",vy[contatore]);
          fprintf(posizione8,"%.20lf\n",y[contatore]);
          fprintf(velocita8,"%.20lf\n",vz[contatore]);
          fprintf(posizione8,"%.20lf\n",z[contatore]);
          conta_step2[8]=0;         
          }
         if (conta_step[8]==step_energia)         
         {
            fprintf(energy8,"%.20lf\n",energia[contatore]);
            fprintf(distanza8,"%.20lf\n",distanza_origine[contatore]);            
            conta_step[8]=0;
         } 
         }

        if (contatore==9)
        {
          conta_step[9]++;
          conta_step2[9]++;
          if (conta_step2[9]=step_posizione)         
          {

          fprintf(velocita9,"%.20lf\n",vx[contatore]);
          fprintf(posizione9,"%.20lf\n",x[contatore]);
          fprintf(velocita9,"%.20lf\n",vy[contatore]);
          fprintf(posizione9,"%.20lf\n",y[contatore]);
          fprintf(velocita9,"%.20lf\n",vz[contatore]);
          fprintf(posizione9,"%.20lf\n",z[contatore]);
          conta_step2[9]=0;         
          }
         
         if (conta_step[9]==step_energia)         
         {
            fprintf(energy9,"%.20lf\n",energia[contatore]);
            fprintf(distanza9,"%.20lf\n",distanza_origine[contatore]);            
            conta_step[9]=0;
         } 
         }
   
 }

//*****************
//*****************
//*****************

//Chiusura dei files aperti
//*****************
//*****************
//*****************
void chiusura_files()
{
     fclose (velocita0);
     fclose (posizione0);
     fclose(energy0);
     fclose(distanza0);

     fclose (velocita1);
     fclose (posizione1);                            
     fclose(energy1);
     fclose(distanza1);
     
     fclose (velocita2);
     fclose (posizione2);
     fclose(energy2);
     fclose(distanza2);
     
     fclose (velocita3);
     fclose (posizione3);
     fclose(energy3);
     fclose(distanza3);
     
     fclose (velocita4);
     fclose (posizione4);
     fclose(energy4);
     fclose(distanza4);
     
     fclose (velocita5);
     fclose (posizione5);
     fclose(energy5);
     fclose(distanza5);
     
     fclose (velocita6);
     fclose (posizione6);
     fclose(energy6);
     fclose(distanza6);
     
     fclose (velocita7);
     fclose (posizione7);
     fclose(energy7);
     fclose(distanza7);
        
     fclose (velocita8);
     fclose (posizione8);
     fclose(energy8);
     fclose(distanza8);    
     
     fclose (velocita9);
     fclose (posizione9);
     fclose(energy9);
     fclose(distanza9);
}

//*****************
//*****************
//*****************




int main()

{
                 
crea_file();
inserimento_dati();
 
}                          


//Parte riguardante il calcolo
//***********
//***********


 
void calcola_accelerazione()
{
//questa calcola l'accelerazione per eulero e adam-bashfort2,anche se per
//quest'ultimo in fondo sono state messe delle condizioni in più
 
   for (contatore2=0;contatore2<numero_masse_movimento;contatore2=contatore2+1)
   {
       ax[contatore2]=0;
       ay[contatore2]=0;
       az[contatore2]=0;
       
       energia_potenziale[contatore2]=0;
    
    for (contatore=0;contatore<numero_punti;contatore=contatore+1)
    {
     
       if (contatore2!=contatore)
       {      
          distx=(-x[contatore2]+x[contatore]);
          disty=(-y[contatore2]+y[contatore]);
          distz=(-z[contatore2]+z[contatore]);

//calcolo l'accelerazione sul punto in movimento

          ax[contatore2]=ax[contatore2]+(massa[contatore]*distx)/((distx*distx+disty*disty+distz*distz)*sqrt(distx*distx+disty*disty+distz*distz));
          ay[contatore2]=ay[contatore2]+(massa[contatore]*disty)/((distx*distx+disty*disty+distz*distz)*sqrt(distx*distx+disty*disty+distz*distz));
          az[contatore2]=az[contatore2]+(massa[contatore]*distz)/((distx*distx+disty*disty+distz*distz)*sqrt(distx*distx+disty*disty+distz*distz));
         if (contatore>contatore2) energia_potenziale[contatore2]=energia_potenziale[contatore2]+massa[contatore2]*massa[contatore]/sqrt(distx*distx+disty*disty+distz*distz);
         
           if (contatore_interno>-1) //questo in caso uso adams bashforth
            {
             //questa parte viene utilizzata da adams per primi 4 passi 
             //calcolati con eulero dopo di che la gestione dei passi precedenti
             //verrà gestita da adams stesso
            
                 printf("contatore int %d\n",contatore_interno);
                                  
                 apx[contatore_interno][contatore2]=ax[contatore2];
                 apy[contatore_interno][contatore2]=ay[contatore2];
                 apz[contatore_interno][contatore2]=az[contatore2];
                 printf("apy[0] %lf",apy[0][contatore2]);       
                 printf("apy[1] %lf",apy[1][contatore2]);       
                 printf("apy[2] %lf",apy[2][contatore2]);                                            
                 printf("apy[3] %lf",apy[3][contatore2]);       
                                     }    
            
         
         
          }
        }
     }
//parte per le masse immobili
for (contatore2=numero_masse_movimento;contatore2<numero_punti;contatore2=contatore2+1)
   {
   //questa parte tratta le masse immobili,ovvero serve per il calcolo della
   //loro unica energia.Quella potenziale!                                                                                       
            energia_potenziale[contatore2]=0;

    for (contatore=0;contatore<numero_punti;contatore=contatore+1)
    {
     
       if (contatore2!=contatore)
       {      
          distx=(-x[contatore2]+x[contatore]);
          disty=(-y[contatore2]+y[contatore]);
          distz=(-z[contatore2]+z[contatore]);

//calcolo l'accelerazione sul punto in movimento

           if (contatore>contatore2) energia_potenziale[contatore2]=energia_potenziale[contatore2]+massa[contatore2]*massa[contatore]/sqrt(distx*distx+disty*disty+distz*distz);
           }
           }
          energia[contatore2]=-energia_potenziale[contatore2]; 
          contatore=contatore2;
          
         if (idrk4==0) scrivi_file();
          
           }

 }


//Metodo di Eulero
//****************
//****************
//****************
void eulero()
{
  
  t=0;
  contatore_interno=-1;
  while (t<limt)
  {
        calcola_accelerazione();//ad ogni passo si calcola l'accelerazione
        t=t+dt;
         
        for (contatore=0;contatore<numero_masse_movimento;contatore=contatore+1)
        {
   
            //il classico eulero prima per le velocità e poi per le posizioni
             
         
            
 
           
            vx[contatore]=vx[contatore]+ax[contatore]*dt;   //velocità esplicita
            vy[contatore]=vy[contatore]+ay[contatore]*dt;
            vz[contatore]=vz[contatore]+az[contatore]*dt;

            x[contatore]=x[contatore]+vx[contatore]*dt;     //posizione implcita
            y[contatore]=y[contatore]+vy[contatore]*dt;
            z[contatore]=z[contatore]+vz[contatore]*dt;
                
 
            energia[contatore]=-energia_potenziale[contatore]+0.5*massa[contatore]*(vx[contatore]*vx[contatore]+vy[contatore]*vy[contatore]+vz[contatore]*vz[contatore]);
            distanza_origine[contatore]=sqrt(x[contatore]*x[contatore]+y[contatore]*y [contatore]+z[contatore]*z[contatore]);
           
            
            scrivi_file();
            } 

         }
 }

//*************
//*************
//************* 
void Adams_Bashforth2()
{
  
  int valore; 
  t=0;
  contatore_interno=-1;
  cc=0; 
  contatore_interno=contatore_interno+1;
  id=0;
   
  while (t<limt)
  {
 
        if (cc!=2)calcola_accelerazione();
        if (cc==2) contatore_interno=-1;
        
  
        if (cc==2) cc=3;
        
        if (cc<2)
        {    
        valore=1;
         cc=cc+1;
         t=t+dt/valore;
        
     
        for (contatore=0;contatore<numero_masse_movimento;contatore=contatore+1)
        {
          
          //Qui si calcolano i primi passi di adams con eulero,si nota che il
          //contatore_interno si incrementa.Questo verrà considerato nel calcolo
          //dell'accelerazione.  
            

  
           
           vpx[contatore_interno][contatore]=vx[contatore];
           vpy[contatore_interno][contatore]=vy[contatore];
           vpz[contatore_interno][contatore]=vz[contatore];
             

 
           x[contatore]=x[contatore]+vx[contatore]*dt/valore; //implicita
           y[contatore]=y[contatore]+vy[contatore]*dt/valore;
           z[contatore]=z[contatore]+vz[contatore]*dt/valore;

           vx[contatore]=vx[contatore]+ax[contatore]*dt/valore;//esplicita
           vy[contatore]=vy[contatore]+ay[contatore]*dt/valore;
           vz[contatore]=vz[contatore]+az[contatore]*dt/valore;
          
 
            energia[contatore]=-energia_potenziale[contatore]+0.5*massa[contatore]*(vx[contatore]*vx[contatore]+vy[contatore]*vy[contatore]+vz[contatore]*vz[contatore]);
 
           
  
 
 
 
 
 
            scrivi_file();
            } 
            contatore_interno=contatore_interno+1;  
         }
         if (cc>2)
         {
         //un volta svolto eulero per i primi passi si passa finalmente al metodo
         //adams da qui in poi questo sarà la strada che percorrerà l'algoritmo
     
         if (id==1)
         {
         
         //questa parte calcola i passi precedenti una volta eseguito eulero
         //in poche parole si "shiftano" i dati di un posto a sinistra scartando   
         //il primo dei precedenti passi.kk indica la posizione del passo mentre
         //kk2 l'indica il punto considerato
         
             for (kk2=0;kk2<numero_masse_movimento;kk2=kk2+1)
             {
                 //l'accelerazione calcolata diventa l'ultimo passo              
                 apx[2][kk2]=ax[kk2];
                 apy[2][kk2]=ay[kk2];
                 apz[2][kk2]=az[kk2];
                 
                 
            //lo shift     
            for (kk=0;kk<2;kk=kk+1)
            {
                apx[kk][kk2]=apx[kk+1][kk2]; 
                apy[kk][kk2]=apy[kk+1][kk2]; 
                apz[kk][kk2]=apz[kk+1][kk2];
            
                vpx[kk][kk2]=vpx[kk+1][kk2]; 
                vpy[kk][kk2]=vpy[kk+1][kk2]; 
                vpz[kk][kk2]=vpz[kk+1][kk2];
            }
           }
          }
        
            
 
         
         id=1;
         t=t+dt;
        
        for (kk2=0;kk2<numero_masse_movimento;kk2=kk2+1)
        {
            contatore_interno=-1;
            vx[kk2]=vx[kk2]+(3*apx[1][kk2]-apx[0][kk2])*dt/2;
            vy[kk2]=vy[kk2]+(3*apy[1][kk2]-apy[0][kk2])*dt/2;
            vz[kk2]=vz[kk2]+(3*apz[1][kk2]-apz[0][kk2])*dt/2;
            
            x[kk2]=x[kk2]+(3*vpx[1][kk2]-vpx[0][kk2])*dt/2;
            y[kk2]=y[kk2]+(3*vpy[1][kk2]-vpy[0][kk2])*dt/2;
            z[kk2]=z[kk2]+(3*vpz[1][kk2]-vpz[0][kk2])*dt/2;
             
             
            
            energia[kk2]=-energia_potenziale[kk2]+0.5*massa[kk2]*(vx[kk2]*vx[kk2]+vy[kk2]*vy[kk2]+vz[kk2]*vz[kk2]);
            distanza_origine[kk2]=sqrt(x[kk2]*x[kk2]+y[kk2]*y [kk2]+z[kk2]*z[kk2]);
            vpx[2][kk2]=vx[kk2];
            vpy[2][kk2]=vy[kk2];
            vpz[2][kk2]=vz[kk2];
           
      
           contatore=kk2;
           scrivi_file();
            } 
                


                
                
     }
         
  }
 }





 
//*****************
//*****************
//*****************
//metodo di heun
 
void heun()
{
  t=0;
  id=0;
  id2=0; 
  printf("heun");
  
  t=0;
  contatore_interno=-1;
  while (t<limt)
  {
        idrk4=0;
        calcola_accelerazione();//ad ogni passo si calcola l'accelerazione
        t=t+dt;
         
        for (contatore=0;contatore<numero_masse_movimento;contatore=contatore+1)
        {
   
            //il classico eulero prima per le velocità e poi per le posizioni
             
            axx[0][contatore]=ax[contatore];
            ayy[0][contatore]=ay[contatore];
            azz[0][contatore]=az[contatore];
            
            vxx[0][contatore]=vx[contatore];
            vyy[0][contatore]=vy[contatore];
            vzz[0][contatore]=vz[contatore];
            
    
            xx[contatore]=x[contatore];
            yy[contatore]=y[contatore];
            zz[contatore]=z[contatore];
            
                  
            vx[contatore]=vx[contatore]+ax[contatore]*dt; //esplicita
            vy[contatore]=vy[contatore]+ay[contatore]*dt;
            vz[contatore]=vz[contatore]+az[contatore]*dt;
           
            x[contatore]=x[contatore]+vxx[0][contatore]*dt;  //implicita
            y[contatore]=y[contatore]+vyy[0][contatore]*dt;
            z[contatore]=z[contatore]+vzz[0][contatore]*dt;
        
            
            
          } 
            idrk4=1;
            calcola_accelerazione();
        for (contatore=0;contatore<numero_masse_movimento;contatore=contatore+1)
        {
            
            
 
            x[contatore]=xx[contatore]+(vx[contatore]+vxx[0][contatore])*dt/2;
            y[contatore]=yy[contatore]+(vy[contatore]+vyy[0][contatore])*dt/2;
            z[contatore]=zz[contatore]+(vz[contatore]+vzz[0][contatore])*dt/2;
 
            vx[contatore]=vxx[0][contatore]+(ax[contatore]+axx[0][contatore])*dt/2;
            vy[contatore]=vyy[0][contatore]+(ay[contatore]+ayy[0][contatore])*dt/2;
            vz[contatore]=vzz[0][contatore]+(az[contatore]+azz[0][contatore])*dt/2;
            energia[contatore]=-energia_potenziale[contatore]+0.5*massa[contatore]*(vx[contatore]*vx[contatore]+vy[contatore]*vy[contatore]+vz[contatore]*vz[contatore]);
            distanza_origine[contatore]=sqrt(x[contatore]*x[contatore]+y[contatore]*y [contatore]+z[contatore]*z[contatore]);
                        
            scrivi_file();
            }
         }
 
 
 }

void rk4()

{
 
  t=0;
  id=0;
  printf("rk4");
  id2=0; 
  while (t<limt)
  {
 
        calcola_accelerazione();
         idrk4=1;       
        
        t=t+dt;
        //questo è rk4 
        id=0;
        for (kk=0;kk<numero_masse_movimento;kk=kk+1)
        {
          //avanzo del primo step memorizzando la posizione attuale         
          axx[0][kk]=ax[kk];//k1
          ayy[0][kk]=ay[kk];
          azz[0][kk]=az[kk];

          vxx[0][kk]=vx[kk];
          vyy[0][kk]=vy[kk];
          vzz[0][kk]=vz[kk];
          
          
          xx[kk]=x[kk];
          x[kk]=x[kk]+(vxx[0][kk])*dt/2;//posizione k2=(h/2k1)+xn
          yy[kk]=y[kk];
          y[kk]=y[kk]+(vyy[0][kk])*dt/2;  //rk1=eulero
          zz[kk]=z[kk];
          z[kk]=z[kk]+(vzz[0][kk])*dt/2;  
                   
          
          //memorizzo l'accelerazione attuale
          //calcolo la accelerazione solo sul punto considerato non contaminando
          //gli altri corpi
          }
          calcola_accelerazione();
 
          //memorizzo le accelerazione al primo passo         
        for (kk=0;kk<numero_masse_movimento;kk=kk+1)
        {
         
          axx[1][kk]=ax[kk];//k2
          ayy[1][kk]=ay[kk];          
          azz[1][kk]=az[kk];
         //memorizzo le velocità al primo passo                   
          vxx[1][kk]=(axx[0][kk])*dt/2+vx[kk];//k2 velocità ix2
          vyy[1][kk]=(ayy[0][kk])*dt/2+vy[kk];            
          vzz[1][kk]=(azz[0][kk])*dt/2+vz[kk];  
          //ritorno alla posizione iniziale "u_n"
          x[kk]=xx[kk];
          y[kk]=yy[kk];
          z[kk]=zz[kk];
    
          x[kk]=x[kk]+dt/2*(vxx[1][kk]);//k2 velocità
          y[kk]=y[kk]+dt/2*(vyy[1][kk]);//k3 posizione
          z[kk]=z[kk]+dt/2*(vzz[1][kk]);
          }
          calcola_accelerazione();
        for (kk=0;kk<numero_masse_movimento;kk=kk+1)
        {
     
          axx[2][kk]=ax[kk];//k3
          ayy[2][kk]=ay[kk];          
          azz[2][kk]=az[kk];


          vxx[2][kk]=vx[kk]+(axx[1][kk])*dt/2;//k3
          vyy[2][kk]=vy[kk]+(ayy[1][kk])*dt/2;            
          vzz[2][kk]=vz[kk]+(azz[1][kk])*dt/2;  
          
       
  
          x[kk]=xx[kk];
          y[kk]=yy[kk];
          z[kk]=zz[kk];
          
          x[kk]=x[kk]+dt*(vxx[2][kk]);
          y[kk]=y[kk]+dt*(vyy[2][kk]);
          z[kk]=z[kk]+dt*(vzz[2][kk]);
          }
          calcola_accelerazione();
 
        for (kk=0;kk<numero_masse_movimento;kk=kk+1)
        {
          
          axx[3][kk]=ax[kk];
          ayy[3][kk]=ay[kk];          
          azz[3][kk]=az[kk];

          vxx[3][kk]=vx[kk]+(axx[2][kk])*dt;//k3
          vyy[3][kk]=vy[kk]+(ayy[2][kk])*dt;            
          vzz[3][kk]=vz[kk]+(azz[2][kk])*dt;  
        
          
          x[kk]=xx[kk];
          y[kk]=yy[kk];
          z[kk]=zz[kk];
 
 
           

           
         
            } 
 
for (kk2=0;kk2<numero_masse_movimento;kk2=kk2+1)
 {
          //metto in pratica la formula di rk4
          energia[kk2]=-energia_potenziale[kk2]+0.5*massa[kk2]*(vx[kk2]*vx[kk2]+vy[kk2]*vy[kk2]+vz[kk2]*vz[kk2]);
          x[kk2]=x[kk2]+dt/6*(vx[kk2]+2*vxx[1][kk2]+2*vxx[2][kk2]+vxx[3][kk2]);
          y[kk2]=y[kk2]+dt/6*(vy[kk2]+2*vyy[1][kk2]+2*vyy[2][kk2]+vyy[3][kk2]);
          z[kk2]=z[kk2]+dt/6*(vz[kk2]+2*vzz[1][kk2]+2*vzz[2][kk2]+vzz[3][kk2]);

          vx[kk2]=vx[kk2]+dt/6*(axx[0][kk2]+2*axx[1][kk2]+2*axx[2][kk2]+axx[3][kk2]);
          vy[kk2]=vy[kk2]+dt/6*(ayy[0][kk2]+2*ayy[1][kk2]+2*ayy[2][kk2]+ayy[3][kk2]);
          vz[kk2]=vz[kk2]+dt/6*(azz[0][kk2]+2*azz[1][kk2]+2*azz[2][kk2]+azz[3][kk2]);
           
         
          distanza_origine[kk2]=sqrt(x[kk2]*x[kk2]+y[kk2]*y [kk2]+z[kk2]*z[kk2]);
          contatore=kk2;
 
          idrk4=0;
          scrivi_file();
           }
 
 
 }
     
 
}
 
  
  
//Inserimento dei dati
//********************
//********************
 
void inserimento_dati()
{
     contatore_interno=-1;//serve solo per i metodi a piu passi
     
     printf("Inserisci il numero di punti gravitazionali=");
     scanf("%d",&numero_punti);
      for (contatore=0;contatore<numero_punti;contatore=contatore+1)
     {
         printf("[x]_\n");
         scanf("%lf",&x[contatore]);
         printf("[y]_");
         scanf("%lf",&y[contatore]);
         printf("[z]_");
         scanf("%lf",&z[contatore]);
         printf("[massa(*G)]");
         scanf("%lf",&massa[contatore]);
 

      }
  
      printf("Indicare il numero di masse che si muovono_\n");
      scanf("%d",&numero_masse_movimento);
  
      for (contatore=0;contatore<numero_masse_movimento;contatore=contatore+1)
      {
          printf("vx[ %d ]\n",contatore);
          scanf("%lf",&vx[contatore]);
          printf("vy[ %d ]\n",contatore);
          scanf("%lf",&vy[contatore]);
          printf("vz[ %d ]\n",contatore);
          scanf("%lf",&vz[contatore]);
      }
      for (contatore2=numero_masse_movimento;contatore2<numero_punti;contatore2=contatore2+1)
      {
          fprintf(masse_fisse,"%lf\n",x[contatore2]);
          fprintf(masse_fisse,"%lf\n",y[contatore2]);
          fprintf(masse_fisse,"%lf\n",z[contatore2]);
          }
    
      printf("dt\n");
      scanf("%lf",&dt);//inserisci il dt
      printf("lim t\n");
      scanf("%lf",&limt);//inserisci il limite temporale si di fine programma
      printf("step dato energia\n");
      scanf("%d",&step_energia);//per ogni quanti valori deve prendere il dato energia
      printf("step dato posizione\n");
      scanf("%d",&step_posizione);//per ogni quanti valori deve prendere il dato energia      
      printf("scegli l'approccio numerico\n");
      printf("1-Eulero\n");
      printf("2-Heun\n");
      printf("3-Adams-Bashforth2\n");
      printf("4-Runge Kutta 4 \n");         
      scanf("%d",&numero_scelta);
      
      printf("inizio");
      startime = clock();
      if (numero_scelta==1) eulero();
      if (numero_scelta==2) heun();
      if (numero_scelta==3) Adams_Bashforth2();
      if (numero_scelta==4) rk4();
      for (kk=0;kk<numero_punti;kk=kk+1)  //a fine ciclo fa vedere le ultime posizioni
      {
          printf("%lf\n ",x[kk]);   
          printf("%lf\n ",y[kk]);
          printf("%lf\n",z[kk]);
          }
      endtime = clock();
      diff=endtime-startime;
      printf("differenza tempo %f",diff);
 
      chiusura_files();
      getch();
      }
//****************
//****************
//****************
