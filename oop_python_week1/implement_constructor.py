# 2. Implement constructor to initialize data

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)

# Take input from user
name = input("Enter employee name: ")
emp_id = int(input("Enter employee ID: "))
salary = float(input("Enter employee salary: "))

# Object creation calls constructor automatically
emp = Employee(name, emp_id, salary)
emp.display()
