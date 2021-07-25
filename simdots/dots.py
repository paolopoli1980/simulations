import numpy as np
class dot:
    def __init__(self,index):
        self.connections=[]
        self.maxstate=0
        self.states=[]
        self.state=0
        self.index=index
        self.statenew=0


    def sim(self,dots):
        stateindex=0
        
        for i in range(len(self.connections)):
            stateindex+=((dots[self.connections[i]].maxstate+1)**(len(self.connections)-i-1))*dots[self.connections[i]].state   
        self.statenew=self.states[stateindex]


class simdot:
    
    def simdots(self,niter,dots):
        listofstates=[]
        
        for el in dots:
            print(el.states)

        for i in range(niter):
            for el in dots:
                el.sim(dots)
                
            for el in dots:        
                el.state=el.statenew
            
            digitlist=[]
            for el in dots:
                
                digitlist.append(el.state)
            listofstates.append(digitlist)          
        return listofstates

class qdot:
    def __init__(self,index):
        self.connections=[]
        self.maxstate=0
        self.states=[]
        self.state=[]
        self.index=index
        self.statenew=[]
        self.momentstate=[]
        self.statenewmoment=[]
      

    def sim(self,qdots):
        self.stringstate=[]
        self.statenew=self.state.copy()
        self.statenewmoment=qdots[self.connections[0]].state.copy()
        self.momentstate=[]

        for i in range(1,len(self.connections)):

            l=len(self.statenewmoment)

            for j in range(l):
                
                for k in range(len(qdots[self.connections[i]].state)):
                    self.momentstate.append(self.statenewmoment[j]*qdots[self.connections[i]].state[k])
                
                
            l=len(self.statenewmoment)
            self.statenewmoment=self.momentstate.copy()
            self.momentstate=[]
    
        for i in range(len(self.statenew)):
            self.statenew[i]=0
  
        for i in range(len(self.statenewmoment)):
               

            self.statenew[self.states[i]]+=self.statenewmoment[i]
            
        self.statenew=self.statenew/np.linalg.norm(self.statenew)
          
        return self.statenew            
            

class simqdot:

    def simqdots(self,niter,qdots):
        listofstates=[]
        for i in range(niter):

            
            liststates=[]


            for i in range(len(qdots)):
                liststates.append(qdots[i].sim(qdots))
 
            for i in range(len(qdots)):
                qdots[i].state=liststates[i]
            listofstates.append(liststates)
        return listofstates

    

        
