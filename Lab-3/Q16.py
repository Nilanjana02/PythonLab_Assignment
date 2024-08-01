# Write a Python program to read two integer values m and n and to decide and print whether m is multiple of n.

def multiple(m, n):
    if m % n == 0:
        return True
    else:
        return False

m = int(input('Enter the value of m: '))
n = int(input('Enter the value of n: '))
print(multiple(m, n))