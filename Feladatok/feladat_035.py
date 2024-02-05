import random

dobasok = []
for _ in range (100):
    dobas = random.randint(1,6)
    dobasok.append(dobas)

ennyi_hatos = 0
for dobas in dobasok:
    if dobas == 6:
        ennyi_hatos += 1

print(f'Összesen, {ennyi_hatos} hatost dobtunk.') 