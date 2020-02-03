"Program to print sum of two numbers using class and object "

class Sum():
    def __init__(self,no1,no2):
        super().__init__()

        self.no1=no1
        self.no2=no2

    def calculate_sum(self,no1,no2):
        self.sum=0
        self.sum=no1+no2

    def print_data(self,no1,no2):
        print("number1 = ",self.no1)
        print("number2 =",self.no2)
        print("Sum = ",self.sum)



number1=int(input("Please enter first number ")) 
number2=int(input("Please enter second number"))

s=Sum(number1,number2)
s.calculate_sum(number1,number2)
s.print_data(number1,number2)

