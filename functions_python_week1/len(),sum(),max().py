# 2. Use built-in functions like len(), sum(), max()
try:
    num = list(map(int,input("Enter a number: ").split()))
    print("length of number:",len(num))
    print("sum of numbers:",sum(num))
    print("maximum of numbers:",max(num))
    print("minimum of numbers:",min(num))


except ValueError:
    print("Invalid input, only integers are allowed")