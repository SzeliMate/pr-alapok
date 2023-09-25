pontok = 0
 
válasz = input('Mi Magyarország fővárosa? ')
if válasz == 'Budapest':
    print('Helyes!')
    pontok = pontok + 1
else:
    print('A válasz helytelen; a helyes válasz Budapest lett volna.')
print()
 
válasz = input('Hány fokon forr a víz? ')
if válasz == '100':
    print('Helyes!')
    pontok = pontok + 1
else:
    print('A válasz helytelen; a helyes válasz 100 lett volna.')
print()
 
válasz = input('Melyik az az állat, amelyiknek nagy füle és hosszú ormánya van? ')
if válasz == 'elefánt':
    print('Helyes!')
    pontok = pontok + 1
else:
    print('A válasz helytelen; a helyes válasz elefánt lett volna.')
print()
 
válasz = input('Hogy mondjuk angolul azt, hogy alma? ')
if válasz == 'apple':
    print('Helyes!')
    pontok = pontok + 1
else:
    print('A válasz helytelen; a helyes válasz apple lett volna.')
print()
 
válasz = input('Mi volt Petőfi vezetéknevű költőnk keresztneve? ')
if válasz == 'Sándor':
    print('Helyes!')
    pontok = pontok + 1
else:
    print('A válasz helytelen; a helyes válasz Sándor lett volna.')
print()
 
százalék = str(100 * pontok / 5) + '%'
print('Az eredmény: ' + százalék)
