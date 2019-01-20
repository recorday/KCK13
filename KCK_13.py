import pandas as pd
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag

dane=pd.read_excel(r"D:\Users\dom\Desktop\HCI-13\sub1trial13.xlsx", sep=',t', delimiter=',')
# print(dane)
kolumnab=dane["sygn_1"]
kolumnaf=dane["liczby"]

#t = np.linspace (0, 37.85, 37.85*200)
#plt.plot(t, kolumnab)
#plt.xlabel("Czas [s]")
#plt.ylabel("Amplituda [-]")
#plt.show()
#
#
##filtr1
#przefiltrowany=ag.pasmowozaporowy(kolumnab, 200, 49, 51)
#plt.plot(t,przefiltrowany)
#plt.xlabel('Czas [s]')
#plt.ylabel('Amplituda [-]')
#plt.show()
#
##filtr2
#przefiltrowany2=ag.pasmowoprzepustowy(przefiltrowany, 200, 1, 50)
#plt.plot(t, przefiltrowany2)
#plt.xlabel('Czas [s]')
#plt.ylabel('Amplituda [-]')
#
#plt.show()

lista1=[]
lista=[]
for i in range(26):  
    
    listawar=[]
    daneprog=dane['sygn_1']
    liczba=dane['liczby']
    warunek1=(daneprog>=1.05)&(liczba==i)
    Liczwar=warunek1.value_counts()
#    print("Wartoć dla ",i, "sekundy: ", warunek1.value_counts())
    listawar.extend(Liczwar)
    if listawar[0] == 7570:
        lista.append(0)
        lista1.append(0)
    else:
        lista.append(1)
        lista1.append(1)
#print(lista) 
   


for z in range(1,6):
    
    liczba=0
    for h in range(1,6): 
        if lista[1]==1:
            liczba+=1
        elif lista[1]==0:
            liczba+=0
        lista.remove(lista[1])
    print("Liczba mrugnięć przy ",z, " wyswietleniu serii cyfr: ",liczba)
    

    
lista2=[0,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
for n in range(26):
    if lista1[n]==1:
        lista1[n]=lista2[n]
#print(lista1)

for m in lista1[:]:
    if m==0:
        lista1.remove(m)
print("Kombinacja cyfr wybrana przez osobe badaną: ", lista1)
#print(dane[dane.sygn_1>0.15]['liczby'])
#&(liczba<3)