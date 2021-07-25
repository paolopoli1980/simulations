

def simula(n):
    stringstato=''
    listastati=[]
    listacont=[0 for i in range(2**n+1)]
    state=[0 for i in range(n)]
    newstate=[0 for i in range(n)]
    cont=0
    state=[0,0,0]
    newstate=[0,0,0]
    for j in range(n):
        stringstato+=str(newstate[j])
    listastati.append(stringstato)       
    #print (listastati)
    for i in range(2**n):
        
        for j in range(n):
            stringa=''
            for k in range(n):
                if k!=j:
                    stringa+=str(state[k])
            decimale=int(stringa,2)
            
            newstate[j]=int(stati[j][decimale])
        stringstato=''
        for j in range(n):
            stringstato+=str(newstate[j])
        listastati.append(stringstato)        
        state[:]=newstate[:]
        
    nocount='true'
    
    for s in range(len(listastati)):
        
        for t in range(s+1,len(listastati)):
            if listastati[s]==listastati[t]:
                #print (t)
                listacont[t]=1
    cont=0
    for s in range(len(listacont)):
        if listacont[s]==0:
            cont+=1
            
    #print('*******************************************')            
   # print (listastati)             
   # print(stati)
    
    if cont>maxval[0]:
        
        #print (listacont)
        maxval[0]=cont
        print ('valoremax',maxval[0])
        print (listastati)
        print (stati)
        
        
n=3
stati=[ ['0' for j in range(2**(n-1))] for i in range(n)]

print (stati)
maxval=[0]

for i in range(2**(2**(n-1)*n)):
    binario=bin(i)
    binario=binario[2:len(binario)]
    
    stringa=''
    for j in range(len(binario),2**(n-1)*n):
        stringa+='0'
    stringa+=binario
    binario=stringa
    
    for j in range(n):
        cont=0
        for k in range(2**((n-1))*j,2**((n-1))*(j+1)):
            
            stati[j][cont]=binario[k]
            cont+=1
    sim=True        

#    for el in stati:
 #       cont=0
        #print (el)
 #       for elem in el:
            
            
 #           if elem=='1':
 #               cont+=1
                #print(cont)
  #      if cont!=(2**(n-1))/2:
 #           sim=False


    if sim==True:        
        simula(n)    

print (stati)
print (maxval[0])
