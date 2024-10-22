#Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
op = input("Enter operation: + - / * %:")

if op == '+':
    c = a + b;
elif op == '-':
    c = a - b;
elif op == '/':
    c = a / b;
elif op == '*':
    c = a * b;

else:
    print("Invalid operation!")

print(f"The result of {a} {op} {b} is: {c}")