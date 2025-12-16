# # Python Program to Read 10 Numbers and Find their Sum and Average
#
# try:
#   numbers=list(map(int,input("Enter 10 numbers").split()))
#   if len(numbers)!=10:
#     raise ValueError("Error")
#   else:
#     print("total=",sum(numbers))
#     print("average=",sum(numbers)/len(numbers))
# except ValueError as e:
#   print(e)

inputs=[]
print("Enter 10 values")
for i in range(10):
    value=int(input("Input "+ str(i+1)+":"))
    inputs.append(value)
print("Entered numbers",inputs)
print("Sum=",sum(inputs))
print("Average=",sum(inputs)/len(inputs))