print('**************************************************************')
print('*Programa para determianr si un numero entero es par o impar *')
print('************************************************************** \n')

numero = int(input('Por favor introduce un numero entero: '))

if numero % 2 == 0:
    print('El numero', numero,  'es par')
elif numero % 2 == 1:
    print('El numero', numero, 'es impar')
else:
    print('Error')
print('Fin de programa')