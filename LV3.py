
string = 'EACAEAABAAEDAEA'


class NodeTree(object):
    def __init__(self, right=None, left=None):
        self.left = left
        self.right = right
    def ispitaj(self,right=None, left=None):
        return type(self.right)==type(self.left)

cvor = {}
for c in string:
    if c in cvor:
        cvor[c] += 1
    else:
        cvor[c] = 1

cvor = sorted(cvor.items(), key=lambda x: x[1], reverse=True)
ispis=cvor

while len(cvor) > 1:
    (key1, c1) = cvor[-1]
    (key2, c2) = cvor[-2]
    cvor = cvor[:-2]
    node = NodeTree(key1, key2)
    cvor.append((node, c1 + c2))

code=list()

lista=cvor[0][0]
for i in range(len(ispis)):
    code.append("")
forb=list()          
while True:
    for i in range(len(ispis)):
        if ispis[i][0]!=lista.left:
            if (ispis[i][0] in forb) ==False:
                code[i]+="1"
            
        else:
            code[i]+="0"
            forb.append(ispis[i][0])
    #print(forb)        
    if lista.ispitaj()==True:
        break
    lista=lista.right

lista_slova=list()
for i in range(len(code)):
    lista_slova.append(ispis[i][0])


for i in range(len(code)):
    print(lista_slova[i], code[i])
    

kodirana_rec=""
for c in string:
    for i in range(len(code)):
        if c==lista_slova[i]:
            kodirana_rec+=code[i]
            
print("Kodirana recenica glasi",kodirana_rec)
print("Stepen kompresije je ", len(string)*8/len(kodirana_rec))

    
    