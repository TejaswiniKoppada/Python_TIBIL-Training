# Remove an Item from a Tuple

my_tuple=tuple(map(str,input("Enter a tuple: ").split()))
print("Original Tuple:", my_tuple)
item=input("Enter a item to remove: ")
temp_list=list(my_tuple)
if item in temp_list:
    temp_list.remove(item)
    my_tuple=tuple(temp_list)
    print("Updated Tuple:", my_tuple)
else:
    print("Item not found in tuple:", item)