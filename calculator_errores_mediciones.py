print('===========================================================')
print('Calculador de Desviacion Estandar en un grupo de mediciones')
print('=========================================================== \n')

print('''La Desviacion Estandar de un grupo de medidas es
la medida de dispersión  que indica qué tan dispersos
están los datos con respecto a la media. \n''')
print(' \n Ingresa un maximo de cuatro valores:')
print('======================================== \n')

opcion_uno = float(input('Ingresa la primera medicion: '))
opcion_dos = float(input('Ingresa la segunda medicion: '))
opcion_tres = float(input('Ingresa la tercera medicion: '))
opcion_cuatro = float(input('Ingresa la cuarta medicion: '))

print('\n Tus opciones fueron: \n')

print('Opcion Uno: ',round(opcion_uno,2))
print('Opcion Dos: ', round(opcion_dos,2))
print('Opcion Tres: ', round(opcion_tres,2))
print('Opcion Cuatro: ', round(opcion_cuatro,2))

print('\n Menu de opciones')
print('================ \n')

print('Presiona 1 para calcular el Valor Medio.')
print('Presiona 2 para calcular la Desviacion Estandar.')
print('Presiona 3 para calcular Error Relativo.')
print('Presiona 4 para calcular el Error Porcentual.')
opcion = int(input('\n Indique la opcion deseada: '))

if opcion == 1:
       valor_medio = opcion_uno + opcion_dos + opcion_tres + opcion_cuatro #Ver Formula valor medio (esta es un ejemplo)!
       print('El valor medio de sus mediciones es: ', valor_medio)
       
elif opcion == 2:
    desv_stnd = (opcion_uno + opcion_dos + opcion_tres + opcion_cuatro)*opcion_uno
    print('La Desviacion Estandar de sus mediciones es: ', desv_stnd)
elif opcion == 3:
    error_rel = (opcion_uno + opcion_dos + opcion_tres + opcion_cuatro)*opcion_dos
    print('El Error Relativo de sus mediciones es: ', error_rel)
elif opcion == 4:
    error_porc = (opcion_uno + opcion_dos + opcion_tres + opcion_cuatro)*opcion_tres
    print('El Error Porcentual de sus mediciones es: ', error_porc, '%')
else:
    print('OPCION NO VALIDA')
print('fin')    




















