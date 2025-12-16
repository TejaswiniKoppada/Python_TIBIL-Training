#Add an item to tuple
# tuples in Python are immutable, which means you cannot directly add (append) an item to an existing tuple.

my_tuple=tuple(map(str,input("Enter a tuple: ").split()))
print(my_tuple)
new_item=input("Enter a tuple: ")
print(my_tuple+(new_item,))

#(new_item,) — the comma is important; without it, Python treats it as a normal value, not a tuple.

"""
my_tuple = (10, 20, 30)
new_items = (40, 50)

my_tuple = my_tuple + new_items
print("Updated Tuple:", my_tuple)
"""