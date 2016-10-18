//*******programma traffic programmato esclusivamenti sui nodi************
///***********************devo mettere una instestazione la programma come si deve*****************
//************************************************************************************************
#include<stdio.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>

//*************dichiarazioni strutture*********************************************************


void random_connection(int,int,int**);
void coordinate_punti(float*,float*,int,int,int);
void distribuisci_elementi(int**,int,int,int);
void distribuzione_probabilita(float*,int,int,float*,float*);
void avvia_simulazione_diffusion(float*,float*,int** ,float* ,int ,int ,int** ,int);
void ricombina_files(int,int);
void scrivi_filesconnessioni(int,int,int**);
void manual_connection(int,int,int**);
void manual_coordinate(float*,float*,int,int,int); 
void manual_elementi(int**,int,int,int);

void The_program();


void The_program()
{


//*********************************************************************************************************************
//****************************scrive nel file le connessioni***********************************************************
//*********************************************************************************************************************
	void scrivi_filesconnessioni(int nnodi,int nelementi,int** mat)
	{
	FILE *fileopenconnessioni;	
	int i,j,cont;				
	fileopenconnessioni = fopen("saveconnect.txt", "w");
	for (i=1;i<nnodi+1;i++)
	{
	j=1;
	while (mat[i][j]>0)	
	{
	        if (mat[i][j+1]>0)
		{
			fprintf(fileopenconnessioni,"%d;",mat[i][j]);
		}
	        if (mat[i][j+1]==0)
		{
			fprintf(fileopenconnessioni,"%d",mat[i][j]);
		}
	
		j++;

	}

	if (mat[i][1]!=0)
	{
		fprintf(fileopenconnessioni,"\n");
	}

	if (mat[i][1]==0)
	{
		fprintf(fileopenconnessioni,"0\n");
	}
	
	}
	fclose(fileopenconnessioni);
	}




//*********************************************************************************************************************
//*********************************************************************************************************************
//*********************************************************************************************************************


//*********************************************************************************************************************
//****************************procedura per ricombinare i files per visualizzazione grafica****************************
//*********************************************************************************************************************
	void ricombina_files(int nelementi,int tempolimite)
	{
	long int i,j,l,k,s,cont,attenzione,identificatore,id;
	FILE *fileopenrisultati;
	FILE *filepergrafica;
	 
	char stringo[80]="";
	char stringa[80]="ciao";
 
	printf("ciao"); 

	filepergrafica=fopen("simulazione.txt", "w");
 	cont=0;
	for (k=1;k<(nelementi+2);k++)
	{ 
	fileopenrisultati = fopen("risultati.txt", "r");
	char stringa[80]="ciao";	

	for (l=0;l<k;l++)
	{	
	fscanf(fileopenrisultati,"%s",stringo);		
	}

	for (j=1;j<(tempolimite);j++)
	{
	 
	 
	for (i=1;i<(nelementi+2);i++)
	{
		
        fscanf(fileopenrisultati,"%s",stringo);	

		}

 
	id=0;
	i=0;
        while (stringo[i]!='.')
	{
	if (stringo[i]!=stringa[i])
	{
		id=1;	
	}
	i++;

	}
	i=0;
        if (id==1)	 
	{
	fprintf(filepergrafica,"%s\n",stringo);
	}
	
	for(i=0;i<80;i++)
	{
	stringa[i]=stringo[i];
	}
	
				
		}

	fprintf(filepergrafica,"*\n");

	fclose(fileopenrisultati);
	}
 
	fclose(filepergrafica);
	printf("closeclose");	
 
	filepergrafica=fopen("simulgraph.txt", "w"); 
	fileopenrisultati=fopen("simulazione.txt", "r");
	stringo[0]='x';
	printf("ecco");	
    	                
    attenzione=0;
  for(k=1;k<(nelementi+1);k++)
	{

     identificatore=0;
    while (stringo[0]!='*')
	{
       	if (attenzione==0)
       	{
    	fscanf(fileopenrisultati,"%s",stringo);
         }
         attenzione=0;					
		j=0;

	
    if (stringo[0]!='*')
    {  
	                          
        while (stringo[j]!=',')
		{
		if (identificatore==0)
		{
               fprintf(filepergrafica,"%c",stringo[j]);
                                  }
    
    		j++;
			 
		}
        if (identificatore==0)
        {
         fprintf(filepergrafica,",0;");
                  }
        identificatore=1;          
		j++;
			
		while (stringo[j]!=',')
		{
			

			fprintf(filepergrafica,"%c",stringo[j]);
		j++;
		}
		fprintf(filepergrafica,",");
		j++;


		while (stringo[j]!='.')
		{	

			fprintf(filepergrafica,"%c",stringo[j]);


			j++;
		}
		fprintf(filepergrafica,";");

//*****************parte asterisco******************************

/*
		cont=cont+1;
 		if (cont==100)
		{
		fprintf(filepergrafica,"*\n");
		cont=0;
		}

*/
//***************************fine parte asterisco********************
//		printf(".\n");

	}
}
    if (stringo[0]=='*')
    {
   	fscanf(fileopenrisultati,"%s",stringo);
   	attenzione=1;
   	fprintf(filepergrafica,"\n");
	cont=0;
                       }
}
	fclose(fileopenrisultati);
	fclose(filepergrafica);

	}
//*********************************************************************************************************************
//*********************************************************************************************************************
//*********************************************************************************************************************


//********************************************************************************************************************
//*************************************procedura che avvia la simulazione********************************************
//********************************************************************************************************************* 
	void avvia_simulazione_diffusion(float* cox,float* coy,int** mat,float* mat2,int nelementi,int nnodi,int** mat3,int tempolimite,int* vet)
	{
 	//**********bisogna configurare gli elementi con la scelta iniziale************
	int i,j,k,l,t,z;
	int caca;
	float** mattoprob;
	float peso;
    int nodoscelto,casual,quota;
	float mem1,mem2,som;
	float intervallo;
	int dist;
	FILE *filerisultati;
	FILE *filecontanodi;

    int vedo;
        filerisultati = fopen("risultati.txt", "w");
	filecontanodi = fopen("contanodi.txt", "w");

	
	printf("limite %d",tempolimite);
	scanf("%d",&caca);


	mattoprob=(float** )malloc((nnodi+2) * sizeof(float* ));
	for (i=0;i<(nnodi+1);i++)
	{
		mattoprob[i] =(float* ) malloc((2) * sizeof(float *));	
	}	
//**************************************parte che inizializza il settaggio**************************
 
        srand((unsigned)time(NULL));	
	i=0;
	while (i<nelementi)
	{
	i++;       
	while (mat3[mat[i][1]][1]==0)
	{
        i++;	
	printf("inccc");
	}
	j=0;
//******************************calcolo il peso probabilistico*********************
	peso=0;

	for(k=0;k<(nnodi+1);k++)
	{
	mattoprob[k][0]=0;
	mattoprob[k][1]=0;
	}
	peso=0; 
	j=1;     
	while ((mat3[mat[i][1]][j]>0) && (j<(nnodi+1)))
	{
		 
	        mattoprob[j][0]=mat2[mat3[mat[i][1]][j]];
 	        mattoprob[j][1]=mat3[mat[i][1]][j];
 	        peso=peso+mat2[mat3[mat[i][1]][j]];	

		j++;
	}

 
 
	for(k=1;k<(j);k++)
	{
	for(l=k;l<(j);l++)
	{
 
	if (mattoprob[k][0]>mattoprob[l][0])
	{
             mem1=mattoprob[k][0];
             mem2=mattoprob[k][1];  
	     mattoprob[k][0]=mattoprob[l][0];
	     mattoprob[k][1]=mattoprob[l][1];
	     mattoprob[l][0]=mem1;		
	     mattoprob[l][1]=mem2;		

	}

	}
	}

 	printf("ciao %d\n",j);
//**********scrive le probabilita a schermo per vedere che siano messe in ordine************************
    /*
    for(k=1;k<(j);k++)
	{
              printf("%f,",mattoprob[k][0]);
	}
	*/

 //************************************************************************
 
        quota=(int)(peso*1000);

	casual=rand() % quota;

	nodoscelto=mattoprob[1][1];
	 

	vedo=1;
    for (k=1;k<(j-1);k++)
	{
		som=0;
		 
		for(l=1;l<(k+1);l++)
		{	
			som=som+mattoprob[l][0];
		}
		som=som*1000;
		if (casual>(som)) 
        {
        nodoscelto=mattoprob[k+1][1];
        vedo=k+1;
        }
	}


	intervallo=sqrt((cox[mat[i][1]]-cox[nodoscelto])*(cox[mat[i][1]]-cox[nodoscelto])+(coy[mat[i][1]]-coy[nodoscelto])*(coy[mat[i][1]]-coy[nodoscelto]));
	intervallo=2;
	dist=(int)intervallo;
	if (dist==0)
	{
		dist=1;	
	}
	mat[i][2]=nodoscelto;
	mat[i][3]=dist;

//********************************************parte di inizializzazione finita***********************************
 
}

//*****************inizia la simulazione vera e propria******************************************************** 
	
	t=0;

	
	printf("tempolimite %d\n",tempolimite);
 	for (l=1;l<(nelementi+1);l++)
	{
		fprintf(filerisultati,"%d,%d,%d.\n",mat[l][1],mat[l][2],mat[l][3]);

	}

	fprintf(filerisultati,"*\n");

	while (t<tempolimite)
	{
	printf("istante %d\n",t);
	for(k=1;k<(nelementi+1);k++)
	{
              printf("%d%d%d\n",mat[k][1],mat[k][2],mat[k][3]);


 	}


		t++;
	for  (z=1;z<(nelementi+1);z++)
	{

	       if (mat[z][3]!=0)
		{
		if (t%mat[z][3]==0) 
		{
	j=0;
 	mat[z][1]=mat[z][2];
	vet[mat[z][1]]++; //contatore di nodi ad ogni step che l'elemento arriva in tale nodo
	

	for(k=0;k<(nnodi+1);k++)
	{
	mattoprob[k][0]=0;
	mattoprob[k][1]=0;
	}
	peso=0; 
	j=1;     
	while ((mat3[mat[z][1]][j]>0) && (j<(nnodi+1))) //?????????????c'è un dubbio su nnodi+1 o nelementi+1????????
	{
		 
	        mattoprob[j][0]=mat2[mat3[mat[z][1]][j]];
 	        mattoprob[j][1]=mat3[mat[z][1]][j];
 	        peso=peso+mat2[mat3[mat[z][1]][j]];	
 
		j++;
	}
 
 
 
	for(k=1;k<(j);k++)
	{
	for(l=k;l<(j);l++)
	{
 
	if (mattoprob[k][0]>mattoprob[l][0])
	{
             mem1=mattoprob[k][0];
             mem2=mattoprob[k][1];  
	     mattoprob[k][0]=mattoprob[l][0];
	     mattoprob[k][1]=mattoprob[l][1];
	     mattoprob[l][0]=mem1;		
	     mattoprob[l][1]=mem2;		

	}

	}
	}


//****scrive le probabilita a schermo per vedere che siano messe in ordine
	for(k=1;k<(j);k++)
	{
              printf("%f,",mattoprob[k][0]);
	}
	 	printf("buongiorno %f\n",peso);

 //************************************************************************

        quota=(int)(peso*1000);

	casual=rand() % quota;
	nodoscelto=mattoprob[1][1];
	

	vedo=1;

    for (k=1;k<(j-1);k++)
	{
		som=0;
			for(l=1;l<(k+1);l++)
		{	
			som=som+mattoprob[l][0];
		}

        som=som*1000;

		if (casual>(som))
        { 
        nodoscelto=mattoprob[k+1][1];
        vedo=k+1;

        }
	}
	intervallo=sqrt((cox[mat[z][1]]-cox[nodoscelto])*(cox[mat[z][1]]-cox[nodoscelto])+(coy[mat[z][1]]-coy[nodoscelto])*(coy[mat[z][1]]-coy[nodoscelto]));
        intervallo=2;
	dist=(int)intervallo+t;
	mat[z][2]=nodoscelto;
	mat[z][3]=dist;
		     		
		
		
		}
		}
		}



	
	
 	for (l=1;l<(nelementi+1);l++)
	{
		fprintf(filerisultati,"%d,%d,%d.\n",mat[l][1],mat[l][2],mat[l][3]);

	}

	fprintf(filerisultati,"*\n");
     	


	}	

	for (l=1;l<(nnodi+1);l++)
	{
		fprintf(filecontanodi,"%d\n",vet[l]);

	}	

 fclose(filerisultati);	
 fclose(filecontanodi);	


	}

//***************************************************************************************************************
//******************************fine procedura di avvio simulazione************************************************
//*****************************************************************************************************************


//*************************************************************************************************
//***************************procedura per le connessioni manuali**********************************
//*************************************************************************************************


	void manual_connection(int n,int max,int** mat)
	{
		char stringo[80];
		char c[80];
		int i,j,id;
		int numero;
		int k;
		FILE *matrixmanual;
		matrixmanual = fopen("manualcon.txt", "r");
		
		for(i=1;i<n+1;i++)
		{
			fscanf(matrixmanual,"%s",stringo);			
 			printf("stringa = %s",stringo);
			j=0;
		        id=0;
			k=0;		
			numero=0;
			while (id<1)
			{
 			
			
			if (stringo[j]==';')
			{
           			j++;			
			}
	
		        while ((stringo[j]!=';') && (id<1))
			{
			printf("blba");
 			  if ((stringo[j]!=';') && (stringo[j]!='\0'))
			  {
			    c[k]=stringo[j];
 
				}
		
		          if (stringo[j]=='\0') 
			  {
				id=1;
 
				}
            if (stringo[j]!='\0')
            {
			  j++;	
			  k++;
            } 		

			}
			numero++;
		        c[k]='\0';
			
			printf("stringo %s ",c);
 			mat[i][numero]=atoi(c);	
			k=0;
			}
		printf("\n");
		}
				

		fclose(matrixmanual);

	}
//**************************************************************************************************
//****************************fine procedura connessioni manuale************************************
//**************************************************************************************************


//************************************************************************************************
//****************************procedura per le connessioni random**********************************
//************************************************************************************************

	void random_connection(int n,int max,int** mat)
	{
	   int i,j,k,consing,exist,inc,elemento;
	   srand((unsigned)time(NULL));	

           for (i=1;i<(n+1);i++)
	{
	       consing=rand() % (max+1);  //numero di elementi che sono connessi al nodo
               consing=max;	       
		inc=1;	//serve per vedere quanti elementi sono già connessi
               for (k=1;k<(n+1);k++)
		{
		 if (mat[i][k]>0) inc++;
                  }
           elemento=i;		            
	   for (j=inc;j<(consing+1);j++)
		{		//while elementi sono nuovi sulla riga ecc.... 
//********random seq********************
/*

		if (elemento<(n)) 
		{		
		elemento=elemento+1;
			

		
		printf("elemento,%d",elemento);
		mat[i][j]=elemento;
                k=1;
               while (mat[elemento][k]>0)
		{
	         k++; 	
		} 
	        mat[elemento][k]=i;
		}
}
}
*/
//***************************************fine random seq****************
		
//**********random primo*************************************

		k=1;	
                 elemento=i;
 	
    	 while (elemento==i)
		{
                 elemento=(rand() % (n))+1;  			
		}


		 k=1;
		 while (mat[i][k]>0)
		{
 
		 if (mat[i][k]==elemento) 
		{
		      k=0;
		     elemento=i;
		     while (elemento==i)
		     {
                        elemento=(rand() % (n))+1;  			
		      }	
		               

		}
 		 k++;
  		}

	mat[i][j]=elemento;
		//****adesso devo memorizzare il nuovo valore nel nodo complementare
                k=1; 
               while (mat[elemento][k]>0)
		{
	         k++; 	
		} 
	        mat[elemento][k]=i;



}	
 }

//***********************fine rand primo*************	

}

//**********************************************************************************************************
//***********************fine procedura connessioni random***************************************************
//************************************************************************************************************

//************************************************************************************************************
//************************procedura coordinate manuali********************************************************
//************************************************************************************************************
	void manual_coordinate(float* cox,float* coy,int limx,int limy,int n)
	{

		char stringo[80];
		char c[80];
		int i,j,id;
		int numero;
		int k;
		FILE *matrixmanual;
    	FILE *filecoxy;
		matrixmanual = fopen("manualcor.txt", "r");
      	filecoxy = fopen("coxy.txt", "w");
	
		for(i=1;i<n+1;i++)
		{
			fscanf(matrixmanual,"%s",stringo);			
 			printf("stringa = %s",stringo);
			j=0;
		        id=0;
			k=0;		
			numero=0;
			while (id<1)
			{
 			
			
			if (stringo[j]==';')
			{
           			j++;			
			}
	
		        while ((stringo[j]!=';') && (id<1))
			{
			printf("blba");
 			  if ((stringo[j]!=';') && (stringo[j]!='\0'))
			  {
			    c[k]=stringo[j];
 
				}
		
		          if (stringo[j]=='\0') 
			  {
				id=1;
 
				}
               
			if (stringo[j]!='\0')
			{
			 
   			 j++;			
               		  k++; 		

			}

		}
			numero++;
		        c[k]='\0';
			printf("il k is %d \n",k);
			printf("stringo %s ",c);
			
			
			if (numero==1) 			
			{
			cox[i]=atof(c);	
			}
			if (numero==2) 			
			{
			coy[i]=atof(c);	
		    fprintf(filecoxy,"%f,%f\n",cox[i],coy[i]);	                
			}
 

			k=0;
			}
		printf("\n");
		}
				

		fclose(matrixmanual);
		fclose(filecoxy);


	}
//************************************************************************************************************
//************************************************************************************************************
//***********************************************************************************************************

//**********************************************************************************************
//*************************procedura coordinate nodi*******************************************
//************************************************************************************************

	void coordinate_punti(float* cox,float* coy,int limx,int limy,int nnodi)
	{
		int i,j;		
		srand((unsigned)time(NULL));	
		int identificatore=0;                
		int errore=1;
		FILE *filecoxy;
  
        	filecoxy = fopen("coxy.txt", "w");
		
		while (errore==1)
		{
		identificatore=0;
 		for (i=1;i<(nnodi+1);i++)
		{
		   cox[i]=(rand() % 10000)/100.0;		
		   coy[i]=(rand() % 10000)/100.0;		

		}
/*
		for (i=1;i<(nnodi+1);i++)
		{
		for (j=i+1;j<(nnodi+1);j++)
		{
		if ((cox[i]-cox[j])*(cox[i]-cox[j])+(coy[i]-coy[j])*(coy[i]-coy[j])<1)
		{	
		 identificatore=1;	
		}

		}		
		}
*/
		if (identificatore==0) errore=0;              		
		}


		for (i=1;i<(nnodi+1);i++)
		{
			fprintf(filecoxy,"%f,%f \n",cox[i],coy[i]);
 
		}

		fclose(filecoxy);

 
	}
//*************************************************************************************************
//*****************************fine procedura coordinate nodi***************************************
//***************************************************************************************************

//***************************************************************************************************
//*****************************manual elementi*******************************************************
//***************************************************************************************************

	void manual_elementi(int** mat,int nelementi,int nnodi,int nfunction)
	{
        	char stringo[80];
		char c;
		int i,j,id;
		int numero;
		int k;
		FILE *matrixmanual;
		matrixmanual = fopen("manualelementi.txt", "r");
 

		for (i=1;i<(nelementi+1);i++)
		{
		
			fscanf(matrixmanual,"%s",stringo);
			numero=atoi(stringo);			
			mat[i][1]=numero;			
			printf("numero %d\n",numero);				

		}

	fclose(matrixmanual);
		
	}
//***************************************************************************************************
//***************************************************************************************************
//***************************************************************************************************

//**********************************************************************************************
//***************procedura per distribuire gli elementi****************************************
///**********************************************************************************************
	void distribuisci_elementi(int** mat,int nelementi,int nnodi,int nfunction)
	{
		int i;		
 		srand((unsigned)time(NULL));	
		for (i=1;i<(nelementi+1);i++)
		{
			mat[i][1]=(rand()% nnodi) +1;
				 
		}			
		
		
	}
//*************************************************************************************************
//****************************fine procedura ditribuzione elementi***************************************
//********************************************************************************************************



//**********************************************************************************************
//***************procedura per distribuire la probabilita****************************************
///**********************************************************************************************

	void distribuzione_probabilita(float* mat,int nnodi,int nfunction,float* cox,float* coy)
	{
	//*****qui si mette la distrbuzione simpatizzata dal problema******  	
	//****di default metto una gaussiana************
		float* parametro;
		float* coefficiente;
		int i,j;
		float* centrox;
		float* centroy;

		parametro=(float* )malloc((nfunction+2) * sizeof(float* ));
		coefficiente=(float* )malloc((nfunction+2) * sizeof(float* ));
		centrox=(float* )malloc((nnodi+2) * sizeof(float* ));
		centroy=(float* )malloc((nnodi+2) * sizeof(float* ));

	    
    	for (i=1;i<nnodi+1;i++)
		{
			printf("coxy.x= %f\n",cox[i]);
			printf("coxy.y= %f\n",coy[i]);
		}
		int p;
		scanf("%d",&p);

		for (i=1;i<(nfunction+1);i++)

		{
			printf("Parametro[%d]",i);			
			scanf("%f",&parametro[i]);
			printf("Coeff[%d]",i);			
			scanf("%f",&coefficiente[i]);
			printf("x[%d]",i);			
			scanf("%f",&centrox[i]);
			printf("y[%d]",i);			
			scanf("%f",&centroy[i]);

  

		}
		for (i=1;i<(nnodi+1);i++)
		{
		for (j=1;j<(nfunction+1);j++)
		{

mat[i]=mat[i]+coefficiente[j]*exp((-(cox[i]-centrox[j])*(cox[i]-centrox[j])-(coy[i]-centroy[j])*(coy[i]-centroy[j]))*parametro[j]);

		 
		
			}
	

	}
	//********Salvataggio punti per il grafico della funzione****************
	float maxx,minx,maxy,miny;
	maxx=-100000;
	minx=100000;
	maxy=-100000;
	miny=100000;
	
//********calcola i limiti per disegnare il grafico	
        for (i=1;i<(nnodi+1);i++)
	{
	  if (cox[i]>maxx) maxx=cox[i];
          if (coy[i]>maxy) maxy=coy[i];
       	  if (cox[i]<minx) minx=cox[i];
	  if (coy[i]<miny) miny=coy[i];
	}
//***********************************************************************
        float px,py,funz;
	px=minx;
	py=miny;
         
	FILE *filegraph;
  
        filegraph = fopen("grafico.txt", "w");
	while (py<maxy)
	{
	     py=py+0.1;  //il passo è meglio regolarlo in funzione della simulazione
	px=minx;
	while (px<maxx)
	{
	     px=px+0.5;
	     funz=0;	
        	for(j=1;j<(nfunction+1);j++)
		{  
		     funz=funz+coefficiente[j]*exp((-(px-centrox[j])*(px-centrox[j])-(py-centroy[j])*(py-centroy[j]))*parametro[j]);

		} 
		fprintf(filegraph,"%f,%f,%f\n",px,py,funz);
        }

	}
	fclose(filegraph);
        }
//****************************************************************************************************
//******************************fine procedura di distribuzione probabilità****************************
//*******************************************************************************************************




//*************************************************************
//***********variabili del programma dichiarate**************
//*************tabella***************************************
        int i,j;
	int nnodi,nelementi,nfunction;
        int max,limx,limy,tempolimite; 
        nnodi=4;
	limx=100;
	limy=100;
	nelementi=1;
	nfunction=2;
	tempolimite=50;	 
	max=2; 
	int** mat_connessioni;
	int** elementi; 
	int* containodi;
	float* probabilita;
        float* cox;
        float* coy;
	char carattere;

         mat_connessioni =(int** ) malloc((nnodi+2) * sizeof(int *)); 
	 containodi = (int* ) malloc((nnodi+2) * sizeof(int* ));
	 elementi=(int** ) malloc((nelementi+2) * sizeof(int *));
	 probabilita=(float*) malloc((nnodi+2) * sizeof(float *));
	 cox=(float* ) malloc((nnodi+2) * sizeof(float *));
	 coy=(float* ) malloc((nnodi+2) * sizeof(float *));
	 
 
 
	//**************************************************

 
	//*****************anche questa parte può essere considerata nella dichiarazione variabili
	for (i=0;i<(nnodi+1);i++)
	{
		probabilita[i]=0; 
	
	}
        for (i=0;i<(nelementi+1);i++)
	{
		elementi[i] =(int* ) malloc((5) * sizeof(int *));	
	}
	for (i=0;i<(nnodi+1);i++)
	{
		mat_connessioni[i] =(int* ) malloc((nnodi+2) * sizeof(int *));
	} 
	//**************inizializzazione a zero la matrice connessioni
 	printf("ok");
	for (i=0;i<(nnodi+1);i++)
	{
	cox[i]=0;
	coy[i]=0;
	for (j=0;j<(nnodi+2);j++)
	{
        mat_connessioni[i][j]=0;
	containodi[j]=0; 	
	 
	}
	}
	for (i=0;i<(nelementi+1);i++)
	{
	for (j=0;j<5;j++)
	{	
	elementi[i][j]=0; 		
	}
	}

//******************************************************
 
//******************************************************
	printf("premi R per random M per configurazione manuale=");
	scanf("%c",&carattere); 

//*******************************************************
	if (carattere=='R')
	{
		 random_connection(nnodi,max,mat_connessioni);
	}


	if (carattere=='M')
	{
		 manual_connection(nnodi,max,mat_connessioni);
	}
	

	printf("\n");
	//***********************scrive la matrice connessioni*************
        for (i=1;i<(nnodi+1);i++)
	{
	for (j=1;j<(nnodi+1);j++)
	{

	printf("x%d",mat_connessioni[i][j]);

	}
	printf("\n");
	}
       //***************************************************
       //********** adesso devo memorizzare i punti delle mie connessioni
       printf("step coordinate");	
       
       if (carattere=='R')  	
       {
       coordinate_punti(cox,coy,limx,limy,nnodi);
       }       
	if (carattere=='M')  	
       {
       
	manual_coordinate(cox,coy,limx,limy,nnodi);
       }
       
       //**************************scrive la struttura dei punti***********

	for (i=1;i<(nnodi+1);i++)
	{

	printf("%f,",cox[i]);
	printf("%f",coy[i]);
	printf("\n");
	}
       //*******************************************************************
       for (i=0;i<(nelementi+1);i++)
       {
       for (j=0;j<(5);j++)
       {
	       elementi[i][j]=0;
       }
	}
       printf("step elementi");

       if (carattere=='R')
       {		
       distribuisci_elementi(elementi,nelementi,nnodi,nfunction);		
       }

       if (carattere=='M')
       {		
	manual_elementi(elementi,nelementi,nnodi,nfunction);		
       }
       

       //**************************scrive l'inizializzazione degli elementi***********
       for (i=1;i<(nelementi+1);i++)
       {
       for (j=1;j<(4);j++)
       {
	       printf("%d",elementi[i][j]);
 

	        
       }
               printf("\n");
	}

	distribuzione_probabilita(probabilita,nnodi,nfunction,cox,coy);
	//****************scrive le probabilità date**************
	for(i=1;i<(nnodi+1);i++)
	{	
	       printf("%f\n",probabilita[i]);			

	}
	//********************************************************
	avvia_simulazione_diffusion(cox,coy,elementi,probabilita,nelementi,nnodi,mat_connessioni,tempolimite,containodi);
	printf("fine");

	


	
	
	


	ricombina_files(nelementi,tempolimite);

	scrivi_filesconnessioni(nnodi,nelementi,mat_connessioni);
 
	//*****************************ristampa alla fine la matrice connessioni
        printf("\n");

        for (i=1;i<(nnodi+1);i++)
	{
	for (j=1;j<(nnodi+1);j++)
	{

	printf("%d",mat_connessioni[i][j]);
	printf("x");

	}
	printf("\n");
	}

	//********************************************



	free(mat_connessioni);
	free(probabilita);
	free(elementi);
	free(containodi);
    free(cox);
    free(coy); 

}


int main()
{

The_program();

}

