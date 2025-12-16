# Python program to Count Even and Odd Numbers in Set
num=set(map(int,input("Enter the numbers:").split()))
even=0
odd=0
for i in num:
    if i %2==0:
        even+=1
    else:
        odd+=1
print("Set:", num)
print("Number of even numbers:",even)
print("Number of odd numbers:",odd)
