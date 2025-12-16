# Python program to Print Odd Numbers in Set

num=set(map(int,input("Enter the numbers :").split()))
print("Numbers in set are:",num)
odd_num=[]
for i in num:
    if i%2!=0:
        odd_num.append(i)
print("Odd Numbers in given set are:",odd_num)
print(type(odd_num))
