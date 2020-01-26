"Program to create unique list from given list"
list=[]
no=int(input("Enter number of element in a list "))

def calc_uniquelist():
    for i in range(0,no):
        elements=int(input("Enter elements of a list "))
        list.append(elements)
    
    uniquelist=[]
    print("List = ",list)
    for a in list:
        if a not in uniquelist:
           uniquelist.append(a)
    return uniquelist

print("Unique list = ",calc_uniquelist())

