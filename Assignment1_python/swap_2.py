def swap_two(a,b):
    s = a
    a = b
    b = s
    print("After swap a = ",a," b = ",b)
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
swap_two(a,b)    