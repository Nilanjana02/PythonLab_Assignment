 # Write a Python program to calculate the sum of natural numbers up to a certain range.
num = int(input("Enter the range: "))
sum = 0
for i in range(num+1):
    sum += i
print(f"The sum of natural numbers up to {num} is {sum}")