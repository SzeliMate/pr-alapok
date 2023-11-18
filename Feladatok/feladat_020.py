
'''
A print függvény a megadott szöveg kiírása után sort emel, 
vagyis a következő print függvény már egy újabb sorba ír.
Az alapértelmezett viselkedés azonban felülírható a "t" paraméterrel.
'''
# a kiírást követően a kurzor egy tabulátornyit ugrik
print('Teszt', end='\t')
print('Teszt', end='\t')
print('Teszt', end='\t')

print()

# a kiírást követően a kurzor a kiírás végén marad
print('Teszt', end='')
print('Teszt', end='')
print('Teszt', end='')       
