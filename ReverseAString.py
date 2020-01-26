"Program to reverse a string "
name=input("Please enter any string ")
def calc_reverseastring(str):
    x=len(str)
    reverse=""
    while x>0:
        for i in str:
            reverse=reverse+i
        x-=1
        

    return reverse
    
print("Reverse string = ",calc_reverseastring(name))

