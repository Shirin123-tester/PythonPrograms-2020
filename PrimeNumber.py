number=int(input('Please Enter a number to check for prime '))
if number>1:
    result=0
    i=2
    while i<=number/2:
        if number%i==0:
            result=1
            break
        i+=1              
if result==1:
    print(number,"is not prime")
else:
     print(number,"is prime")
