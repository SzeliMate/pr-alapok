#eljárás - program
def koszont_nevvel(vnev, knev):
        print('Szia '+ vnev + knev +', üdv a fedélzeten!')

koszont_nevvel('Kiss ','Ádám')


print('---------------------------------')

#függvény - érték
def koszont_nevvel1(nev1):
            uzenet = 'Szia '+ nev1 +', üdv a fedélzeten!'
            if uzenet == 'Ádám1':
                return 'Ádám1'
            else:
                return('Hiba')    

print(koszont_nevvel1('Ádám1'))

print('---------------------------------')