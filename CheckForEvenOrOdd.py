"Program to check if given number is even or odd "

def check_number(no):
    if no%2==0:
        print(no,"is even number ")
    elif no%2>0:
        print(no,"is odd number ")
number=int(input("Please enter any number "))

check_number(number)