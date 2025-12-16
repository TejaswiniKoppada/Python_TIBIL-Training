# Python program to Count words in a String using Dictionary
# Take input string from user
text = input("Enter a sentence: ")

# Split the string into words
words = text.split()

# Create an empty dictionary
word_count = {}

# Count each word
for word in words:
    if word in word_count:
        word_count[word] += 1   # If word already exists, increase count
    else:
        word_count[word] = 1    # If word is new, set count to 1

# Display the result
print("Word count:", word_count)
