# Write a program to compute the value of Euler’s number that is used as the base of natural logarithms. Use the following formula. e= 1+ 1/1! +1 /2! + 1/3+................ 1/n!
import math
def euler(n):
    e = 0
    for i in range(n+1):
        e += 1/math.factorial(i)
    return e

n = int(input('Enter the value of n: '))
print(euler(n))