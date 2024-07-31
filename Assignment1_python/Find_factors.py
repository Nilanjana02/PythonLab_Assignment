
import math
def find_factors(num):
    sq = int(math.sqrt(num))
    i=1
    for i in range (1,sq+1):
        if num%i == 0:
            print(i)
            if num // i != i:
                print(num//i)  

num = int(input("Enter a number: "))
find_factors(num) 

