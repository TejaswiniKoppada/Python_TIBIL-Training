# Python example to add Key-Value Pair to a Dictionary


data = {}
pairs = input("Enter key:value pairs separated by spaces: ").split()

for pair in pairs:
    key, value = pair.split(":")
    data[key] = value

print("Dictionary:", data)
