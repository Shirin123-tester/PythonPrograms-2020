"Program to multiply all the numbers in list "
list =[]
rng =int(input("Please enter no of elemnts in list "))
def calc_multiplication():
    for i in range(0,rng):
        element1=int(input("Enter elements of list "))
        list.append(element1)
    print("list = ",list)

    mul=1
    for x in range(0,rng):
        mul=mul*list[x]
    return mul
print("Multiplication of all no.s of list = ",calc_multiplication())

