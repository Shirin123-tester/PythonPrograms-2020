"Program to print even numbers from a list "
list=[]
evenlist=[]
n=int(input("Please enter no of elemnts in list "))
def calc_evennumbersfromlist():
    for i in range(0,n):
        lstelement=int(input("Enter list elemnts "))
        list.append(lstelement)
    print("List = ",list)
    for x in list:
        if x%2==0:
            evenlist.append(x)
    return evenlist

print("List of even numbers = ",calc_evennumbersfromlist())