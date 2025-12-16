# Python Program for ASCII value of the single character
# ord() function in Python returns the ASCII (or Unicode) value of a given character.

ch=input("Enter a character:")
if len(ch)!=1 or not ch.isalpha():
    print("Enter a single alphabet character")
else:
    print("ASCII value of the given single character is", ord(ch))  #  ascii_value = ch.encode()[0]


# to find the character from an ASCII value, use chr()

# num = int(input("Enter an ASCII value: "))
# print("The character for ASCII value", num, "is", chr(num))
