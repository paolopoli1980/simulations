#include<stdio.h>
#include <stdlib.h>
#include<string.h>
#include<math.h>
//******************external declaration*************//
struct nodo
{
  int label;
  int nconnections;
  int* connections;
  double x[3];
  int holes;
  int balls;
  double temperature;
  double coef1;
  double coef2;
};

//void lettura_files(int *, struct ); 

void avvia_simulazione(int nnodi,struct nodo nodilist[],int nsteps)
{
     int i,t,numberconnect,numbernode;
     double dist,prob1,prob2,casual;
     char stringa[20];
     double density;
     FILE *f3=fopen("nodidata.out","w");
     i=0;
     srand(time(NULL));
     
     while (i<nsteps)
     {   
             i++;   
             numbernode = rand() % (nnodi) + 1;
             numberconnect = rand() % (nodilist[numbernode].nconnections) + 1;
             dist=(nodilist[numbernode].x[0]-nodilist[nodilist[numbernode].connections[numberconnect]].x[0])*(nodilist[numbernode].x[0]-nodilist[nodilist[numbernode].connections[numberconnect]].x[0]); 
             dist=dist+(nodilist[numbernode].x[1]-nodilist[nodilist[numbernode].connections[numberconnect]].x[1])*(nodilist[numbernode].x[1]-nodilist[nodilist[numbernode].connections[numberconnect]].x[1]);
             dist=dist+(nodilist[numbernode].x[2]-nodilist[nodilist[numbernode].connections[numberconnect]].x[2])*(nodilist[numbernode].x[2]-nodilist[nodilist[numbernode].connections[numberconnect]].x[2]);  
             dist=sqrt(dist);
             prob1=exp((-nodilist[numbernode].coef1*dist)/((nodilist[numbernode].coef2*(nodilist[numbernode].balls*nodilist[numbernode].temperature/nodilist[numbernode].holes))));
             prob2=1;
                           
             if (nodilist[nodilist[numbernode].connections[numberconnect]].balls>0)
             {
             prob2=exp(-1/(nodilist[nodilist[numbernode].connections[numberconnect]].holes/nodilist[nodilist[numbernode].connections[numberconnect]].balls));
             }
             if (nodilist[nodilist[numbernode].connections[numberconnect]].balls==nodilist[nodilist[numbernode].connections[numberconnect]].holes) prob2=0;
             if (nodilist[numbernode].balls==0) prob1=0;
             prob1=prob1*prob2;
             casual=(double)rand() / (double)RAND_MAX;
             if (casual<prob1)
              {
                nodilist[numbernode].balls=nodilist[numbernode].balls-1;
                nodilist[nodilist[numbernode].connections[numberconnect]].balls++;
                
             }                  
              
             for (t=1;t<=nnodi;t++)
             {
 
                  density=(double)nodilist[t].balls/(double)nodilist[t].holes;  
                  fprintf(f3,"%f\n",density);
                                       
             }                                            
  }
fclose(f3);
}
void lettura_files(int nnodi,struct nodo nodilist[])
{
  //****apri files e compilare i nodi******
  char stringa[40];
  char letters[40];
  char *ptr;
  char st[40];
  int contatore=1;
  int contnumb=0;
  int contaconn=0;
  int c=0;
  int c2=0;
  int number,ex;
  float number2;
   
  FILE *f1=fopen("positions.txt","r");
  if (f1==NULL)
  {
   printf("is not possible to open the file");
   exit(1);
               }
  while (!feof(f1))
  {
           
          fscanf(f1,"%s\t",stringa);
          ptr = strtok(stringa, " ");
          printf("OK\n");
          while (ptr != NULL)
          {
             strcpy(letters, ptr);
             ptr = strtok(NULL, " ");
             number=atof(letters);
             printf("number %f",number);
             nodilist[contatore].x[contnumb]=number;
             printf("contnumb %d",contnumb);
             contnumb++;
             if (contnumb==3)
             {
                contnumb=0;
                contatore++;                
                             }                
           }
      }
          
                
 fclose(f1); 
 FILE *f2=fopen("connections.txt","r");
 contaconn=0;
 contatore=0;
 if (f2==NULL)
 {
  printf("is not possible to open the file");
  exit(1);
               }
    while (!feof(f2))
    {
          contaconn=0; 
          fscanf(f2,"%s",st);
          contatore++;
          c=0;
          while (st[c]!=';')
          {
                
           printf("%c",st[c]);     
           if (st[c]==',')
           {
                contaconn++;   
 
                              }
                                     
            c++;   
            if (st[c]==';')
            {      
                   contaconn++;
                   }                             
                }
                
         printf("contaconn %d\n",contaconn);  
         nodilist[contatore].connections=(int *) malloc((contaconn+1)*sizeof(int));
         nodilist[contatore].nconnections=contaconn-1;
               
 
   }
 
 fclose(f2);  

//********************************************************************************    
//*******************ora che ho alloccato la memoria posso salvare****************
//********************************************************************************
 f2=fopen("connections.txt","r");
 contaconn=0;
 contatore=0;
 memset(letters, 0, sizeof(char*));

 if (f2==NULL)
 {
  printf("is not possible to open the file");
  exit(1);
               }
    while (!feof(f2))
    {
          contaconn=0; 
          fscanf(f2,"%s",st);
          contatore++;
          printf("bbabaaba %s\n",st);
          c=0;
          c2=0;
          ex=0;
          while (ex==0)
          {
           if ((st[c]!=',') && (st[c]!=';'))
           {
               letters[c2]=st[c];
           } 
           if ((st[c]==',') || (st[c]==';'))
           {
                contaconn++;
                number=atoi(letters);
                printf("st è %c",st[c]);
                printf("il number e' %d \n",number);
                memset(letters, 0, sizeof(char*));
                nodilist[contatore].connections[contaconn]=number; 
                c2=0;  
            }
                                     
            c++;   
            if (st[c]==';')
            {      
                   contaconn++;
                   printf("exit");
                   ex=1;
                   }                             
                
                }   
         printf("contaconn %d\n",contaconn);  
 
   }
 
 fclose(f2);  

 f2=fopen("holes.txt","r");
 int k;
 printf("ciao");
 for (k=1;k<=nnodi;k++)
 {
    fscanf(f2,"%d",&number);
    nodilist[k].holes=number;
 }
 fclose(f2);  

 f2=fopen("balls.txt","r");
 printf("cahcchoo");
 
 for (k=1;k<=nnodi;k++)
 {
    fscanf(f2,"%d",&number);
    nodilist[k].balls=number;
 }
 fclose(f2);  
 f2=fopen("coef1.txt","r");
 
 
 for (k=1;k<=nnodi;k++)
 {
    fscanf(f2,"%f",&number2);
    nodilist[k].coef1=number2;
 }
 fclose(f2);  
 f2=fopen("coef2.txt","r");
 
 printf("cacchio");
 for (k=1;k<=nnodi;k++)
 {
    fscanf(f2,"%f",&number2);
    nodilist[k].coef2=number2;
 }
 fclose(f2);  
 f2=fopen("temperature.txt","r");
 
 printf("cacchio");
 for (k=1;k<=nnodi;k++)
 {
    fscanf(f2,"%f",&number2);
    
    nodilist[k].temperature=number2;
    printf("%f",nodilist[k].temperature);
 }
 fclose(f2);  


 }
 




int main()
{
int nnodi,number,nsteps;


FILE *f0=fopen("nnodi.txt","r");
fscanf(f0,"%d",&number);
nnodi=number;
fscanf(f0,"%d",&number);
nsteps=number;
fclose(f0);

struct nodo *nodilist = (struct nodo*)malloc((number+2)*sizeof(struct nodo));
int n=0;

 

lettura_files(nnodi,nodilist);
int i,j;

for (i=1;i<=nnodi;i++)
{
  printf("connessioni %d\n",nodilist[i].nconnections);
  printf("holes %d\n",nodilist[i].holes);
  printf("balls %d\n",nodilist[i].balls);
  printf("temperature %f\n",nodilist[i].temperature);
  printf("coef1 %f\n",nodilist[i].coef1);
  printf("coef2 %f\n",nodilist[i].coef2);
  
  
  
}
for (i=1;i<=nnodi;i++)
{
  for (j=1;j<=nodilist[i].nconnections;j++)
  {
  printf("connessioni nodo %d sono %d\n",i,nodilist[i].connections[j]);
 }
}
for (i=1;i<=nnodi;i++)
{
  for (j=0;j<3;j++)
  {
  printf("x %d is %f\n",i,nodilist[i].x[j]);
 }
}


avvia_simulazione(nnodi,nodilist,nsteps);
}
