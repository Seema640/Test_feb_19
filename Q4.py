class Temperature:
    def __init__(self,celsius,fahrenheit):
        self.celsius=celsius
        self.fahrenheit=fahrenheit
    def convertfahrenheit(self):
        return self.celsius*1.8+32
    def convertcelsius(self):
        return (self.fahrenheit-32)*0.556

temp=Temperature(0,40)
t1=temp.convertfahrenheit()
print("The conversion to fahrenheit is {}".format(t1))
t2=temp.convertcelsius()
print("The conversion to celsius is {}".format(t2))

