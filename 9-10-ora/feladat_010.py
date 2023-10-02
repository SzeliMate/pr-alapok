"""
A feladat_003 kibővítése:
0 éves ---> Még nem születtél meg!
1|2|3|4|5 éves vagy, még nem jársz általános iskolába!
6|7|...|13|14 éves vagy, általános iskolába jársz!
15|16|...|63|64 éves vagy, tanulsz vagy dolgozol!
65 vagy több éves vagy, nyugdíjas.
"""
              
print(f'Üdv néked!')
évek_száma = input('Hány éves vagy?')
évek_száma = int(évek_száma)
if évek_száma == 0:
    print('Még nem születtél meg!')
elif évek_száma <=5:
   print('Még nem jársz általános iskolába!')
elif évek_száma <= 14:
    print('Általános iskolában jársz.')
elif évek_száma <=64:
    print('Tanulsz vagy dolgozol!')
elif évek_száma >=65:
   print('Nyugdíjas vagy.')     
