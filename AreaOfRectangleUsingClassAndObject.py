"Program to calculate area of rectangle using class and object"

class Rectangle:

    def __init__(self,l,b):
        super().__init__()
        self.l=l
        self.b=b

    def calc_area(self):
        rec_area=self.l*self.b
        return rec_area
    
    def print_data(self):
        print("Length of rectangle = ",self.l)
        print("Width of rectangle = ",self.b)


length=int(input("Please enter length of rectangle "))
width=int(input("Please enter width of rectangle "))
r=Rectangle(length,width)
r.print_data()
print("Area of rectangle = ",r.calc_area())

