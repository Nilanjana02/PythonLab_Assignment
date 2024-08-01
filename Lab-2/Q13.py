# Write a Python program to print the first 6 terms of a geometric sequence starting with 2 and having a common ratio of 3. means 2, 6, 18, 54, 162, 486
num = 2

def geometric_sequence(num, i):
    if i > 6:
        return
    else:
        print(num, end = ", ")
        geometric_sequence(num*3, i+1)

geometric_sequence(num, 1)