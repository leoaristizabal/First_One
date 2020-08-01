<<<<<<< HEAD
# Sentencias condicionales anidadas.}

print('=========')
print('Conversor')
print('=========\n')

print('Menu de Opciones: ')
print('================= \n')

print('Presiona 1 para convertir de numero a palabra.')
print('Presiona 2 para convertir de palabra a numero. \n')

opcion = int(input('Indica la opcion deseada: '))

if opcion == 1:
    print('\n Conversor de numero a palabra. \n')
    opcion_uno = int(input('Indica el numero a convertir y presiona Enter: '))

    if opcion_uno == 1:
        print('El numero es "UNO"')
    elif opcion_uno == 2:
        print('El numero es "DOS"')
    elif opcion_uno == 3:
        print('El numero es "TRES"')
    elif opcion_uno == 4:
        print('El numero es "CUATRO"')
    elif opcion_uno == 5:
        print('El numero es "CINCO"')
    elif opcion_uno == 0:
        print('El numero es "CERO"')
    else:
        print('El numero seleccionado no esta registrado')

elif opcion == 2:
    print('\n Conversor de palabra a numero. \n')
    
    opcion_dos = input('\n Ingrese la palabra a convertir y presiona Enter: \n')
    
    if opcion_dos == 'uno':
        print('El numero es "1"')
    elif opcion_dos == 'dos':
        print('El numero es "2"')
    elif opcion_dos == 'tres':
        print('El numero es "3"')
    elif opcion_dos == 'cuatro':
        print('El numero es "4"')
    elif opcion_dos == 'cinco':
        print('El numero es "5"')
    elif opcion_dos == 'cero':
        print('El numero es "0"')
    else:
        print('La palabra seleccionada no esta registrada')
    
     
else:
    print('Opcion no valida')
print('Fin.')














    
=======
# Sentencias condicionales anidadas.}

print('=========')
print('Conversor')
print('=========\n')

print('Menu de Opciones: ')
print('================= \n')

print('Presiona 1 para convertir de numero a palabra.')
print('Presiona 2 para convertir de palabra a numero. \n')

opcion = int(input('Indica la opcion deseada: '))

if opcion == 1:
    print('\n Conversor de numero a palabra. \n')
    opcion_uno = int(input('Indica el numero a convertir y presiona Enter: '))

    if opcion_uno == 1:
        print('El numero es "UNO"')
    elif opcion_uno == 2:
        print('El numero es "DOS"')
    elif opcion_uno == 3:
        print('El numero es "TRES"')
    elif opcion_uno == 4:
        print('El numero es "CUATRO"')
    elif opcion_uno == 5:
        print('El numero es "CINCO"')
    elif opcion_uno == 0:
        print('El numero es "CERO"')
    else:
        print('El numero seleccionado no esta registrado')

elif opcion == 2:
    print('\n Conversor de palabra a numero. \n')
    
    opcion_dos = input('\n Ingrese la palabra a convertir y presiona Enter: \n')
    opcion_dos = opcion_dos.lower()
    
    if opcion_dos == 'uno':
        print('El numero es "1"')
    elif opcion_dos == 'dos':
        print('El numero es "2"')
    elif opcion_dos == 'tres':
        print('El numero es "3"')
    elif opcion_dos == 'cuatro':
        print('El numero es "4"')
    elif opcion_dos == 'cinco':
        print('El numero es "5"')
    elif opcion_dos == 'cero':
        print('El numero es "0"')
    else:
        print('La palabra seleccionada no esta registrada')
    
     
else:
    print('Opcion no valida')
print('Fin.')














    
>>>>>>> dd70c8b4391d639cb5ecacb4f3223ba8a9c67cb2
