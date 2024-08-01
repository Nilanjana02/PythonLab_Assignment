# Write a Python program that prompts the user to enter a base number and an exponent,and then calculates the power of the base to the exponent. The program should not use the exponentiation operator (**) or the math.pow() function.

num1 = int(input("Enter the base number: "))
num2 = int(input("Enter the exponent: "))
result = 1
for i in range(num2):
    result *= num1
print(f"The power of {num1} to the {num2} is {result}")


