#Python program to check Character is an Alphabet, Digit or Special Character
character=input("Enter a character: ")

if len(character)!=1:
    print("Enter only single character")
else:
    if character.isalpha():
        print(character,"is a alphabet")
    elif character.isdigit():
        print(character,"is a digit")
    else:
        print(character,"is a special character")

