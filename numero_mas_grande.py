print('*************************************************************************')
print('*Programa para determianr  el numero mayor entre tres numeros posibles  *')
print('************************************************************************* \n')

num_uno = float(input('Introduce el primer numero: '))
num_dos = float(input('Introduce el segun numero: '))
num_tres = float(input('Introduce el tercer numero: '))

if num_uno > num_dos and num_uno > num_tres:
    print('El numero,', num_uno, 'es el numero mas grande de los tres. \n')
else: 
    if num_dos > num_tres:
        print('El numero,', num_dos, 'es el numero mas grande de los tres. \n')
    else:
        print('El numero,', num_tres, 'es el numero mas grande de los tres. \n')
        
print('\n Fin del programa')