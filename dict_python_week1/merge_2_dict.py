# Python program to Merge Two Dictionaries

# Create two dictionaries
dict1 = {"name": "Alice", "age": 20}
dict2 = {"course": "BCA", "grade": "A"}

# Merge dictionaries
dict1.update(dict2)    # merged = {**dict1, **dict2}    --> This does not modify the original dictionaries.

# Display the merged dictionary
print("Merged Dictionary:", dict1)


# update() adds all key–value pairs from one dictionary into another.
#
# If the same key exists in both, the second one overwrites the first.