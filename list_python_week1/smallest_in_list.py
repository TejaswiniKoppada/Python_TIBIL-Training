#Print Smallest number in a list
my_list=list(map(int,input("Enter the required elements").split()))
my_list.sort(reverse=True)
print(my_list[-1])