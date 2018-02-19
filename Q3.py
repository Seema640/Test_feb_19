class Employee:
    def __init__(self,first_name,last_name,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary

    def gen_email(self):
        self.email=self.first_name + '.' + self.last_name + '@deerwalk.edu.np'

    def display(self):
         print("First name={}".format(self.first_name))
         print("Last name={}".format(self.last_name))
         print("Salary={}".format(self.salary))
         print("Email={}".format(self.email))

emp=Employee("Seema","Tamang",100000)
emp.gen_email()
emp.display()



