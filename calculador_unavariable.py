print('CALCULADORA CON UNA SOLA VARIABLE \n')

print('********************')
print('* Menu de Opciones *')
print('********************')

print('''\n1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division Entera
6. Exponente
7. Modulo o Resto \n''')

numero = int(input('Introduce el numero de la opcion deseada: \n'))

if numero == 1:
    print('Elesgiste la Opcion 1. Suma \n')
    numero = int(input('Introduce el primer numero: '))
    numero += int(input('Introduce el segundo numero: \n'))
    print('El resultado de la suma es:', numero)

elif numero == 2:
    print('Elegiste la Opcion 2. Resta \n')
    numero = int(input('Introduce el primer valor: '))
    numero -= int(input('Introduce el segundo valor: \n'))
    print('El resultado de la resta es: ', numero)
elif numero == 3:
    print('Elegiste la Opcion 3. Multiplicacion \n')
    numero = int(input('Introduce el primer valor: '))
    numero *= int(input('Introduce el segundo valora multiplicar: \n'))
    print('El resultado de la multiplicacion es: ', numero)
elif numero == 4:
    print('Elegiste la Opcion 4. Division \n')
    numero = int(input('Introduce el primer valor: '))
    numero /= int(input('Introduce el valor por el cual quieres dividir: \n'))
    print('El resultado de la division es: ', numero)
elif numero == 5:
    print('Elegiste la Opcion 5. Division Entera \n')
    numero = int(input('Introduce el primer valor: '))
    numero //= int(input('Introduce el valor por el cual quieres dividir: \n'))
    print('El resultado de la resta es: ', numero)
elif numero == 6:
    print('Elegiste la Opcion 6. Exponente \n')
    numero = int(input('Introduce el primer valor: '))
    numero **= int(input('Introduce el valor del exponente: \n'))
    print('El resultado de la potencia es: ', numero)
elif numero == 7:
    print('Elegiste la Opcion 7. Modulo o Resto \n')
    numero = int(input('Introduce el primer valor: '))
    numero %= int(input('Introduce el segundo valor: \n'))
    print('El resultado del modulo o resto es: ', numero)
else:
    print('Opcion No Valida')




















    
                   
