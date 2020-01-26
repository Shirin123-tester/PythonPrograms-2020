"Program to check if no is in given range or not "
lrange=int(input("Please enter a lower range "))
urange=int(input("Please enter a upper range "))
number=int(input("Please enter a number to check "))
def calc_range(a):
    if a>=lrange and a<=urange:
        print(a,"is in range")
    else:
        print(a,"not in range")

calc_range(number)

