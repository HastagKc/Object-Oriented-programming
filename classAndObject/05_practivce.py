# Design a class representing employees with attributes like name, salary, 
#  and department. Include methods for calculating bonuses, deductions, and displaying employee information.

class Employees:
    def __init__(self, name, salary, department):
        self.name=name
        self.salary=salary
        self.department=department

    def emp_bonus(self,bonuses ):
        self.bonuses=bonuses
        bonus_amout= self.salary*self.bonuses/100
        total_salary= bonus_amout + self.salary
     
        print(f"bonuses {bonus_amout} total salary with bonuses is {total_salary}")

    def deductions(self, working_day):
        self.working_day= working_day
        if (working_day <=30) and (working_day>=20):
            print(f"{self.salary*15/100}")
        elif (working_day <=20) and (working_day>=10):
            print(f"{self.salary*15/100}")
        else:
            print("your fired")
    
    def emp_info(self):
        print(f"Employ Info name{self.name} salary:{self.salary} and department{self.department}")
    
  
emp_name=input("Enter your Name: ")
emp_salary=int(input("Enter your  Salary: "))
emp_department=input("Enter your department: ")



emp1=Employees(emp_name,emp_salary, emp_department)
emp1.emp_bonus(10)
emp1.deductions(23)
emp1.emp_info()

