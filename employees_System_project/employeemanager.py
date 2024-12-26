from utility import *
from employee import *

class employeemanager:
    def __init__(self):
        self.employee = []
    
    def add_employee(self):
        print('enter employee data')
        name = input("Enter employee name:")
        age = input_is_valid("Enter employee age:")
        salary = input_is_valid("Enter employee salary:")
        self.employee.append(employee(name,age,salary))

    def list_employee(self):
        if len(self.employee) == 0:
            print("\nEmployee list is empty!!")
            return
        else:
            for emp in self.employee:
                print(emp)

    def delete_employee_with_age(self,age_from,age_to):
        for emp in self.employee:
            if age_from <= emp.age <= age_to:
                print(f"\tDeleting employee {emp.name}")
                self.employee.remove(emp)

    def find_employee(self, name):
        for emp in employee:
         if emp.name == name:
            return emp  
        return None

    def update_salary_by_name(self,name,age,salary):
        emp = self.find_employee(name)
        if emp is None:
            print('Error: No employee found')
        else:
            emp.salary = salary      

