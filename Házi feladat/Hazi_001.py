#feladat_001
#Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!

#Feladat_001/2
#Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"


nap= input("Jó a napod? ")
if nap == 'igen':
    print(f'A válaszod: {igen}')
elif nap == 'nem':
    print(f'A válaszod:{nem}')
else:
    print(f'Sajnos nem értem a válaszodat!{igen}{nem}')
