# Print the series upto N terms: 1,2,6,24,120,720 … N means 1*1, 1*2, 2*3, 6*4, 24*5, 120*6 … N
num = 1
N = int(input("Enter the number of terms: "))
def series(num, N):
    if N == 0:
        return
    else:
        print(num, end = ", ")
        series(num*(N), N-1)


series(num, N)

