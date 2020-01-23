'Program to print largest number from list'
number=[10,20,30,40,50]
greater=number[0]
for item in number :
    if number[item]>greater :
        greater=number[item]

print(greater)