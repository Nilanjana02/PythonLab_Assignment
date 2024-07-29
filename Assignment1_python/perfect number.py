import math
def perfect(num):
    dup = num
    k = int(math.sqrt(num))
    s = 1
    for i in range(2,k+1):
        if num%i == 0:
            s = s+i
            if num//i != i:
                p = num//i
                s = s+p
    print("the sum = ",s)            
    if dup == s:
        print("This is a perfect number")
    else:
        print("This is not a perfect number")                

num = int(input("Enter the number:"))
perfect(num)                
