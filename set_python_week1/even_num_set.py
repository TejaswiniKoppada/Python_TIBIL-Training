# Python program to Print Even Numbers in Set

num=set(map(int,input("Enter the numbers :").split()))
print("Numbers in set are:",num)
even_num=[]
for i in num:
    if i%2==0:
        even_num.append(i)
print("Even Numbers in given set are:",even_num)
