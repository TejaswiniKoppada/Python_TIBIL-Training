# Python program to find Sum of Even and Odd Numbers in Set

num=set(map(int,input("Enter a numbers").split()))
print("Given Set:",num)
even_sum=0
odd_sum=0
for i in num:
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print("Sum of even numbers:",even_sum)
print("Sum of odd numbers:",odd_sum)
