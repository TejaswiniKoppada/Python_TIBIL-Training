# 4. Function returning multiple values

def calculate(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div  # returning 4 values

# Taking input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Getting multiple return values
addition, subtraction, multiplication, division = calculate(x, y)

# Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
