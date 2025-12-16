#Count number of digits in number
try:
  num=int(input("Enter a number"))
  num=abs(num)
  count=len(str(num))
  print("Digits in num :",count)
except ValueError as e:
  print(e)

  """
  # Count number of digits in number
try:
  num=int(input("Enter a number:"))
  num=abs(num)
  if num==0:
    count=1
  else:
    count=0
    while num!=0:
      num //=10
      count+=1
    print("Digits=",count)
except ValueError as e:
  print(e)
  """