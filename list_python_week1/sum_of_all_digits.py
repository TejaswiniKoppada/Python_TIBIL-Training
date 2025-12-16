# Sum of all the digits
digit=int(input("Enter a number: "))
total=0
temp=digit
while temp>0:
    last_digit=temp%10
    total+=last_digit
    temp=temp//10
print(total)
