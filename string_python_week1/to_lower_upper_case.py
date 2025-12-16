# Convert String to lower case ,String to uppercase
try:
    text=input("Enter a string:")
    if not text.isalpha():
        raise ValueError("Invalid input")
    print("original string is", text)
    print("Lowercase string is",text.lower())
    print("Uppercase string is",text.upper())
except ValueError as e:
    print(e)