# Convert Decimal number to Binary
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary_num = ""
    while n > 0:
        binary_num = str(n % 2) + binary_num
        n = n // 2
    return binary_num

decimal_number = int(input("Enter a decimal number: "))

binary_number = decimal_to_binary(decimal_number)

print(f"The binary representation of {decimal_number} is {binary_number}")
