import math

# Function to get user input and calculate the sum of square roots
def sum_of_square_roots():
    numbers = []
    for i in range(3):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    sum_sqrt = sum(math.sqrt(num) for num in numbers)
    return sum_sqrt

# Calculate and print the result
result = sum_of_square_roots()
print(f"The sum of the square roots is: {result}")
