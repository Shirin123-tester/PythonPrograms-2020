"Program to check if given staring is palindrome or not "
name=input("Please enter any staring ")
def chk_palindrome(str):
    x=len(name)
    reverse=""
    while x>0:
        reverse+=str[x-1]
        x-=1
    print("Given String = ",str)
    print("Reverse String = ",reverse)

    if reverse==str:
        print("Given string is Palindrome ")
    else:
        print("Given string is not Palindrome ")

chk_palindrome(name)

