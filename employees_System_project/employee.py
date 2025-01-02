
class employee:
    def __init__(self ,Name ,age ,salary):
        self.Name = Name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'employee {self.Name} has age {self.age} and salary {self.salary}'
    
    def __repr__(self):
        return F'employee(name={self.Name},age={self.age},salary={self.salary})'