# Python program to Check if a Given key exists in a Dictionary

# Create a dictionary
student = {"name": "Alice", "age": 20, "course": "BCA"}

# Take key input from user
key = input("Enter key to check: ")

# Check if key exists
if key in student:
    print("Yes", key, "exists in the dictionary.")
else:
    print("No", key ,"does not exist in the dictionary.")
