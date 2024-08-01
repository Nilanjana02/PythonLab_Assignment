# Write a Python program to convert a Binary Number to Decimal.write with logic , don't use any build in function.
num = int(input("Enter a binary number: "))
binary = num
decimal = 0
i = 0
while binary != 0:
    rem = binary % 10
    decimal += rem * pow(2, i)
    binary = binary // 10
    i += 1
print(f"The decimal equivalent of {num} is {decimal}")