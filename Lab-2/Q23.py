# Write a Python program to count the number of digits of an integer
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num = num // 10
print(f"The number of digits in the integer is {count}")