#feladat_001
#Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!

#Feladat_001/2
#Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"

nem = 0
igen = 0
igen= input("Jó a napod? ")
if igen == igen:
    print(f'A válaszod: {igen}')
elif nem == nem:
    print(f'A válaszod:{nem}')
else:
    print(f'Sajnos nem értem a válaszodat!{igen}{nem}')