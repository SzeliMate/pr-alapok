#Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.

szam = int(input(f"Kérek egy gondolt számot 1-5 között: "))
if szam == 3:
    print(f"Eltaláltad! Ügyes vagy!")

if szam == 4:
    print(f'Majdnem sikerült, de eggyel kevesebb!')

if szam == 5:
    print(f'Majdnem sikerült, de kettővel kevesebb!')

if szam == 2:
    print(f'Majdnem sikerült, de eggyel kevesebb!')

if szam == 1:
    print(f'Majdnem sikerült, de kettővel kevesebb!')

