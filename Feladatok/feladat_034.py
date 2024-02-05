"""
Célnak megfelelően használjuk az in operátorokat.
Példa:
Ellenőrizze, hogy az "alma" szerepel-e a listában:
"""

lista1 = ["alma", "banán", "szőlő"]
if "alma" in lista1:
  print("Igen az alma szerepel a lista1 nevü listában!")

"""
Célnak megfelelően használjuk a not in operátorokat.
Példa:
Ellenőrizze, hogy az "körte" szerepel-e a listában:
"""

lista2 = ["alma", "banán", "szőlő"]
if "körte" not in lista1:
  print("Igen az körte nem szerepel a lista1 nevü listában!")

"""
Feladat: Készíts programot, ami egy-egy listában tárolja a felhasználóneveket, és a jelszavakat.
A program kérje a felhasználónevet és jelszót, addig amíg helyeset nem adtunk meg.
A program megengedi, hogyegy  másik felhasználó jelszavával is belépjünk.
Belépés után írassuk ki, hogy belépésed sikeres.
Egy enter leütésével lépjünk ki a programból, ami kiírja, hogy kiléptem a programból.
"""  


felhasznalonevek=["fh1", "fh2", "fh3"]
felhasznalonev=None
jelszavak=["jelszo_fh1", "jelszo_fh2", "jelszo_fh3"]
jelszo=None
print(f"A felhasználónevek: {felhasznalonevek}")

Igaz=True

while Igaz:
    felhasznalonev = input("Kérek egy felhasználónevet: ")
    if felhasznalonev in felhasznalonevek:
        break

while True: # a ciklus addig fut amíg a feltétel igaz
    jelszo = input("Kérek egy jelszavat: ")
    if jelszo in jelszavak:
        break

print("belépésed sikeres")

while True:
    kilepes = input("")
    if kilepes == "":
        print("kiléptem a programból")