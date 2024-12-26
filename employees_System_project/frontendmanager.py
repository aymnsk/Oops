from employeemanager import *

class frontendmanager:
    def __init__(self):
        self.employeemanager = employeemanager()

    def print_menu(self):
        print("\nprogram options: ")
        messages = [
            '1) add new employee',
            '2) list all employees',
            '3) Delete by age range',
            '4) Update salary given a name',
            '5) End the program'
        ]
        print('\n'.join(messages))
        msg =f'Enter your choice ( from 1 to {len(messages)})'
        return input_is_valid(msg,1 ,len(messages))
    
    def run(self):
        while(True):
            choice = self.print_menu()

            if choice == 1:
                self.employeemanager.add_employee()
            elif choice == 2:
                self.employeemanager.list_employee()
            elif choice == 3:
                age_from = int(input("Enter Age from: \n"))
                age_to = int(input("Enter Age to:"))
                self.employeemanager.delete_employee_with_age(age_from,age_to)
            elif choice == 4:
                name = input("Enter employee name: \n")
                salary = input("Enter employee salary \n")
                self.employeemanager.update_salary_by_name(name,salary)
            else:
                break              