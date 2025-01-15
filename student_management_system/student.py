class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display_student(self):
        print(f"Name{self.name}")
        print(f"Age{self.age}")
        print(f"Marks{self.marks}")
    def calculate_average(self):
        return sum(self.marks)/len(self.marks)