<<<<<<< HEAD
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
=======
print('Sistema para calcular el promedio de notas en tres materias: ')
nombre = input('Para comenzar, cual es tu nombre?: ')
nota_mate = float(input(nombre +', Cual es tu nota en math?: '))
nota_che = float(input(nombre + ', cual es tu nota en química?: '))
nota_bio = float(input(nombre + ', cual es tu nota en biología?: '))

print('Wait a few seconds')

promedio = (nota_mate + nota_che + nota_bio)/3
print('Tu promedio fue de: ', round(promedio,2))

if promedio >=5:
    print("Lo lograste")
else:
    print('''
Has reprobado''')

print('Sigue intentando')
>>>>>>> dd70c8b4391d639cb5ecacb4f3223ba8a9c67cb2