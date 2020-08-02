print('======================================')
print("""SISTEMA PARA DETERMINAR lOS DIAS
DE VACACIONES DE TRABAJADORES EN 
UNA EMPRESA""")
print('====================================== \n')

print('''\n Tipos de Claves: 

Clave 1: Departamento de Atencion al Cliente.
Clave 2: Departamento de Logística
Clave 3: Gerencia. \n ''')

nombre = input('Indica tu nombre y presiona enter: ')
clave = int(input('Indica el numero de la clave de departamento:'))
años_antiguedad = int(input('Indica tus años de antiguedad (en numero): \n'))

if clave == 1:
    if años_antiguedad == 1:
        print(nombre + ', usted tiene derecho a 6 dias de vacaciones. \n')
    elif años_antiguedad >= 2 and años_antiguedad <= 6:
        print(nombre + ', usted tiene derecho a 14 dias de vacaciones. \n')
    elif años_antiguedad >= 7:
        print(nombre + ', usted tiene derecho a 20 dias de vacaciones. \n')
    else:
        print('Sin derecho a vacaciones.\n')
    print('Fin del programa')
elif clave == 2:
    if años_antiguedad == 1:
        print(nombre + ', usted tiene derecho a 7 dias de vacaciones.\n' )
    elif años_antiguedad >= 2 and años_antiguedad <= 5:
        print(nombre + ', usted tiene derecho a 15 dias de vacaciones. \n')
    elif años_antiguedad >= 7:
        print(nombre +', usted tiene derecho a 22 dias de vacaciones. \n ')
    else: 
        print('Sin derecho a vacaciones.')
    print('Fin del programa')
elif clave == 3:
    if años_antiguedad == 1:
        print(nombre + ', usted tiene derecho a 1o dias de vacaciones. \n')
    elif años_antiguedad >= 2 and años_antiguedad <= 6:
        print(nombre + ', usted tiene derecho a 20 dias de vacaciones. \n')
    elif años_antiguedad >= 7:
        print(nombre + ', usted tiene derecho a 30 dias de vacaciones. \n')
    else:
        print('Sin derecho a vacaciones')
    print('Fin del programa')
else:
    print('\n La clave no existe')