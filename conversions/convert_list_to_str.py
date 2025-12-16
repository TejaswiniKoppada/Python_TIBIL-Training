# Python Program to Convert List To String
my_list=list(input("Enter a list: ").split())
print("Original list:",my_list)
string_list=' '.join(my_list)
print("Converted string_list:",string_list)
print("type of list :", type(string_list))

# # Example 4: Using str()
# my_list = [1, 2, 3, 'Python']
# result = str(my_list)
# print(result)  # Output: "[1, 2, 3, 'Python']"
