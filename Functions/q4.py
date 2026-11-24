
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None              
    return a / b


a = float(input("First number: "))
op = input("Operator : ")
b = float(input("Second number: "))

if op == "+":
    result = add(a, b)
elif op == "-":
    result = subtract(a, b)
elif op == "*":
    result = multiply(a, b)
elif op == "/":
    result = divide(a, b)
    if result is None:
        print("Error: cannot divide by zero")
else:
    result = None
    print("Invalid operator")

if result is not None:
    print(f"Result: {result}")