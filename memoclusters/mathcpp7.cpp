//*****************************************************************************
//********************************* Title memoclusters ************************
//*************** Simulation concerning 3D memoclusters sustaining was written*******************
//*************** with the goal to simulate a mathematics model, where clusters interact *******************                          
//*************** with a law of r^(alpha) field, and where their surviving depend by the sum of the 
//*************** total felt field.************************************************* 
//*****************************************************************************
//*****************************************************************************


#include<iostream>
#include <cmath>
#include <malloc.h>
#include <time.h>
#include <stdlib.h>
#include <fstream>
using namespace std;
//void density_calcuation(Cube);
//*********************************************************************************************************
//********************* The class about the cube space, where memoclusters are laid ***********************
//*********************************************************************************************************

class Cube
{
	private:
		double grid[20][20][20];
		double memgrid[20][20][20];	
		bool cuborestart=true;
				
		
		
		
	public:
		void init_pos_setting();
		void fill_in();
		void write_grid();
		void selection();
		void field_calculation(int,int,int);
		void valuetozero();
		void mem_grid();
		void mem_grid_fill_in();
		void outer_counting_off();
		void zerosurfacefunction(int);
		void mem_grid_in_grid();
		int density_calculation();
		int outer_clusters_count();
		bool restart();
		double density,esp,valueon,valuetrigger,latticedistance,coef;
		double value[20][20][20];
		int cube_side;
		int nsites;
		int contsites;
		double countoutoff,countoff;
		double resetsurface;
			
		
};

//*******************************************************************************************************************
//*********************** This function allows you to cancel for a moment the clusters on the surface ****************
//*******************************************************************************************************************
 
void Cube::zerosurfacefunction(int deep)
{
	for (int x=0;x<deep;x++)
	{
	
	for (int j=0;j<cube_side;j++)
	{
		for (int k=0;k<cube_side;k++)
		{
			if (grid[0+x][j][k]==1) grid[0+x][j][k]=0.0000001;
		}
	}
	for (int i=0;i<cube_side;i++)
	{
		for (int k=0;k<cube_side;k++)
		{
			if (grid[i][0+x][k]==1) grid[i][0+x][k]=0.0000001;
		}
	}
	for (int i=0;i<cube_side;i++)
	{
		for (int j=0;j<cube_side;j++)
		{
			if (grid[i][j][0+x]==1) grid[i][j][0+x]=0.0000001;
		}
	}
	for (int j=0;j<cube_side;j++)
	{
		for (int k=0;k<cube_side;k++)
		{
			if (grid[cube_side-1-x][j][k]==1) grid[cube_side-1-x][j][k]=0.0000001;
		}
	}
	for (int i=0;i<cube_side;i++)
	{
		for (int k=0;k<cube_side;k++)
		{
			if (grid[i][cube_side-1-x][k]==1) grid[i][cube_side-1-x][k]=0.0000001;
		}
	}
	for (int i=0;i<cube_side;i++)
	{
		for (int j=0;j<cube_side;j++)
		{
			if (grid[i][j][cube_side-1-x]==1) grid[i][j][cube_side-1-x]=0.0000001;
		}
	}

}
}

//***********************************************************************************************************
//************************ It inserts the grid put in memgrid in the main grid, used in the simulation*******
//***********************************************************************************************************
void Cube::mem_grid_in_grid()
{
	for (int i=0;i<20;i++)
	{
		for (int j=0;j<20;j++)
		{
			for (int k=0;k<20;k++)
			{
				grid[i][j][k]=memgrid[i][j][k];
			}
		}
	}
	
}

//***********************************************************************************************
//********************** It memorizes the cluster cube taken in consideration ******************
//**********************************************************************************************

void Cube::mem_grid()
{
	for (int i=0;i<20;i++)
	{
		for (int j=0;j<20;j++)
		{
			for (int k=0;k<20;k++)
			{
				memgrid[i][j][k]=grid[i][j][k];
			}
		}
	}

}
//***************************************************************************************************
//******************************* reset of the variable vaules field.*********************************
//***************************************************************************************************

void Cube::valuetozero()
{
	for (int i=0;i<20;i++)
	{
		for (int j=0;j<20;j++)
		{
			for (int k=0;k<20;k++)
			{
				value[i][j][k]=0;
			}
		}
	}
	}
//***********************************************************************************
//**************** It sets the intial grid to zero **********************************
//***********************************************************************************

void Cube::init_pos_setting()
{
	for (int i=0;i<20;i++)
	{
		for (int j=0;j<20;j++)
		{
			for (int k=0;k<20;k++)
			{
				grid[i][j][k]=0;
			}
		}
	}
	}
//***************************************************************************************************************
//******************************** Set memoclusters to on given a certain density ***********************
//***************************************************************************************************************
	
void Cube::fill_in()
{
	int cont=0;
	//cout<<nsites<<endl;
	//cout<<cont;
	while (cont<nsites)
	{
		//cout<<"into";
		int x=(int)rand()%cube_side;
		int y=(int)rand()%cube_side;
		int z=(int)rand()%cube_side;
		
		if (grid[x][y][z]==0)
		{
			cont++;
			grid[x][y][z]=1;
			
			//cout<<x<<","<<","<<y<<","<<z<<endl;
		}
		
		
	}	
	}
//*********************************************************************************************************
//******************** When this fuction is called, it writes to screen the clusters grid in that**********
//******************** specific time.**********************************************************************
//*********************************************************************************************************
 	
void Cube::write_grid()
{
	for (int i=0;i<cube_side;i++)
	{
		for (int j=0;j<cube_side;j++)
		{
			for (int k=0;k<cube_side;k++)
			{
				if (grid[i][j][k]!=0.0000001)
				{
				
					cout<<grid[i][j][k]<<",";
				}
				else
				{
					cout<<"*"<<",";
				
					}
				}
			cout<<endl;
			}
			
		cout<<"*************"<<endl;
		}
	
	
 
}
//**********************************************************************************************************
//*************** If the cluster is active, the field is calculated in funtion of the other clusters********
//**********************************************************************************************************

void Cube::selection()
{
	for (int i=0;i<cube_side;i++)
	{
		for (int j=0;j<cube_side;j++)
		{
			for (int k=0;k<cube_side;k++)
			{
				if (grid[i][j][k]>0)
				field_calculation(i,j,k);
			}
			//cout<<endl;
		}
	//cout<<"*************"<<endl;
	}	

}
//**********************************************************************************************************
//************************** The field is calculated on the spcific cluster considered *********************
//**********************************************************************************************************

void Cube::field_calculation(int x,int y,int z)
{
	for (int i=0;i<cube_side;i++)
	{
		for (int j=0;j<cube_side;j++)
		{
			for (int k=0;k<cube_side;k++)
			{
				if ((grid[i][j][k]==1) and ((i!=x) or (j!=y) or (k!=z)))
				{
					value[x][y][z]+=valueon*coef*pow(latticedistance*sqrt(pow((i-x),2)+pow((j-y),2)+pow((k-z),2)),esp);
					
					
				}
				
			}
			//cout<<endl;
		}
	//cout<<"*************"<<endl;
	}
	//cout<<value[x][y][z]<<endl;		
	}
	
//***********************************************************************************************************
//*********************** This function updates the grid until new events happen ****************************
//************************************************************************************************************
	
bool Cube::restart()
{
	cuborestart=false;
//	cout<<"AAAAAA";
	for (int i=0;i<cube_side;i++)
	{
		for (int j=0;j<cube_side;j++)
		{
			for (int k=0;k<cube_side;k++)
			{
				if (grid[i][j][k]==1)
				{
					if (value[i][j][k]<valuetrigger)
					{
						grid[i][j][k]=0;
						cuborestart=true;
						//cout<<"in";
						//cout<<value[i][j][k];
						contsites++;
						}
					
				}
				if (grid[i][j][k]==0.0000001)
				{
					if (value[i][j][k]>=valuetrigger)
					{
						grid[i][j][k]=1;
						cuborestart=true;
						//cout<<"in";
						//cout<<value[i][j][k];
						contsites++;
						}

				}			
				

			}
			//cout<<endl;
		}
	//cout<<"*************"<<endl;
	}		
	return cuborestart;
	}

//*****************************************************************************************
//*************************** Density on clusters calculation function ********************
//*****************************************************************************************
 
int Cube::density_calculation()
{
	int contatore=0;
	for (int i=0;i<cube_side;i++)
	{
		for (int j=0;j<cube_side;j++)
		{
			for (int k=0;k<cube_side;k++)
			{
				if (grid[i][j][k]==1) contatore++; 
				
			}
			//cout<<endl;
		}
	//cout<<"*************"<<endl;
	}		
	return contatore;
		
				
	}

//******************************************************************************************************
//******** The survived clusters calculation on the border *********************************************
//******************************************************************************************************
	
int Cube::outer_clusters_count()
{
	int contatore=0;
	int memcountedgrid[20][20][20];
	for (int i=0;i<20;i++)
	{
		for (int j=0;j<20;j++)
		{
			for (int k=0;k<20;k++)
			{
				memcountedgrid[i][j][k]=0;
			}
		}
	}	
	for (int j=0;j<cube_side;j++)
	{
		for (int k=0;k<cube_side;k++)
		{
			if ((grid[0][j][k]==1) and (memcountedgrid[0][j][k]==0))
			{
			
			memcountedgrid[0][j][k]=1;
			contatore++;
			}
		}
	}
	for (int i=0;i<cube_side;i++)
	{
		for (int k=0;k<cube_side;k++)
		{
			if ((grid[i][0][k]==1) and (memcountedgrid[i][0][k]==0))
			{
				memcountedgrid[i][0][k]=1;
				contatore++;
			}
		}
	}
	for (int i=0;i<cube_side;i++)
	{
		for (int j=0;j<cube_side;j++)
		{
			if ((grid[i][j][0]==1) and (memcountedgrid[i][j][0]==0))
			{
				memcountedgrid[i][j][0]=1;
				contatore++;
			}
		}
	}
	for (int j=0;j<cube_side;j++)
	{
		for (int k=0;k<cube_side;k++)
		{
			if ((grid[cube_side-1][j][k]==1) and (memcountedgrid[cube_side-1][j][k]==0))
			{
				memcountedgrid[cube_side-1][j][k]=1;
			
				contatore++;
			}
		}
	}
	for (int i=0;i<cube_side;i++)
	{
		for (int k=0;k<cube_side;k++)
		{
			if ((grid[i][cube_side-1][k]==1) and (memcountedgrid[i][cube_side-1][k]==0))   
			{
				memcountedgrid[i][cube_side-1][k]=1;
			
				contatore++;
			}
		}
	}
	for (int i=0;i<cube_side;i++)
	{
		for (int j=0;j<cube_side;j++)
		{
			if ((grid[i][j][cube_side-1]==1) and (memcountedgrid[i][j][cube_side-1]==0))
			{
				memcountedgrid[i][j][cube_side-1]=1;
				contatore++;
			}
		}
	}

	return contatore;	
}
							
int main()
{
int numbdensity=1;
int ntrials=2;
int deep=3;
char press_key;
double densityval[numbdensity];
double numberon[numbdensity];
int outer_counter[1];

srand(time(NULL));
Cube cubo;

cout<<"Start!"<<endl;
cubo.cube_side=8;
cubo.esp=-100;
cubo.valueon=1.0;
cubo.valuetrigger=1.0;
cubo.latticedistance=1.0;
cubo.resetsurface=1;

cubo.coef=1.0;



for (int l=0;l<numbdensity;l++)
{
	numberon[l]=0;
	densityval[l]=0;
}
for (int j=0;j<numbdensity;j++)
{
	cubo.density=(double)(j+1)/(double)numbdensity;
	cubo.density=0.44;
	densityval[j]=cubo.density;
	for (int i=0;i<ntrials;i++)
	{
	
		

		//cubo.density=.5;
		
		
		
		cubo.nsites=cubo.density*pow(cubo.cube_side,3);
		cubo.contsites=0;
		cubo.init_pos_setting();
		//cubo.write_grid();
		cubo.fill_in();
		if ((cubo.resetsurface==1) and (i==1))
		{
			cubo.mem_grid_in_grid();
			
			cubo.zerosurfacefunction(deep);	
			
			
		}
		if ((cubo.resetsurface==1) and (i==0))
		{
		
			outer_counter[0]=cubo.outer_clusters_count();
		}
		//cubo.write_grid();
		//cout<<cubo.density<<endl;

		if (cubo.resetsurface==1)
		{
			cout<<"Pressa a key";
			cin>>press_key;
		}
		//cout<<"start!"<<endl;
	
		
	do
	{
		cubo.valuetozero();
		cubo.selection();
		
		//cubo.write_grid();
		//cout<<"xxxxxxxxxxxxxxxxx"<<endl;
		}while (cubo.restart()==true);

	numberon[j]+=(double)cubo.density_calculation()/(pow(cubo.cube_side,3));
	if ((cubo.resetsurface==1) and (i==0))
	{
	
		cubo.mem_grid();			
	}			
	}
		
	  //            
	//cout<<endl;
 
	numberon[j]/=ntrials;

//	cout<<"END"<<endl;
//	cubo.write_grid();

	}
	cout<<"xxxxxxxxxxxxxxxxx"<<endl;	



if (cubo.resetsurface==1) 
{

outer_counter[1]=cubo.outer_clusters_count();
cout<<"Outer ratio="<<(outer_counter[0])<<endl;
cout<<"Outer ratio="<<(outer_counter[1])<<endl;
cout<<"ratio"<<((double)outer_counter[1]/(double)outer_counter[0])<<endl;

}
cubo.write_grid();
for (int h=0;h<numbdensity;h++) 
{

cout<<numberon[h]<<" , ";

}
cout<<endl;
for (int h=0;h<numbdensity;h++) 
{

cout<<densityval[h]<<" , ";

}
if (cubo.resetsurface==0)
{
	//******* apri file *********
	ofstream graphfile;
	graphfile.open("graphfile.txt");
	for (int h=0; h<numbdensity;h++)
	{
		graphfile<<densityval[h]<<"   "<<numberon[h]<<endl;
	}	
	graphfile.close();
}

}
