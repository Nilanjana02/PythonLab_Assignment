def armstrong(num):
    k = num
    n = num
    C = 0
    s = 0
    while num != 0:
        r = num%10
        C =C+1
        num = num//10
    while k!= 0:
        r = k%10
        s = s+pow(r,C)
        k = k//10
    if n == s:
        print(s," is a armstrong number")
    else:
        print(s," is not a armstrong number") 
num = int (input("Enter a number: "))
armstrong(num)                
