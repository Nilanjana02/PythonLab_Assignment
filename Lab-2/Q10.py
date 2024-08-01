# Write a program in Python to check if a number is Krishnamurthy number.
import math

def is_krishnamurthy_number(n):
    digits = str(n)
    sum_of_factorials = sum(math.factorial(int(digit)) for digit in digits)
    return sum_of_factorials == n

number = int(input("Enter a number: "))
if is_krishnamurthy_number(number):
    print(f"{number} is a Krishnamurthy number.")
else:
    print(f"{number} is not a Krishnamurthy number.")
