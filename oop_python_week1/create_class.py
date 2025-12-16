# 1.Create class Employee with attributes and Methods

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_details(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)

# Taking input from user
name = input("Enter employee name: ")
emp_id = int(input("Enter employee ID: "))
salary = float(input("Enter employee salary: "))

# Creating object
emp = Employee(name, emp_id, salary)
emp.display_details()
