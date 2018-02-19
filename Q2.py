class Circle:
    pi=22/7
    def __init__(self,radius):
        self.radius=radius

    def getarea(self):
        return self.pi *(self.radius)**2
    def getcircumference(self):
        return 2* self.pi*self.radius


cir=Circle(2)
a=cir.getarea()
print("The area is {}".format(a))
p=cir.getcircumference()
print("The perimeter is {}".format(p))

