import tkinter as tkk
from tkinter import *
import time
import sys

tk = Tk()
canvas=Canvas(tk,width=700,height=700)
canvas.pack()


def countingSort(niz,vizualizacija=0):
    
    if vizualizacija==0:
        velicina=max(niz)+1
        sortirani_niz=[0 for i in range(len(niz))] 
        histogram=[0 for i in range(velicina)] 
         
        for i in niz:           #brojanje
            histogram[i]+=1
    
        
        for i in range(1,velicina):         #sabiranje
            histogram[i]=histogram[i]+histogram[i-1] 
    
        for i in niz:       #sortiranje
            sortirani_niz[histogram[i]-1]=i
            histogram[i]-=1
            
        return sortirani_niz 
       
    x1=10
    y1=10
    x2=40
    y2=40
    velicina=max(niz)+1
    sortirani_niz=[0 for i in range(len(niz))] 
    histogram=[0 for i in range(velicina)] 
    
    time.sleep(1)
    
    
    pozicija=0      #prvi red
    for i in niz:
        canvas.create_rectangle(x1+(20+x2-x1)*pozicija,y1,x2+(20+x2-x1)*pozicija,y2,fill="green")
        canvas.create_text(x1+(20+x2-x1)*pozicija+15,y1+15,fill="white",font="Times 20 bold",text=str(i))
        tk.update()
        pozicija+=1
    pozicija+=1
    canvas.create_text(x1+(20+x2-x1)*pozicija+15,y1+15,fill="SlateBlue1",font="Times 18 bold",text="Ulazni niz")
    tk.update()
    time.sleep(5)
    
    y1=150
    y2=180  
    pozicija=0      #drugi red
    for i in histogram:
        canvas.create_rectangle(x1+(20+x2-x1)*pozicija,y1,x2+(20+x2-x1)*pozicija,y2,fill="green")
        canvas.create_text(x1+(20+x2-x1)*pozicija+15,y1+15,fill="white",font="Times 20 bold",text=str(i))
        canvas.create_text(x1+(20+x2-x1)*pozicija+15,y1-10,fill="SlateBlue1",font="Times 10 bold",text=str(pozicija))
        tk.update()
        pozicija+=1
    pozicija+=1    
    canvas.create_text(x1+(20+x2-x1)*pozicija+15,y1+15,fill="SlateBlue1",font="Times 18 bold",text="Histogram")
    canvas.create_text(x1+(20+x2-x1)*pozicija+15,y1-10,fill="SlateBlue1",font="Times 10 bold",text="Indexi")
    tk.update()
    time.sleep(5)    
    uputstvo=canvas.create_text(x1,y1+200+140,fill="SlateBlue1",anchor=tkk.SW,font="Times 20 bold",text="Prvo je potrebno da prebrojimo broj ponavaljanja svakog\nelementa ulaznog niza te rezultat smjestimo u histogram.")
    tk.update()   
    
    pozicija=0    
    for i in niz:           #brojanje
        histogram[i]+=1
        canvas.create_rectangle(x1+(20+x2-x1)*i,y1,x2+(20+x2-x1)*i,y2,fill="green")
        canvas.create_text(x1+(20+x2-x1)*i+15,y1+15,fill="white",font="Times 20 bold",text=str(histogram[i]))
        strijelica=canvas.create_line(x1+(20+x2-x1)*i+15, y1-50, x1+(20+x2-x1)*i+15, y1-20,arrow=tkk.LAST)
        krug=canvas.create_oval(x1+(20+x2-x1)*pozicija-3, y1-140-3, x2+(20+x2-x1)*pozicija+3, y2-140+3,width=2.5,outline='red')
        tk.update()
        time.sleep(1.5)  #bilo 1
        canvas.delete(strijelica)
        canvas.delete(krug)
        tk.update()
        pozicija+=1
    
    canvas.delete(uputstvo)
    tk.update()
    uputstvo=canvas.create_text(x1,y1+200+140,fill="SlateBlue1",anchor=tkk.SW,font="Times 20 bold",text="Zatim sabiremo susjedne članove niza histograma sa lijeva na desno.")
    tk.update()
    time.sleep(5)
    
    for i in range(1,velicina):         #sabiranje
        histogram[i]=histogram[i]+histogram[i-1] 
        plus=canvas.create_text(x1+(20+x2-x1)*(i-1)+40,y1+15,fill="red",font="Times 20 bold",text="+")
        strijelica=canvas.create_line(x1+(20+x2-x1)*i+15, y1-50, x1+(20+x2-x1)*i+15, y1-20,arrow=tkk.LAST)
        tk.update()
        time.sleep(1)   #bilo 0.7
        canvas.create_rectangle(x1+(20+x2-x1)*i,y1,x2+(20+x2-x1)*i,y2,fill="green")
        canvas.create_text(x1+(20+x2-x1)*i+15,y1+15,fill="white",font="Times 20 bold",text=str(histogram[i]))
        tk.update()
        time.sleep(1)  #bilo 0.7
        canvas.delete(strijelica)
        canvas.delete(plus)
        tk.update()
        
    canvas.delete(uputstvo)
    uputstvo=canvas.create_text(x1,y1+200+140,fill="SlateBlue1",anchor=tkk.SW,
                                font="Times 20 bold",text="Idemo kroz ulaz i tražimo vrijednost histograma na onom\nindexu koji je jednak trenutnom elementu ulaza do kojeg\nsmo došli i u izlazni niz upisujemo vrijednost ulaznog\nelementa na indexu koji odgovara vrijednosti histograma,\nte vrijednost histograma umanjujemo za 1")
    tk.update()
    time.sleep(5)
    pozicija=0
    for i in niz:  #prazan zadnji red
        canvas.create_rectangle(x1+(20+x2-x1)*pozicija,y1+140,x2+(20+x2-x1)*pozicija,y2+140,fill="green")
        canvas.create_text(x1+(20+x2-x1)*pozicija+15,y1-10+140,fill="SlateBlue1",font="Times 10 bold",text=str(pozicija+1))
        
        pozicija+=1
        tk.update()
    pozicija+=1
    canvas.create_text(x1+(20+x2-x1)*pozicija+15,y1+15+140,fill="SlateBlue1",font="Times 18 bold",text="Izlazni niz")
    tk.update()   
    time.sleep(1)
    pozicija=0
    for i in niz:       #sortiranje
        sortirani_niz[histogram[i]-1]=i
        canvas.create_rectangle(x1+(20+x2-x1)*(histogram[i]-1),y1+140,x2+(20+x2-x1)*(histogram[i]-1),y2+140,fill="green")
        krug=canvas.create_oval(x1+(20+x2-x1)*pozicija-3, y1-140-3, x2+(20+x2-x1)*pozicija+3, y2-140+3,width=2.5,outline='red')
        canvas.create_text(x1+(20+x2-x1)*(histogram[i]-1)+15,y1+15+140,fill="white",font="Times 20 bold",text=str(i))
        strijelica1=canvas.create_line(x1+(20+x2-x1)*(histogram[i]-1)+15, y1-50+140, x1+(20+x2-x1)*(histogram[i]-1)+15, y1-20+140,arrow=tkk.LAST)
        strijelica=canvas.create_line(x1+(20+x2-x1)*i+15, y1-50, x1+(20+x2-x1)*i+15, y1-20,arrow=tkk.LAST)
        tk.update()
        time.sleep(3)   #bilo 1
        histogram[i]-=1
        canvas.create_rectangle(x1+(20+x2-x1)*i,y1,x2+(20+x2-x1)*i,y2,fill="green")
        canvas.create_text(x1+(20+x2-x1)*i+15,y1+15,fill="white",font="Times 20 bold",text=str(histogram[i]))
        tk.update()
        pozicija+=1
        tk.update()
        canvas.delete(strijelica)
        canvas.delete(strijelica1)
        canvas.delete(krug)
        tk.update()
    pozicija+=1    
    
    canvas.delete(uputstvo)
    tk.update()   
    return sortirani_niz
        
    
niz=[]
for i in range(1,len(sys.argv)):
    niz.append(int(sys.argv[i]))
    
print(countingSort(niz,1))
    