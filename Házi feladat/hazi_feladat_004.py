#Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!

#Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"

nap = input("Jó a napod van?(igen/nem) ")

if nap == 'igen':
    print(f"Igen jó napom van!")

elif nap == 'nem':
    print(f"Nem nincs jó napom!")

else:
    print(f"Sajnos nem értem a válaszodat!")