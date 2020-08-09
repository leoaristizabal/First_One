def cube(num1):  #definicion de la funcion
    return num1**3 #return
result = (cube(2)) #variable contenedora de la funcion bajo el parametro del valor 2

print(result) #imprime 
#if statements

is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male or tall")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall): #Es hombre pero no alto, se cumple una
    print("You are a short man")
elif not is_male and is_tall: #SI NO es hombre pero es alto
    print("You are not a male but are tall")
else:
    print("You are either not male or not tall or both")

# if statements with comparisons (numero mas grande)

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(2131,13213,1221))







