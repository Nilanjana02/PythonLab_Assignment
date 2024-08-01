# Write a Python program to find LCM of two Numbers
num = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num > num2:
    greater = num
else:
    greater = num2
while True:
    if((greater % num == 0) and (greater % num2 == 0)):
        lcm = greater
        break
    greater += 1
print(f"The LCM of {num} and {num2} is {lcm}")