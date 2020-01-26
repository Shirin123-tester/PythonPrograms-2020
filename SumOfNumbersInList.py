"Program to sum all the numbers in list"
list1=[]

n=int(input("Please enter no of elemnts in list :"))

def calc_sumoflistnumbers():
    for i in range(0,n):
        element=int(input("Enter elements of list "))
        list1.append(element)
    print("List1 = ",list1)
    sum=0
    for x in range(0,len(list1)):
        sum=sum+list1[x]
    return sum


print ("sum of elemnts = ",calc_sumoflistnumbers())

