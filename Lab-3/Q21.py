# Write a Python program to calculate Sum & Average of an integer array.
def sum_average(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum, sum/len(lst)

arr = int(input('Enter the number of elements in the array: '))
lst = []
for i in range(arr):
    lst.append(int(input('Enter the element: ')))

print(f"Sum: {sum_average(lst)[0]}")
print(f"Average: {sum_average(lst)[1]}")