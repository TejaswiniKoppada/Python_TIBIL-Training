#Remove Duplicates from a list
original_list=list(map(str,input("Enter the items:").split()))
required_list=set(original_list)
print("list with no duplicates:",required_list)

"""
my_list = [1, 2, 3, 2, 4, 1, 5, 3]

unique_list = []

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print("Original List:", my_list)
print("List after removing duplicates:", unique_list)
"""