# # Find the total average-and-percentage-of-five-subjects
#
# try:
#   marks=list(map(float,input("Enter 5 subjects marks").split()))
#   if len(marks)!=5:
#     raise ValueError("Error:Enter 5 subjects marks")
#   total=sum(marks)
#   total_avg=total/5
#   per=(total/500)*100
#   print("total=",total)
#   print("average=",total_avg)
#   print("percentage=",per)
# except ValueError as e:
#   print(e)

marks=[]
print("Enter 5 subject marks:")
for i in range(5):
    subject=int(input("marks of subject "+ str(i+1) + ":"))
    marks.append(subject)
print("5 Subject marks=",marks)
print("Total =",sum(marks))
print("Average=",sum(marks)/len(marks))
print("Percentage=",(sum(marks))/500*100)