# Python program to Map two lists into a Dictionary

keys = ["name", "age", "course"]
values = ["Alice", 20, "BCA"]

student = {}

# student = dict(zip(keys, values))

for i in range(len(keys)):
    student[keys[i]] = values[i]

print("Dictionary:", student)


