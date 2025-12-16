# Python Program to Read 10 Numbers

inputs = []

print("Enter 10 values:")

for i in range(10):
    value = input("Input" + str(i+1) +":" )
    inputs.append(value)

print("You entered:", inputs)