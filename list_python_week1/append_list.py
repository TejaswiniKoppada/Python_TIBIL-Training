#Append an item to list

my_list=[]
n=int(input("How many items do you want to add? "))
for i in range(n):
    item=input("Enter item " + str(i+1)+" to add to list: ")
    my_list.append(item)
print("Final List:", my_list)


"""numbers = [1, 2, 3]
numbers.extend([4, 5])
print(numbers)"""

"""numbers = [1, 2, 3]
numbers.append(4)"""