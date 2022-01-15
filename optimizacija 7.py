"""
Napravite program koji će za danu listu uređenih parova cijelih brojeva napraviti novu listu 
u kojoj će ostati samo oni parovi u kojima je prvi element manji od drugoga.
Kada dobiješ novu listu treba vratiti one parove koji imaju najveću sumu prvog i drugog člana.
Npr. za listu [(5,1),(2,5),(7,6),(3,9),(2,10),(4,3),(1,2)] 
prvo se dobije [(2,5),(3,9),(2,10),(1,2)],
a zatim se vraća listu [(3,9),(2,10)] jer se maksimalan zbroj 12 postiže za ta dva elementa.
"""
lista=[(5,1),(2,5),(7,6),(3,9),(2,10),(4,3),(1,2)] 
nova_lista=[]
for i in lista:
    if i[0]<i[1]:
        nova_lista.append(i)

maks=0
for i in nova_lista:
    if i[0]+i[1]>maks:
        maks=i[0]+i[1]

maks_lista=[]
for i in nova_lista:
    if i[0]+i[1]==maks:
        maks_lista.append(i)


"""
Napiši funkciju koja  će kao argument primiti neki string (rečenicu), 
a kao rezultat vratiti sortiranu listu uredenih parova riječi i broja pojavljivanja te riječi u stringu.
Napomena: treba koristiti rječnike i sve riječi prebaciti u string s malim slovima te izbaciti točke i zareze.
Npr. za tekst: 
"Jednom davno u kraljevstvu iza sedam mora, sedam gora, sedam rijeka i sedam planina živio strašni zmaj u svojoj pećini."
treba dobiti rezultat: 
[('davno', 1), ('gora', 1), ('i', 1), ('iza', 1), ('jednom', 1), ('kraljevstvu', 1), ('mora', 1), ('pećini', 1), ('planina', 1), ('rijeka', 1), ('sedam', 4), ('strašni', 1), ('svojoj', 1), ('u', 2), ('zmaj', 1), ('živio', 1)]
"""

def funkcija(s):
    rijeci=s.split()
    nove_rijeci=[]
    for i in rijeci:
        i=i.lower()
        if i.find('.')>=0 or i.find(',')>=0:
            i=i[:-1]
        nove_rijeci.append(i)
    
    rijecnik={}
    for i in nove_rijeci:
        rijecnik[i]=rijecnik.get(i,0)+1 #brojanje u rijecniku
        
    print(rijecnik)

funkcija("Jednom davno u kraljevstvu iza sedam mora, sedam gora, sedam rijeka i sedam planina živio strašni zmaj u svojoj pećini.")