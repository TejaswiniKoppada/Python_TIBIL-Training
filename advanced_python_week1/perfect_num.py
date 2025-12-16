# Perfect number
# A number is perfect if when you add up all the numbers that divide it (except itself),the sum equals the original number.

try:
  num=int(input("Enter a number"))
  if num<=0:
    raise ValueError("Enter a positive number")
  sum_of_divisors=0
  # Find divisors
  for i in range(1,num):
      if num%i==0:
          sum_of_divisors+=i
  # Check if perfect
  if sum_of_divisors==num:
      print("It's a perfect number")
  else:
      print("Not a perfect number")

except ValueError as e:
  print(e)