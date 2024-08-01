# Write a Python program to find all roots of a quadratic equation.
def roots(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + d**0.5) / 2*a
        x2 = (-b - d**0.5) / 2*a
        return x1, x2
    elif d == 0:
        x = -b / 2*a
        return x
    else:
        return "No real roots"
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
print(roots(a, b, c))