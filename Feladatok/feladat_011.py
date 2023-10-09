
"""
Kérjük be két egész számot szam1, szam2.
Hasonlítsuk össze a két számot és írassuk ki, hogy a "szam1 kisebb, mint a szam2",
vagy a "szam2 kisebb mint szam1",
vagy a "szam1 egyenlő szam2-vel"
"""

szam1=input("Írj be egy számot /szam1/")
szam2=input("Írj be mégegy számot /szam2/")
szam1=int(szam1)
szam2=int(szam2)

#-------------------
"""
if szam1 < szam2:
    print(f"A szám1 kisebb, mint szám2")
if szam2 < szam1:
    print(f'A szám2 kisebb, mint a szám1')
if szam1==2:
    print(f'szám1 egyenlő a szám2-vel')
"""
"""
if szam1 < szam2:
    print(f"A szám1 kisebb, mint szám2")
elif szam2 < szam1:
    print(f'A szám2 kisebb, mint a szám1')
else:
    print(f'szám1 egyenlő a szám2-vel')
 """
'''
if szam1 < szam2:
    print(f"A szám1 kisebb, mint szám2")
if szam2 < szam1:
    print(f'A szám2 kisebb, mint a szám1')
if szam1==szam2:
    print(f'szám1 egyenlő a szám2-vel')
    '''
#-------------------

if szam1 < szam2:
    print(f"A szám1 kisebb, mint szám2")
elif szam2 < szam1:
    print(f'A szám2 kisebb, mint a szám1')
elif szam1==szam2:
    print(f'szám1 egyenlő a szám2-vel')