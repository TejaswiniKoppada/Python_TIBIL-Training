# Python program to check Vowel or Consonant

ch=input("Enter a character: ")

if len(ch)!=1 or not ch.isalpha():
    print("Please enter a single alphabet character")
else:
    if ch.lower()==('a','e','i','o','u'):
        print("Character is a vowel")
    else:
        print("Character is a consonant")