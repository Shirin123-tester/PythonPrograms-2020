'Program to add ing or ly at the end of given string '
string=input('enter any string')
length=len(string)
if length<3:
    print("Invalid length string")
else:
    if string.endswith('ing'):
        string=string+'ly'
    else:
        string=string+'ing'

print(string)    

