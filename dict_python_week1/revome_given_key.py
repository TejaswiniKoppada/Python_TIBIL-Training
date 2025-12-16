# Python program to Remove Given Key from a Dictionary

# Create a dictionary
student = {"name": "Alice", "age": 20, "course": "BCA", "grade": "A"}

# Display original dictionary
print("Original Dictionary:", student)

# Take key to remove
key = input("Enter the key to remove: ")

# Check and remove key
if key in student:
    student.pop(key)
    print(f"'{key}' has been removed.")
else:
    print(f"'{key}' not found in dictionary.")

# Display updated dictionary
print("Updated Dictionary:", student)
