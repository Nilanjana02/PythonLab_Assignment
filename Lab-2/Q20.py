#  Write a Python program to print all multiple of 10 between a given interval.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
for i in range(num1, num2+1):
    if i % 10 == 0:
        print(i)