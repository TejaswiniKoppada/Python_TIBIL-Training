# Palindrome number
# a number that reads the same backward as forward.
"""num=input("Enter a number: ")
if num==num[::-1]: #sequence[start:end:step] it reverses the sequence.
  print(num,"is a palindrome")
else:
    print("Not a palindrome")"""

try:
    num = int(input("Enter a number: "))
    temp = num  # store original number
    rev = 0     # variable to store reversed number

    # reverse the number
    while temp > 0:
        digit = temp % 10          # get last digit
        rev = (rev * 10) + digit   # add it to reverse
        temp //= 10                # remove last digit

    if num==rev:
        print(num,"is a palindrome")
    else:
        print(num,"is not a palindrome")

except ValueError:
    print("Error: Please enter a valid integer.")


