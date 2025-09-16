'''
8. Employee Management System (Dictionaries + Inheritance)
Task: Manage employees with inheritance.
Input:
employees = {"Alice": {"role": "Manager", "base_salary": 5000}, "Bob": {"role": "Developer",
"base_salary": 4000}}
Expected Output:
Alice Salary: 7000
Bob Salary: 4800
'''

'''
8. Employee Management System (Dictionaries + Inheritance)
Task: Manage employees with inheritance.
Input:
employees = {"Alice": {"role": "Manager", "base_salary": 5000}, "Bob": {"role": "Developer",
"base_salary": 4000}}
Expected Output:
Alice Salary: 7000
Bob Salary: 4800
'''
class Employee:
    def __init__(self,name):
        self.name=name
        
    def add_role_and_base_salary(self,role,base_salary):
        self.role=role
        self.base_salary=base_salary
        
    def calc_salary(self):
        if self.role == 'Manager':
            self.salary = self.base_salary + 2000
        elif self.role == 'Developer':
            self.salary = self.base_salary + 800
        print(f"{self.name} : {self.salary}")
    
employees = {
    "Alice": {
        "role": "Manager", 
        "base_salary": 5000
    }, 
    "Bob": {
        "role": "Developer",
        "base_salary": 4000
    }
}

for name,role_desc in employees.items():
    e=Employee(name)
    e.add_role_and_base_salary(role_desc["role"],role_desc["base_salary"])
    e.calc_salary()

'''

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Manager(Employee):
    def calculate_salary(self):
        return self.base_salary + 2000


class Developer(Employee):
    def calculate_salary(self):
        return self.base_salary + 800

employees = {
    "Alice": {"role": "Manager", "base_salary": 5000},
    "Bob": {"role": "Developer", "base_salary": 4000}
}

for name, details in employees.items():
    role = details["role"]
    base_salary = details["base_salary"]

    if role == "Manager":
        emp = Manager(name, base_salary)
    elif role == "Developer":
        emp = Developer(name, base_salary)
    else:
        emp = Employee(name, base_salary)  

    final_salary = emp.calculate_salary()
    print(f"{name} Salary: {final_salary}")

'''