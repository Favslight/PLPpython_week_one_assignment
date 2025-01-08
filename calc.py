# Simple calculator build up

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#operator set up

operator = input("Enter a mathematical operator (+,-,*,/)")

#loop

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
    
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
    
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Division by zero is not allowed")
        
else:
    print("Invalid mathematical operator")