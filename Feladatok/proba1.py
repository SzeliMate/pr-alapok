#Eljárás
def menut_kiir(tipus):
    '''
    A menű megjelenítése aképernyőn
    '''
    if tipus == 2:
        print('1.Új adat bevitele')
        print('2.Kilépés a programból')
    
    elif tipus == 3:
        print('1.Új adat bevitele')
        print('2.Adatok módosítása / törlése')
        print('3.Kilépés a programból')

    else:
        print(f'A megadott menüszám {menu_szama} érvénytelen')
menu_szama = int(input('Kérek egy menü számot: '))

#Eljárás hívása
menut_kiir(menu_szama)