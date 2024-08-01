import math

def find_gcd():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    gcd = math.gcd(num1, num2)
    return gcd

result = find_gcd()
print(f"The GCD of the two numbers is: {result}")
