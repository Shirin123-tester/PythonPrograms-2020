"Program to print list where values are square of numbers between 1 to 30 "
list=[]
squarelist=[]
def calc_squareofnumbersinlist():
    for i in range(1,31):
        element=int(input("Enter elemnt between 1 to 30 "))
        list.append(element)

    print("List = ",list)
    for x in list:
        sqr=x*x
        squarelist.append(sqr)
    
    return squarelist

print("List of square of numbers = ",calc_squareofnumbersinlist())

