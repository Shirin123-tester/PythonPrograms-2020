"Program to find maximum of three numbers"
def calc_maxnumber(no1,no2,no3):
    if no1>no2 and no1>no3:
        return no1
    elif no2>no1 and no2>no3:
        return no2
    else:
        return no3

number1=int(input("Please enter first number "))

number2=int(input("Please enter second number"))

number3=int(input("Please enter third number"))

print("maximum of theree no = ",calc_maxnumber(number1,number2,number3))