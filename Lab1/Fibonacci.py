def Fibonacci(n):
    if n==1:
        print(0)
    if n==2:
        print(0)
        print(1)
    if n>2:
        C = 0
        f1 = 0
        f2 = 1 
        print(f1)
        print(f2)
        C = 2   
        while C<n:
            f3 = f1+f2
            print(f3)
            C += 1
            f1 = f2
            f2 = f3
    
            
n = int(input("Enter how many Fibonacci number you want to display: "))
Fibonacci(n) 

