# Write a Python program to find median of a set of numbers.
def median(lst):
    lst.sort()  
    n = len(lst)
    if n%2 == 0:
        return (lst[n//2-1] + lst[n//2])/2
    else:
        return lst[n//2]

lst = [1, 2, 3, 4, 6, 7, 8, 9, 10]
print(median(lst)) 