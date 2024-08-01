# 11. Write a program in Python to find the sum of digits of a number. Example 1234=>1+2+3+4=10
num = int(input("Enter the number: "))
# funtion for sum of digits
def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return num%10 + sum_of_digits(num//10)

print(f"The sum of digits of {num} is {sum_of_digits(num)}")