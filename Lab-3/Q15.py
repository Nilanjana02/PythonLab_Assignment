# Write a Python program to generate all combination of 1, 2, or 3 using loop
def combination():
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                print(i, j, k)
combination()