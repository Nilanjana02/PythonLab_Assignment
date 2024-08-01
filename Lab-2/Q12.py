# Write a program in Python that prompts the user to input a number and prints its multiplication table.
num = int(input("Enter the number: "))
def multiplication_table(num, i):
    if i > 10:
        return
    else:
        print(f"{num} * {i} = {num*i}")
        multiplication_table(num, i+1)
        
multiplication_table(num, 1)