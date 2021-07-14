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
            #print('********************')
            digitlist=[]
            for el in dots:
                #print(el.state, end=" ")
                digitlist.append(el.state)
            listofstates.append(digitlist)          
        return listofstates
