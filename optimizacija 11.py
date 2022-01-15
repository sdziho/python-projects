
b1=[1,1,0,1,1,1,0,0,0,1,0]
Bc=[]
Bc.append(b1)
for i in range(len(b1)-1):
    bn=b1[1:]
    bn.append(b1[0])
    Bc.append(bn)
    b1=bn

B=[]

for i in range(len(Bc)):
    B.append(Bc[i])
    B[i].append(1)

zadnji_red=[]
for i in range(len(b1)-1):
    zadnji_red.append(1)
zadnji_red.append(0)
B.append(zadnji_red)

I=[]

for i in range(len(B)):
    red=[]
    for j in range(len(b1)):
        if i==j:
            red.append(1)
        else:
            red.append(0)
    I.append(red)
    
G=[] #G=BI
for i in range(len(B)):
    red=[]
    red.extend(B[i])
    red.extend(I[i])
    G.append(red)
    
H=[] #G=IB
for i in range(len(B)):
    red=[]
    red.extend(I[i])
    red.extend(B[i])
    H.append(red)
    
print("B=")
for i in B:
    print(i)

print("\nG=")
for i in G:
    print(i)

print("\nH=")
for j in H:
    print(j)