print('Introduce dos numeros a comparar: \n')

num_uno = float(input('Introduce el primero numero: '))
num_dos = float(input('Introduce el segundo numero: '))

print(' \n Los numeros a comparar son: ', num_uno, 'y', num_dos, '\n')

if num_uno > num_dos:
    print('- El primer numero es mayor que el segundo \n')

if num_uno < num_dos:
    print('- El primer numero es menor que el segundo \n')
if num_uno == num_dos:
    print('- Los numeros son iguales \n')
if num_uno != num_dos:
    print('- Los numeros son diferentes \n')
if num_uno <= num_dos:
    print('- El primer numero es menor o igual que el segundo \n')
if num_uno >= num_dos:
    print('- El primer numero es mayor o igual que el segundo \n')
else:
    print('Comando no valido')
print('Fin del programa')
