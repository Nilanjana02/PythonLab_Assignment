# Write a Python program to calculate factorial of 12.
num = 12
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
print(f"The factorial of {num} is {factorial(num)}")