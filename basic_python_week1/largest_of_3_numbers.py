#Python Program to find the largest of 3 numbers
try:
    elements=list(map(int, input("Enter only 3 numbers").split()))
    if len(elements)!=3:
      raise ValueError("Error:Enter 3 elements")
    else:
        elements.sort(reverse=True)
        print(elements[0])
except ValueError as e:
  print(e)

  """
  #Python Program to find the largest of 3 numbers
elements=list(map(int, input("Enter only 3 numbers").split()))
if len(elements)==3:
    print(max(elements))
else:
  print("Error:Enter 3 elements")"""