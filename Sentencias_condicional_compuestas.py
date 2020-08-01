print('Calcula tu promedio pav perrito: ')
nombre = input('Para comenzar, cual es tu nombre?: ')
nota_mate = float(input(nombre +', Cual es tu nota en mate llae?: '))
nota_che = float(input(nombre + ', cual es tu nota en quimica llae?: '))
nota_bio = float(input(nombre + ', cual es tu nota en biologia mano?: '))

print('''verga esto esta arrecho de calcular manaure, pero tu confia.
Vamos a ver qlq''')

promedio = (nota_mate + nota_che + nota_bio)/3
print('Aja mano tu promedio fue de ', round(promedio,2))


if promedio >=10:
    print('''Perrito lo lograste llae!!!
Coronamos''')
else:
    print('''Verga mano, no hay manera.
Estas clavadisimo''')

print('Dejalo asi mano, dale por ahi')
