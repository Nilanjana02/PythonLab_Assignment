def Palindrome(n):
    k = n
    s = 0
    while k!=0:
        r = k%10
        s = s*10 +r
        k = k//10
    if s==n:
        print(n," is a palindrome")
    else:
        print(n, " is not a palindrome")       
           
n = int(input("Enter a number to check palindrom or not: "))
Palindrome(n) 

