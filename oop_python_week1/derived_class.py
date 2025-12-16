# 3. Create derived class Manager extending Employee

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


class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


# Take input from user
name = input("Enter manager name: ")
emp_id = int(input("Enter employee ID: "))
salary = float(input("Enter salary: "))
dept = input("Enter department: ")

# Create object and show info
mgr = Manager(name, emp_id, salary, dept)
mgr.display()
