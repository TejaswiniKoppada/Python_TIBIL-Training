# Python program to Print Positive Numbers in Set


num=set(map(int,input("Enter the numbers :").split()))
print("Numbers in set are:",num)
pos_num=[]
for i in num:
    if i>1 and i!=0:
        pos_num.append(i)
print("Positive Numbers in given set are:",pos_num)

