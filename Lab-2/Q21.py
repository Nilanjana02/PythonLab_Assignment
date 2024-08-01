# Write a Python program to find HCF of two Numbers. HCF is the highest common factor of two numbers.

num = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num > num2:
    smaller = num2 
else:
    smaller = num
for i in range(1, smaller+1):
    if((num % i == 0) and (num2 % i == 0)):
        hcf = i
print(f"The HCF of {num} and {num2} is {hcf}")