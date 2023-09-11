# feladat_002
"""
Kérjünk be a billentyűzetről a két egész számot és írassuk ki a két szám összegét képernyőre!
"""

szam_1 = input("Kérek egy számot: ")
szam_1 = int(szam_1)

szam_2= int(input("Kérek egy másik számot: "))
szam_3 = float(szam_1)

osszeg = szam_1 + szam_2

print(f"A megadott két szám összege: {szam_1 + szam_2}")
print(f"A megadott két szám összege: {osszeg}")
print(f"A szam_1 valtozó típusa: {type(szam_1)}")
print(f"A szam_2 valtozó típusa: {type(szam_2)}")
print(f"A osszeg valtozó típusa: {type(osszeg)}")
print(f"A szam_3 változó értéke: {szam_3}")
print(f"A osszeg valtozó típusa: {type(szam_3)}")