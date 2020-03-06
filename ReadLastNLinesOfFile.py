"Program to read last n lines of a file"
f=open("Student.txt","r")
data=f.readlines()
line_number=int(input("Please enter line number you want to read :"))


for x in range(0,len(data)):
    if  line_number==x:
        f.seek(x,0)
        print(f.readlines())
        
        