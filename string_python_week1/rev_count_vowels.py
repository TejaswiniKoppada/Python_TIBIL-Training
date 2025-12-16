# Program to reverse a string and count vowels

text = input("Enter a string: ")

lower_text = text.lower()

# Reverse the string
reversed_text = text[::-1]


vowels = "aeiou"

# Count vowels
vowel_count = 0
for ch in lower_text:
    if ch in vowels:
        vowel_count += 1

print("Original string:", text)
print("Reversed string:", reversed_text)
print("Number of vowels:", vowel_count)
