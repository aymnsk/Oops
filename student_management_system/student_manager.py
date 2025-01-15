from student import Student

class StudentManager:
    def __init__(self):
        self.students = []
    def add_student(self,student):
        self.students.append(student)
    def display_all_students(self):
        if not self.students:
            print("No student found")
            return
        for student in self.students:
            student.display_student()
            print(f"Average Marks: {student.calculate_average()}")
            print("-"*20)