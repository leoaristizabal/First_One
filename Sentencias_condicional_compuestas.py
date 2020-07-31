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
