#be: szam
#ki: a szám negatív

def bekert_egy_szamot():
    szam = int(input("Kérek egy számot: "))
    print(szam)


def bekert_egy_szamot1(parameter1):
    szam1 = int(input("Kérek egy számot: "))# 50
    szam1 = szam1 + parameter1
    print(szam1)

def szamok_osszege():
    return 15+9


bekert_egy_szamot()
bekert_egy_szamot()
bekert_egy_szamot1(100) #150
osszeg= szamok_osszege()
print(osszeg)
szamok_osszege()



"""
szam = int(input("Adj meg egy számot! "))
if szam < 0:
    print(f"A megadott szám {szam} negatív")
print(f">> A program vége!<<")
"""
"""
#be: szam
#ki: a szam negatív, vagy nem negatív
szam = int(input('Adj meg egy számot! '))
if szam < 0:
    print(f'A megadott szám {szam} negatív.')
else:
    print(f'A megadott szám nemnegatív.')
print(f'>> A program vége! <<')
"""