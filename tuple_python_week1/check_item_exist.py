# Check Item exists in Tuple
my_tuple=tuple(map(int,input("Enter a tuple: ").split()))
item=input("Enter a item to check: ")
if item in my_tuple: # if my_tuple.count(item)>0:
    print("Item is present")
else:
    print("Item is not present")