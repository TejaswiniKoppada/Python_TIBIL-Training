# Armstrong number (narcissistic number)
# 153  1³ + 5³ + 3³ = 1 + 125 + 27 = 153
# a number that is equal to the sum of its own digits,each raised to the power of the number of digits.

try:
  num=int(input("Enter a number"))
  temp=num
  length=len(str(num))
  sum_of_digits=0
  while num>0:
    digit=num%10
    sum_of_digits +=digit ** length
    num//=10
  if temp==sum_of_digits:
    print("It is an armstrong number")
  else:
    print("It is not an armstrong number")
except ValueError as e:
  print(e)

