# Count occurence of the character

# text.count(ch)
# text.lower().count(ch.lower())

text=input("Enter a string")
ch=input("Enter a character to count the occurence")

if len(ch)!=1 or not ch.isalpha():
    print("Enter a single alphabet character to count the occurence")
else:
    count=0
    for c in text:
        if c == ch:
            count+=1
    print("The occurence of",ch,"is",count)

    # text = input("Enter a string").lower()
    # ch = input("Enter a character to count the occurence").lower()
    #
    # if len(ch) != 1 or not ch.isalpha():
    #     print("Enter a single alphabet character to count the occurence")
    # else:
    #     count = 0
    #     for c in text:
    #         if c == ch:
    #             count += 1
    #     print("The occurence of", ch, "is", count)