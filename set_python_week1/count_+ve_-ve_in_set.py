# Python program to Count Positive and Negative Numbers in Set

num=set(map(int,input("Enter numbers: ").split()))
print("Set=",num)
positive_count=0
negative_count=0
for i in num:
    if i>0:
        positive_count+=1
    elif i<0:
        negative_count+=1
    else:
        print("Zero is a neutral number")

print("Positive count=",positive_count)
print("Negative count=",negative_count)