#1 és 10 közötti (a határokat is beleértve, tehát lehet 1 és 10 is) szám generálása
import random
szam = int(input("Kérek egy számot: "))
random_szam = random.randint(1, 3)
if szam == random_szam:
    print(f'Eltaláltad! A helyes szám {random_szam}')
else:
    print(f'Buktad')


