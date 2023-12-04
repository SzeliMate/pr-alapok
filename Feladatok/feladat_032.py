honapok = ['január', 'február','március', 'április', 'május', 'június']

for honap in honapok:
    # az eredeti listaelem NEM módosul!
    honap = honap.upper()

for index in range(len(honapok)):
    #az eredeti listaelem módosul!
    honapok[index] = honapok[index].upper()
print(honapok)

for index in range(len(honapok)):
    # az eredeti listaelem módosul!
    honapok[index] = honapok[index].lower()
print(honapok)

for index in range(0,len(honapok),2):
    # az eredeti listaelem módosul!
    honapok[index] = honapok[index].upper()
print(honapok)