number=int(input('Enter a no from 1500 to 2700 '))
div1=number%7
div2=number%5
if div1==0 and div2==0:
    print(number,"is divisible by 7 and multiple of 5")
else:
    print(number,"is not divisible by 7 and multiple of 5")