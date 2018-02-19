class Student:
    def __init__(self,name,section):
        self.name=name
        self.section=section

    @classmethod
    def get_from_string(cls, inp):
            name, sec = inp.split("-")
            return cls(name, sec)


student1 = Student.get_from_string("Seema-A")
print(student1)
print(student1.__dict__)



