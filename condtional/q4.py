a = float(input("first number: "))
op = input("operator (+ - * /): ")
b = float(input("second number: "))

if op == "+":
    print(f"Result: {a + b}")
elif op == "-":
    print(f"Result: {a - b}")
elif op == "*":
    print(f"Result: {a * b}")
elif op == "/":
    if b != 0:
        print(f"Result: {a / b}")
    else:
        print("Error: cannot divide by zero")
else:
    print("Invalid operator")