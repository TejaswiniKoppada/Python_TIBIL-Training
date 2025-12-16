# Python Program to Convert List(ordered, allows duplicates) to set(unordered, no duplicates)


my_list=list(input("Enter the list: ").split())
set_list=set(my_list)
print("Original list:",my_list)
print("Converted List:",set_list)
print("Type of the converted list:",type(set_list))