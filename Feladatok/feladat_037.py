import random


utvonal_magassagai = [random.randint(0, 9) for _ in range(30)]


meredek_elore = 0
meredek_vissza = 0


for i in range(1, len(utvonal_magassagai)):
    if utvonal_magassagai[i] >= utvonal_magassagai[i - 1] + 2:
        meredek_elore += 1


for i in range(len(utvonal_magassagai) - 2, -1, -1):
    if utvonal_magassagai[i] >= utvonal_magassagai[i + 1] + 2:
        meredek_vissza += 1

print("Az úton előre", meredek_elore, "meredek szakasz van.")
print("Az úton visszafelé", meredek_vissza, "meredek szakasz van.")