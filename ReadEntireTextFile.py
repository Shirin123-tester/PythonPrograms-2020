"Program to read entire text file"
f=open("Student.txt","r")
text=f.readlines()
count=0
print("Entire file text : ",text)
for x in text:
    print(x)
    if x=="abcd" :
        count=1
        break

if count==1:
    print("Student name present in a file:")
else:
    print("Student name not present in a file")