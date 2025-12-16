# # Python program to multiply all items in a Dictionary

import math

numbers = {'a': 2, 'b': 3, 'c': 4}
result = math.prod(numbers.values())

print("Product of all items:", result)


# # Create a dictionary
# numbers = {'a': 2, 'b': 3, 'c': 4}
#
# # Initialize product variable
# result = 1
#
# # Multiply all values
# for value in numbers.values():
#     result *= value
#
# # Display the result
# print("Dictionary:", numbers)
# print("Product of all items:", result)
#
#
# # Example input: {'x': 2, 'y': 5, 'z': 3}
#
# data = eval(input("Enter a dictionary of numbers: "))
# product = 1
#
# for value in data.values():
#     product *= value
#
# print("Product of all items:", product)
