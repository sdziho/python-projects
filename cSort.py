
def countSort(niz):
    velicina=max(niz)+1
    sortirani_niz=[0 for i in range(len(niz))] 
    histogram=[0 for i in range(velicina)] 
    
    for i in niz:
        histogram[i]+=1
    
    for i in range(1,velicina):
        histogram[i]=histogram[i]+histogram[i-1]
        
    
    
    for i in niz:
        sortirani_niz[histogram[i]-1]=i
        histogram[i]-=1
        
    return sortirani_niz
        
    

print(countSort([4,5,2,7,1,8,3]))