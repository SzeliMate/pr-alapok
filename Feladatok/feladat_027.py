#lista bejárása
tantargyak = ['matek', 'töri', 'bio','kémia', 'info']
szamlalo = 0
index = 0
for tantargy in tantargyak:
    print(f'A tantargyak lista {index} elem: {tantargy}')
    szamlalo = szamlalo + 1
    index = index + 1
print(f'{szamlalo} szamlalo eleme van tantargyak listanak.')