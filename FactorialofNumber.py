"Program to clculate factorial of a number"
def clac_factorial(no):
        fact=1
        while(no>1):
            fact*=no
            no-=1
            
        return fact

    
number=int(input("Enter number to clculate factorial"))

fact1= clac_factorial(number)

print("Factorial of a number = ",fact1)



