class RectangleGeometry:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def getarea(self):
        return self.length * self.breadth
    def getperimeter(self):
        return 2*(self.length+self.breadth)


rect=RectangleGeometry(12,13)
a=rect.getarea()
print("The area is {}".format(a))
p=rect.getperimeter()
print("The perimeter is {}".format(p))


