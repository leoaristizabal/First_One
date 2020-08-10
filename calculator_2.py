num1 = float(input("Enter first numer: "))
operation = input("Enter operator: ")
num2 = float(input("Enter second numer: "))

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 *num2)
elif operation == "/":
    print(num1/num2)
else:
    print("Invalid Operator")
