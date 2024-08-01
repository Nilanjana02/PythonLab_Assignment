# Write a Python program to display prime numbers between a given interval.
firstNum = int(input("Enter the first number: "))
secondNum = int(input("Enter the second number: "))
for num in range(firstNum, secondNum + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)