# Python program to Print Negative Numbers in Set

num=set(map(int,input("Enter the numbers :").split()))
print("Numbers in set are:",num)
neg_num=[]
for i in num:
    if i<1:
        neg_num.append(i)
print("Negative Numbers in given set are:",neg_num)

