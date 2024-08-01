import math

def solve_quadratic():
    # Taking input from the user
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"The roots are real and different: {root1} and {root2}"
    elif discriminant == 0:
        # One real root
        root = -b / (2*a)
        return f"The root is real and same: {root}"
    else:
        # Complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return f"The roots are complex: {real_part} ± {imaginary_part}i"

# Solve the quadratic equation and print the result
result = solve_quadratic()
print(result)
