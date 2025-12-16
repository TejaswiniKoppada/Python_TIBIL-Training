# 1. Write a function to find factorial
#
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)

num=int(input("Enter a number: "))
print(factorial(num))


# import math
#
# num = int(input("Enter a number: "))
# print("The factorial of", num, "is", math.factorial(num))
