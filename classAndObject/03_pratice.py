# 3. Student Information System:
#  Implement a class to store student information with attributes such as name, roll number, and marks. Include methods for calculating grades and displaying student details.

class Student:
    def __init__(self, stu_name, stu_roll_no, stu_marks):
        self.stu_name = stu_name
        self.stu_roll_no = stu_roll_no
        self.stu_marks = stu_marks

    def grade(self):
        if self.stu_marks >= 90 and self.stu_marks < 100:
            return 'A+'
        elif self.stu_marks >= 80 and self.stu_marks < 90:
            return 'A'
        elif self.stu_marks >= 70 and self.stu_marks < 80:
            return 'B+'
        elif self.stu_marks >= 60 and self.stu_marks < 70:
            return 'B'
        elif self.stu_marks >= 50 and self.stu_marks < 60:
            return 'C'
        elif self.stu_marks >= 40 and self.stu_marks < 50:
            return 'D+'
        elif self.stu_marks < 40:
            return 'Fail'
        else: 
            return 'Invalid marks please enter valid marks'
        
    def display_student_details(self):
        print(f"Student name: {self.stu_name}")
        print(f"Student roll Number: {self.stu_roll_no}")
        print(f"Student grade: {self.grade()}")

# crating object 
name = input("Enter your name: ")
roll_no = input("Enter your roll number: ")
marks = int(input("Enter your marks: "))

stu1 = Student(stu_name=name, stu_roll_no=roll_no, stu_marks=marks)
stu1.display_student_details()