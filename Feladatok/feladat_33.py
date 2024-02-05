
"""
Listák rendezése ideiglenesen és maradandóan
"""

nyelvek = ['Python', 'C', 'C++', 'Java']

# sorted() FÜGGVÉNY: lista elemeinek eredeti sorrendje nem változik,
# csak rendezetten kerülnek kiírásra
print(sorted(nyelvek))  
print(nyelvek)

# sort() METÓDUS: lista felülírása, az elemek eredeti sorrendje megváltozik,
# rendezett lesz
nyelvek.sort()
print(nyelvek)
 

rendezetlen_lista_indexek = [0, 1, 2, 3, 4, 5, 6, 7]
rendezetlen_lista_ertekek = [6, 5, 3, 1, 8, 7, 2, 4]

rendezett_lista_ertekek = [1, 2, 3, 4, 5, 6, 7, 8]


# Buborékos rendezés Pythonban

"""Az algoritmus újra és újra végigiterál a listán, összehasonlítja a lista szomszédos elemeit, és ha azok az elvárt rendezéshez képest fordítva vannak, akkor megcseréli őket. Első menetben a lista elejéről indul és a végéig megy. Ennek az első menetnek az eredményeként a legnagyobb elem (mint egy buborék) felszáll a lista végére. Így a következő menetben már elegendő az utolsó előtti elemig elvégezni a szomszédos elemek összehasonlítását és cseréjét. Az ezután következő menetben a lista utolsó két eleme lesz a helyén és így tovább. Az algoritmus két egymásba ágyazott ciklusból áll."""

t = [6, 5, 3, 1, 8, 7, 2, 4]
lista_hossza=len(t)
print(f"A lista hossza: {lista_hossza}")
for i in range(lista_hossza-1, 0, -1):
    for j in range(0, i):
        if t[j] > t[j+1]:    
            tmp= t[j+1]
            t[j+1]= t[j]
            t[j]= tmp
    print(f"{t} i = {i} j = {j}")

"""A lista hossza: 8
[5, 3, 1, 6, 7, 2, 4, 8] i = 7 j = 6
[3, 1, 5, 6, 2, 4, 7, 8] i = 6 j = 5
[1, 3, 5, 2, 4, 6, 7, 8] i = 5 j = 4
[1, 3, 2, 4, 5, 6, 7, 8] i = 4 j = 3
[1, 2, 3, 4, 5, 6, 7, 8] i = 3 j = 2
[1, 2, 3, 4, 5, 6, 7, 8] i = 2 j = 1
[1, 2, 3, 4, 5, 6, 7, 8] i = 1 j = 0
"""


"""Az algoritmust gyorsabbá tehetjük, ha figyeljük a cseréket. Ha a belső ciklusnál nincs csere, akkor kilépünk a ciklusból, a lista már rendezett."""

# Ha nincs csere készen vagyunk!

# A rendezetlen lista:
t = [6, 5, 3, 1, 8, 7, 2, 4]
print(t)
csere_volt = None
rendezetlen_lista_hossza=len(t)
for i in range(rendezetlen_lista_hossza-1, 0, -1):
    csere_volt = False
    for j in range(0, i):
        if t[j] > t[j+1]:
            csere_volt = True    
            tmp= t[j+1]
            t[j+1]= t[j]
            t[j]= tmp
            # t[j], t[j+1] = t[j+1], t[j]
    if not csere_volt:
      break
    print(f"{t} i = {i} j = {j}")


 
"""
# A rendezetlen lista:
[6, 5, 3, 1, 8, 7, 2, 4]

[5, 3, 1, 6, 7, 2, 4, 8] i = 7 j = 6
[3, 1, 5, 6, 2, 4, 7, 8] i = 6 j = 5
[1, 3, 5, 2, 4, 6, 7, 8] i = 5 j = 4
[1, 3, 2, 4, 5, 6, 7, 8] i = 4 j = 3
[1, 2, 3, 4, 5, 6, 7, 8] i = 3 j = 2
[1, 2, 3, 4, 5, 6, 7, 8] i = 2 j = 1
[1, 2, 3, 4, 5, 6, 7, 8] i = 1 j = 0

if not csere_volt:                     # Ha nincs csere, készen vagyunk!
    break                              # Ha nincs csere, készen vagyunk!

# A rendezetlen lista:
[6, 5, 3, 1, 8, 7, 2, 4]

[5, 3, 1, 6, 7, 2, 4, 8] i = 7 j = 6
[3, 1, 5, 6, 2, 4, 7, 8] i = 6 j = 5
[1, 3, 5, 2, 4, 6, 7, 8] i = 5 j = 4
[1, 3, 2, 4, 5, 6, 7, 8] i = 4 j = 3
[1, 2, 3, 4, 5, 6, 7, 8] i = 3 j = 2
"""